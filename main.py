import pygame
from keymap import key_to_freq
from audio_engine import pressed_keys, start_audio_engine, stop_audio_engine
from lfo import lfo

current_lfo = 0

def handle_lfo_key(event):
    """Keyboard controls for LFO selection and parameters."""
    global current_lfo
    if event.type != pygame.KEYDOWN:
        return

    # Select which LFO to edit: 1 = LFO1, 2 = LFO2
    if event.key == pygame.K_1:
        current_lfo = 0
    elif event.key == pygame.K_2:
        current_lfo = 1

    l = lfo[current_lfo]

    # Toggle enable/disable
    if event.key == pygame.K_SPACE:
        l["enabled"] = not l["enabled"]

    # Wave select: Q/W/E/R = sine/triangle/saw/square
    elif event.key == pygame.K_q:
        l["wave"] = "sine"
    elif event.key == pygame.K_w:
        l["wave"] = "triangle"
    elif event.key == pygame.K_e:
        l["wave"] = "saw"
    elif event.key == pygame.K_r:
        l["wave"] = "square"

    # Rate up/down (speed)
    elif event.key == pygame.K_UP:
        l["rate"] = min(20.0, l["rate"] + 0.5)
    elif event.key == pygame.K_DOWN:
        l["rate"] = max(0.05, l["rate"] - 0.5)

    # Pitch depth (intensity)
    elif event.key == pygame.K_RIGHT:
        l["pitch_depth"] = min(0.1, l["pitch_depth"] + 0.005)
    elif event.key == pygame.K_LEFT:
        l["pitch_depth"] = max(0.0, l["pitch_depth"] - 0.005)

    # Amp depth (tremolo amount)
    elif event.key == pygame.K_z:
        l["amp_depth"] = max(0.0, l["amp_depth"] - 0.05)
    elif event.key == pygame.K_x:
        l["amp_depth"] = min(1.0, l["amp_depth"] + 0.05)

def draw_lfo_panel(screen, font):
    """Simple HUD to show current LFO settings."""
    panel_w, panel_h = 260, 120
    x, y = 10, 10

    # background rectangle
    pygame.draw.rect(screen, (0, 0, 0), (x, y, panel_w, panel_h))
    pygame.draw.rect(screen, (80, 80, 80), (x, y, panel_w, panel_h), 2)

    l = lfo[current_lfo]

    lines = [
        f"LFO: {current_lfo + 1} ({l['name']})",
        f"Enabled: {l['enabled']}",
        f"Wave: {l['wave']}",
        f"Rate: {l['rate']:.2f} Hz",
        f"Pitch depth: {l['pitch_depth']:.3f}",
        f"Amp depth: {l['amp_depth']:.2f}",
        f"Cutoff depth: {l['cutoff_depth']:.2f}",
    ]

    y_offset = y + 5
    for text in lines:
        img = font.render(text, True, (200, 200, 200))
        screen.blit(img, (x + 8, y_offset))
        y_offset += 16


def main():
    #init pygame
    pygame.init()

    # window to receive events
    WIDTH, HEIGHT = 1200, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stage 3.6 - Streaming Synth LFO Prototype")
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

            # Note release
            if event.type == pygame.KEYUP:
                if event.key in key_to_freq:
                    pressed_keys.discard(event.key)


            # LFO controls
            handle_lfo_key(event)

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

        # Draw LFO HUD
        draw_lfo_panel(screen, font)

        pygame.display.flip()

        clock.tick(60) # Limit redraw to 60 FPS

    stop_audio_engine(stream)
    pygame.quit()

if __name__ == "__main__":
    main()