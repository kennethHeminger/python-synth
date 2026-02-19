import sys
import pygame
from keymap import key_to_freq
from audio_engine import pressed_keys, start_audio_engine, stop_audio_engine
from lfo import lfo

def main():
    #init pygame
    pygame.init()

    # window to receive events
    WIDTH, HEIGHT = 600, 200
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stage 3.2 - Streaming Synth Prototype")
    clock = pygame.time.Clock()  # clock to cap frame rate
    font = pygame.font.SysFont(None, 20)

    # Building keyboard from keymap
    key_order = list(key_to_freq.keys())

    key_width = WIDTH // len(key_order)
    key_height = 120
    key_rects = {}
    for i, k in enumerate(key_order):
        x = i * key_width
        rect = pygame.Rect(x, HEIGHT - key_height, key_width, key_height)
        key_rects[k] = rect

    # Minimal labels just for readability (no extra logic)
    key_labels = {
        pygame.K_a: "C4",
        pygame.K_s: "C#4",
        pygame.K_d: "D4",
        pygame.K_f: "D#4",
        pygame.K_g: "E4",
        pygame.K_h: "F4",
        pygame.K_j: "F#4",
        pygame.K_k: "G4",
        pygame.K_l: "G#4",
        pygame.K_SEMICOLON: "A4",
        pygame.K_QUOTE: "A#4",
        pygame.K_RETURN: "B4",
    }

    stream = start_audio_engine()

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

            # --LFO--

                # Wave select: 1:saw 2:triangle 3:square
                if event.key == pygame.K_1:
                    lfo["wave"] = "saw"
                elif event.key == pygame.K_2:
                    lfo["wave"] = "triangle"
                elif event.key == pygame.K_3:
                    lfo["wave"] = "square"

                # Rate up/down (speed)
                elif event.key == pygame.K_UP:
                    lfo["rate"] = min(20.0, lfo["rate"] + 0.5)
                elif event.key == pygame.K_DOWN:
                    lfo["rate"] = max(0.1, lfo["rate"] - 0.5)

                # Pitch depth (intensity)
                elif event.key == pygame.K_RIGHT:
                    lfo["pitch_int"] = min(0.1, lfo["pitch_int"] + 0.005)
                elif event.key == pygame.K_LEFT:
                    lfo["pitch_int"] = max(0.0, lfo["pitch_int"] - 0.005)

                    # Note release
            if event.type == pygame.KEYUP:
                if event.key in key_to_freq:
                    pressed_keys.discard(event.key)

        #Draw
        screen.fill((30, 30, 30))

        for k, rect in key_rects.items():
            color = (100, 180, 255) if k in pressed_keys else (240, 240, 240)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 0, 0), rect, 2)

            label = key_labels.get(k, "")
            if label:
                text = font.render(label, True, (0, 0, 0))
                text_rect = text.get_rect(center=(rect.centerx, rect.centery + 20))
                screen.blit(text, text_rect)

        pygame.display.flip()

        clock.tick(60) # Limit redraw to 60 FPS

    stop_audio_engine(stream)
    pygame.quit()

if __name__ == "__main__":
    main()