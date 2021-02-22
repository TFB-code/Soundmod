Soundmod for Python (Windows) by TFB
Latest version at https://github.com/TFB-code/soundmod

Relies on : 
	ctypes 
	winmm.dll 

Pros : 
	Allows multichannel sound.
	Lightweight.
	Works for MP3s.

Cons :
	Not cross platform.
	No channel monitoring.
	Manage your own memory and processing (i.e. don't play 20 wavs simultaneously and expect no detriment.)


Commands : 
	alias = assignwav(filename) - this will load a wav(or mp3), see examples.

	playwav(alias) - either a filename or an alias will work here.

	stopwav(alias)

	resumewav(alias)

	setvol([vl.off|vl.low|vl.mid|vl.high|vl.full])

	freewav(alias) - free an individual wav alias from memory.

	closewavs() - free all wav aliases from memory.  Do this at program termination.

Example 1 :

	from soundmod import *

	playwav("test.wav")

	{{{{rest of your code here}}}}

	closewavs()


Example2 :

	from soundmod import *

	test=assignwav("test.wav")

	setvol(vl.mid)

	playwav(test)

	{{{{rest of your code here}}}}

	freewav(test)


FAQ
---

Q : Why won't my wav file play?

A : If your filename includes a \ then it needs to be a raw string, i.e. (r"c:\myfilename.wav") rather than ("c:\myfilename.wav").

Some Wav formats don't play for some reason, but a good work around is to resave them in your favourite wav editor(Audacity maybe) and that can fix the format.

Finally, make sure the program is not just dropping through as once you free a wav or closewavs() then sound playback stops.



