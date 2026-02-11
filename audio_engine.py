import numpy as np
import math
import sounddevice as sd
from keymap import key_to_freq
from oscillators import oscillators, osc_wave

# --- CONFIG ---
sample_rate = 44100    # samples per second
volume = 0.2           # 0.0 to 1.0

pressed_keys = set() # Tracks currently played keys
phase = 0.0 # Global phase counter so wave form is continuous across callback calls

def audio_callback(outdata, frames, time, status):
    # param outdata: Numpy array for writing audio sample into
    # param frames: number of samples requested

    global phase

    # Create a time axis for this block of samples.
    # np.arrange(frames) -> [0, 1, 2, ..., frames-1]
    # Add phase so time continues from previous call.
    # Divide by sample_rate to convert from sample index to seconds.
    t = (np.arange(frames) + phase) / sample_rate

    # Advance phase so next callback starts where this one ended
    phase += frames

    # Starts will silence
    sig = np.zeros(frames, dtype=np.float32)

    active_keys = list(pressed_keys)

    if active_keys:
        for key in active_keys:
            base_freq = key_to_freq.get(key)
            if base_freq is None:
                continue


            # Generate a sine wave for this key over time
            note_sig = np.zeros(frames, np.float32)

            for osc in oscillators:
                f = base_freq * (1.0 + osc["detune"])
                note_sig += osc["level"] * osc_wave(osc["wave"], f, t)

            note_sig /= float(len(oscillators))
            sig += note_sig

        # Start of polyphony
        # divide by number of notes so more notes don't just multiply the volume
        sig /= math.sqrt(len(active_keys))

    # applying volume to prevent output from clipping
    sig *= volume

    # Shaping audio buffer into a 2d column
    outdata[:] = sig.reshape(-1, 1)

def start_audio_engine():
    # Creates an output stream that will call audio_callback to get audio samples
    stream = sd.OutputStream(
        samplerate=sample_rate,
        channels=1,
        dtype='float32', #32 channels for polphony
        callback=audio_callback,
        blocksize=512,
    )
    stream.start()
    return stream

def stop_audio_engine(stream):
    stream.stop()
    stream.close()