import pygame

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