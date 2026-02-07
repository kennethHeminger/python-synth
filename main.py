import pygame
import numpy as np
import math

# --- CONFIG ---
sample_rate = 44100    # samples per second
note_ms = 300      # length of beep in milliseconds
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

def sine_sound(freq_hz: float, duration_ms: int) -> pygame.mixer.Sound:
    """Create a pygame Sound object for a sine wave"""
    duration_sec = duration_ms / 1000.0

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
    sound = pygame.sndarray.make_sound(stereo_audio)
    return sound

def main():
    #init pygame & audio
    pygame.init()
    pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)

    # window to receive events
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Stage 3 - adding notes")

    # Generate sounds for each key beforehand
    note_sounds = {}
    for key, freq in key_to_freq.items():
        note_sounds[key] = sine_sound(freq, note_ms)


    running = True
    while running:
        for event in pygame.event.get():
            #Quitting event
            if event.type == pygame.QUIT:
                running = False

            # "the keyboard"
            if event.type == pygame.KEYDOWN:
                if event.key in note_sounds:
                    note_sounds[event.key].play(maxtime=note_ms)

    pygame.quit()

if __name__ == "__main__":
    main()