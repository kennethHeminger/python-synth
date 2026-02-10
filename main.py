import pygame
from keymap import key_to_freq
from audio_engine import pressed_keys, start_audio_engine, stop_audio_engine

def main():
    #init pygame
    pygame.init()

    # window to receive events
    screen = pygame.display.set_mode((600, 200))
    pygame.display.set_caption("Stage 3.2 - Streaming Synth Prototype")
    clock = pygame.time.Clock()  # clock to cap frame rate

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

            # Note release
            if event.type == pygame.KEYUP:
                if event.key in key_to_freq:
                    pressed_keys.discard(event.key)

        clock.tick(60) # Limit redraw to 60 FPS

    stop_audio_engine(stream)
    pygame.quit()

if __name__ == "__main__":
    main()