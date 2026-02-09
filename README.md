## Synth/Drum Machine – Stage 3

---

### Streaming Keyboard Synth (Python + Pygame + sounddevice)

This project is the third step toward a Raspberry Pi synth.  
The goal in this stage is to move from preloaded/looped audio buffers to a **streaming synthesizer** that generates tones in real time using NumPy and a continuous audio callback.

---

## Features

- Simple real‑time audio stream driven by a callback function.
- Computer keyboard acts as a piano: notes from `A` through `Return` (C4–B4).
- Multiple keys can be held at once for basic polyphony.
- Small, readable script intended as Stage 3 of a multi‑stage synth/drum machine project.

---

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)
- [python-sounddevice](https://python-sounddevice.readthedocs.io/)
- NumPy

Install with:

```bash
pip install pygame sounddevice numpy
