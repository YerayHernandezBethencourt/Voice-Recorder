import sounddevice
from scipy.io.wavfile import write

fs = 44100 # Sample rate
seconds = 10

try:
    print("recording...")
    # Recording
    record_voice = sounddevice.rec(int(seconds * fs), samplerate=fs, channels=2)
    sounddevice.wait()  # Wait until recording is finished
    print("finished recording")
except:
    print("error recording")

write("output.wav", fs, record_voice)
print("done recording")
