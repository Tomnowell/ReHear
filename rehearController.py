from playsound import *

import pyaudio
import wave

filename = 'bufferFile.wav'
# set chunk (of samples) size
chunkSize = 1024
sampleSize = 44100


waveFile = wave.open(filename, 'rb')

port = pyaudio.PyAudio()

# make a stream
stream = port.open(format=port.get_format_from_width(waveFile.getsampwidth(
)), channels=wf.getnchannels(), rate=waveFile.getframerate(), output=True)

# read data in samples
data = waveFile.readframes(sampleSize)


# wrap some wave open and close functions because we may change this functionality later
def open_wav_for_reading(filename):
    return (wav_file=wave.open(filename, 'rb'))


def open_wav_for_writing(filename):
    return (wav_file=wave.open(filename, 'wb'))


def set_number_of_channels(wav_file, number_of_channels):
    try:
        wav_file.setnchannels(number_of_channels)
    except wave.Error:
        print('Wave error! Bye bye...waving')


def set_sample_width(wav_file, sample_width):
    try:
        wav_file.setsampwidth(sample_width)
    except wave.Error:
        print('Wave error! Wave bye bye!')
    finally:
        return wav_file


def set_frame_rate(wav_file, frame_rate):
    try:
        wav_file.setframerate(frame_rate)
    except wave.Error:
        print('Wave error! Bye bye')
    finally:
        return wav_file


def build_stream(wav_file, output=True):
    port = pyaudio.PyAudio()
    format = port.get_format_from_width(wav_file.getsampwidth())
    channels = wav_file.getnchannels()
    rate = wav_file.getframerate()

    stream = port.open(format, channels, rate, output)
    return stream


def play(filename):

    stream = build_stream(wav_file)

    # Load initial chunk
	data = wav_file.readframes(chunkSize)

	while data != '':
		stream.write(data)
		data = wave_file.readframes(chunkSize)  # Next chunk

    stream.close()
	print('Stopped playing')

	return(0)


def record(button_not_pressed):
	sample_format = pyaudio.paInt16  # use 16-bit audio
	sample_rate = 44100  # CD quality audio.  Remember CDs?
	channels = 2  # Use stereo for now
	seconds = 30

	stream = port.open(format=sample_format, channels=channels,
	                   rate=sample_rate, frames_per_buffer=chunkSize, input=True)
	frames = []
	int i = 0
	while(button_not_pressed):  # replace with event handler

		# First fill a 30 second buffer
		if (i < int(sample_rate / chunkSize * seconds))):
			data=stream.read(chunkSize)
			frame.append(data)


		else:  # Buffer is full, keep it trimmed and topped up
			frame.pop(0)
			frame.append(data)

		i++

	# button pressed logic
	stream.stop_stream()
	stream.close()

	# terminate PortAudio interface
	port.terminate()

	print('Stopped Recording')

	return(frames)


waveFile.close()
