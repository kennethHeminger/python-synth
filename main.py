import pygame
import numpy as np
import math
import sounddevice as sd

# --- CONFIG ---
sample_rate = 44100    # samples per second
volume = 0.2           # 0.0 to 1.0

# Mapping key to frequencies in hz
key_to_freq = {
    pygame.K_a: 261.63,         # C4
    pygame.K_s: 277.18,         # C#4 / Db4
    pygame.K_d: 293.66,         # D4
    pygame.K_f: 311.13,         # D#4 / Eb4
    pygame.K_g: 329.63,         # E4
    pygame.K_h: 349.23,         # F4
    pygame.K_j: 369.99,         # F#4 / Gb4
    pygame.K_k: 392.00,         # G4
    pygame.K_l: 415.30,         # G#4 / Ab4
    pygame.K_SEMICOLON: 440.00, # A4
    pygame.K_QUOTE: 466.16,     # A#4 / Bb4
    pygame.K_RETURN: 493.88,    # B4
}

pressed_keys = set() # Tracks currently played keys
phase = 0.0 # Global phase counter so wave form is continuous across callback calls

def audio_callback(outdata, frames, time, status):
    """
    :param outdata: Numpy array for writing audio sample into
    :param frames: number of samples requested
    """
    global phase

    # Create a time axis for this block of samples.
    # np.arrange(frames) -> [0, 1, 2, ..., frames-1]
    # Add phase so time continues from previous call.
    # Divide by sample_rate to convert from sample index to seconds.
    t = (np.arange(frames) + phase) / sample_rate

    # Advance phase so next callback starts where this one ended
    phase += frames

    # Stats will silence
    sig = np.zeros(frames, dtype=np.float32)

    active_keys = list(pressed_keys)

    if active_keys:
        for key in active_keys:
            freq = key_to_freq.get(key)
            if freq is None:
                continue

            # Generate a sine wave for this key over time
            sig += np.sin(2.0 * math.pi * freq * t).astype(np.float32)

        # Start of polyphony
        # divide by number of notes so more notes don't just multiply the volume
        sig /= float(len(pressed_keys))

    # applying volume to prevent output from clipping
    sig *= volume

    # Shaping audio buffer into a 2d column
    outdata[:] = sig.reshape(-1, 1)

def main():
    #init pygame & audio
    pygame.init()
    pygame.mixer.init(frequency= sample_rate, size= -16, channels= 2, buffer = 512)
    pygame.mixer.set_num_channels(32) #Up to 32 channels for polyphony

    # window to receive events
    screen = pygame.display.set_mode((600, 200))
    pygame.display.set_caption("Stage 3.2 - Streaming Synth Prototype")
    clock = pygame.time.Clock()  # clock to cap frame rate

    # Audio
    # Create an output stream that will call audio_callback to get audio samples
    stream = sd.OutputStream(
        samplerate = sample_rate,
        channels = 1,
        dtype = 'float32',
        callback = audio_callback,
        blocksize = 512,
    )

    stream.start()


    running = True
    while running:
        for event in pygame.event.get():
            #Quitting event
            if event.type == pygame.QUIT:
                running = False

            # The keyboard
            if event.type == pygame.KEYDOWN:
                if event.key in key_to_freq:
                    pressed_keys.add(event.key)

            # Note release
            if event.type == pygame.KEYUP:
                if event.key in key_to_freq:
                    pressed_keys.discard(event.key)

        clock.tick(60) # Limit redraw to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()