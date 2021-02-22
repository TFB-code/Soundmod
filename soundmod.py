## Soundmod, Copyright (c) 2021 TFB
## Use freely under zlib terms, see licence file.

from ctypes import WinDLL, c_buffer

global winmm
winmm=WinDLL('winmm.dll')

global aliasnum
aliasnum=0

class vl :
    off=0x00000000
    low=0x55555555
    mid=0x99999999
    high=0xCCCCCCCC
    full=0xFFFFFFFF

class sf :
    _sync=0
    _async=1
    _nodefault=2
    _memory=4
    _loop=8
    _nostop=16
    _nowait=8192
    _fromfile=131072

def buildwavheader(datasize=176400, samplerate=44100, channels=2, bps=16) :         # datasize of 176400 = 1 second of 16 bit stereo PCM audio
    header=bytes
    header=b'RIFF'
    header=header+int(datasize+36).to_bytes(4,byteorder='little')                   # length = data length + 44 header bytes - 8 bytes of first fields
    header=header+b'WAVE'
    header=header+b'fmt '
    header=header+int(16).to_bytes(4,byteorder='little')                            # 16 bytes for PCM format header
    header=header+int(1).to_bytes(2,byteorder='little')                             # 1 = PCM
    header=header+int(channels).to_bytes(2,byteorder='little')                      # number of channels, 1 = mono, 2 = stereo
    header=header+int(samplerate).to_bytes(4,byteorder='little')                    # samplerate
    header=header+int(samplerate*channels*(bps/8)).to_bytes(4,byteorder='little')   # byterate = samplerate * number of channels * bits per sample / 8
    header=header+int(channels*(bps/8)).to_bytes(2,byteorder='little')              # block align = number of channels * bits per sample / 8
    header=header+int(bps).to_bytes(2,byteorder='little')                           # bits per sample
    header=header+b'data'
    header=header+int(datasize).to_bytes(4,byteorder='little')                      # data length in bytes
    return header

def wavload(filename) :
    wavefile=open(filename,'rb',0)
    wave=wavefile.read()
    wavefile.close()
    datasize=int.from_bytes(wave[40:44],byteorder='little')
    return wave[0:44], wave[44:datasize+2]

def wavdataload(filename) :
    wavefile=open(filename,'rb',0)
    wave=wavefile.read()
    wavefile.close()
    datasize=int.from_bytes(wave[40:44],byteorder='little')
    return wave[44:datasize+2]

def wavdatasize(header) :
    return int.from_bytes(header[40:44],byteorder='little')

def wavtotalsize(header) :
    return int.from_bytes(header[4:8],byteorder='little')

def sendcommand(command) :
    global winmm
    buf=c_buffer(256)
    err=winmm.mciSendStringW(command, buf, 254, 0)
    return err

def assignwav(filename) :
    global aliasnum
    aliasnum=aliasnum+1
    alias='soundname'+str(aliasnum)
    sendcommand(r'Open '+filename+' alias '+alias)
    return alias

def freewav(alias) :
    sendcommand('Close '+alias)
    return

def playwav(alias) :
    sendcommand('Play '+alias+' from 0')
    return

def stopwav(alias) :
    sendcommand('Stop '+alias)
    return

def resumewav(alias) :
    sendcommand('Play '+alias)
    return

def setvol(volume) :
    winmm.waveOutSetVolume(None,volume)
    return volume

def closewavs() :
    sendcommand('Close all')
    return



