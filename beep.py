import math
import wave
import struct

SAMPLE_RATE = 44100
DURATION_SEC = 0.3
FREQUENCY = 440.0  # A4
with wave.open("beep.wav", "w") as wf:
    wf.setnchannels(1)       # mono
    wf.setsampwidth(2)       # 16-bit
    wf.setframerate(SAMPLE_RATE)

    num_samples = int(SAMPLE_RATE * DURATION_SEC)
    for n in range(num_samples):
        t = n / SAMPLE_RATE
        sample = 0.3 * math.sin(2 * math.pi * FREQUENCY * t)
        value = int(sample * 32767.0)
        data = struct.pack("<h", value)
        wf.writeframesraw(data)
