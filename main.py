import pygame
import numpy as np
import math

# --- CONFIG ---
sample_rate = 44100    # samples per second
volume = 0.3           # 0.0 to 1.0


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

def sine_sound(freq_hz: float) -> pygame.mixer.Sound:
    """Create a pygame Sound object for a sine wave"""
    duration_sec = 1.0 # buffer length,

    # Time axis: 0 to duration_sec, sample_rate * duration_sec samples
    num_samples = int(sample_rate * duration_sec)
    t = np.linspace(0, duration_sec, num_samples, endpoint=False)

    # Sine wave between -1.0 and 1.0
    waveform = np.sin(2.0 * math.pi * freq_hz * t)

    # Applying Volume
    waveform *= volume

    # Convert to 16-bit signed integers
    audio = np.int16(waveform * 32767)
    stereo_audio = np.column_stack((audio, audio))

    # Turn numpy array into a pygame Sound
    return pygame.sndarray.make_sound(stereo_audio)

def main():
    #init pygame & audio
    pygame.init()
    pygame.mixer.init(frequency= sample_rate, size= -16, channels= 2)

    # window to receive events
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Stage 3.1 - holding notes with keys")

    # Generate sounds and currently playing channels for key
    note_sounds = {key: sine_sound(freq) for key, freq in key_to_freq.items()}
    playing_channels = {}


    running = True
    while running:
        for event in pygame.event.get():
            #Quitting event
            if event.type == pygame.QUIT:
                running = False

            # The keyboard
            if event.type == pygame.KEYDOWN:
                if event.key in note_sounds and event.key not in playing_channels:
                    ch = note_sounds[event.key].play(loops = -1) #loops note while held down
                    playing_channels[event.key] = ch

            if event.type == pygame.KEYUP:
                if event.key in playing_channels:
                    playing_channels[event.key].stop()
                    del playing_channels[event.key]

    pygame.quit()

if __name__ == "__main__":
    main()