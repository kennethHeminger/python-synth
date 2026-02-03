import pygame
import numpy as np
import math

# --- CONFIG ---
sample_rate = 44100    # samples per second
duration_ms = 300      # length of beep in milliseconds
volume = 0.3           # 0.0 to 1.0
frequency = 440.0      # A4, 440 Hz

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
    pygame.display.set_caption("Stage 2 - generate sine beep on space")

    beep_sound = sine_sound(frequency,duration_ms)

    running = True
    while running:
        for event in pygame.event.get():
            #Quitting event
            if event.type == pygame.QUIT:
                running = False

            #Space for beep
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    beep_sound.play()

    pygame.quit()

if __name__ == "__main__":
    main()