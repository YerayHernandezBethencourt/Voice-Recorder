import sounddevice as sd
from scipy.io.wavfile import write
import keyboard
import numpy as np
import time

fs = 44100  # Sample rate
output_file = "output.wav"
print("Press spacebar to start recording")

try:
    while True:
        # Wait for spacebar to be pressed
        keyboard.wait("space")
        print("recording...")
        
        # Start recording
        record = []
        stream = sd.InputStream(samplerate=fs, channels=2, dtype="int16")
        stream.start()
        
        # Give time for the stream to start
        time.sleep(0.1)  # Small delay to ensure stream is ready
        
        data_available = False
        
        while not keyboard.is_pressed("space"):
            audio_chunk, __ = stream.read(1024)
            if audio_chunk.size > 0:  # Ensure that we have audio data
                data_available = True
                record.append(audio_chunk)
            
        # Stop recording
        stream.stop()
        stream.close()
        print("finished recording")
        
        # Check that we actually have data
        if not data_available:
            raise ValueError("No audio data was recorded.")
        
        # Convert the list of numpy arrays into a single numpy array
        recording = np.concatenate(record, axis=0)
        
        # Save recording
        write(output_file, fs, recording)
        print("Recording saved to", output_file)
        break

except KeyboardInterrupt:
    print("exiting")
except Exception as e:
    print(f"error: {e}")
  