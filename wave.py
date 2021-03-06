import pyaudio
import numpy as np

p = pyaudio.PyAudio()
valor = 25
volume = 1  # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 15.0   # in seconds, may be float
f = 60.0        # sine frequency, Hz, may be floadt

# generate samples, note conversion to float32 array
samples = (np.sin(2*np.pi*np.arange(fs*duration)*f /fs)).astype(np.float32)
while valor > 20:
    valor = int(input("gimme: "))

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(samples)
    

stream.stop_stream()
stream.close()

p.terminate()