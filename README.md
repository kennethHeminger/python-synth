## Synth/Drum Machine Stage 2

---
Key‑Triggered Beep (Python + Pygame)
This project is the second step toward a Raspberry Pi synth: when you press the space bar, it plays a short beep sound.
The goal is to replace part one's beep.wav with file with a tone generated via code using Numpy & Pygame logic

## Features

---
Simple event loop using Pygame.

Plays a sound when the space bar is pressed.

Small, readable script intended as Stage 2 of a multi‑stage synth/drum machine project.
 
## Requirements

---
- Python 3.x
- [Pygame]

## How to Run

---
1. Clone or download this repository.
2. Ensure `beep.wav` is in the same folder as `stage1_play_sound.py`.
3. Install dependencies (`pip install pygame`).
4. Run:

```bash
python stage1_play_sound.py
```
## How it works

---
Press the space bar to play the beep. Close the window to exit.<br>

The script initializes Pygame, 
configured basic audio settings: sample rate, beep duration (in milliseconds), 
volume, and a frequency like 440 Hz<br>
The main() function initializes Pygame and the mixer with matching settings (44100 Hz, 16‑bit, mono), 
creates a window, and enters the same event loop used in Stage 1.


## Roadmap

Planned next stages:

- Stage 3 – Map multiple keys to different notes and add basic note length control.
- Stage 4 – Add drum machine/Looper:
  - Key-triggered drum pads (kick/snare/hat) using samples.
  - A simple step sequencer to play drum patterns automatically.
- Stage 5 – Port the project to a Raspberry Pi and tune audio settings for low latency.
- Stage 6 – Integrate a Teensy-based MIDI controller to trigger notes and drums.
