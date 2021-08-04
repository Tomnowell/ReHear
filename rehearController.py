from playsound import *

import pyaudio
import wave

filename = 'bufferFile.wav'
# set sample size
chunkSize = 1024

waveFile = wave.open(filename, 'rb')

port = pyaudio.PyAudio()

# make a stream
stream = port.open(format = port.get_format_from_width(waveFile.getsampwidth()), channels = wf.getnchannels(), rate = waveFile.getframerate(), output = True)

# read data in samples
data = waveFile.readframes(sampleSize)

def record(button_not_pressed):
	sample_format = pyaudio.paInt16 # use 16-bit audio
	sample_rate = 44100 # CD quality audio.  Remember CDs?
	channels = 2 # Use stereo for now 
	seconds = 30

	stream = port.open(format = sample_format, channels = channels, rate = sample_rate, frames_per_buffer = chunkSize, input = True)
	frames = []
	int i = 0
	while(button_not_pressed): # replace with event handler
		
		#First fill a 30 second buffer
		if (i < int(sample_rate / chunkSize * seconds ))):
			data = stream.read(chunkSize)
			frame.append(data)
		
		
		else: # Buffer is full, keep it trimmed and topped up
			frame.pop(0)
			frame.append(data)
		
		i++
	
	#button pressed logic
	stream.stop_stream()
	stream.close()

	# terminate PortAudio interface
	port.terminate()
	
	print('Stopped Recording')

	return(frames)


		
	
		