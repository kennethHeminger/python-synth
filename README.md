## Python PolySynth/Drum Machine – Stage 3

---

### Streaming Keyboard Synth (Python + Pygame + sounddevice)

A small virtual‑analog polyphonic synthesizer written in Python using NumPy and sounddevice. 
It’s designed as a learning project for building a Raspberry Pi‑ready synth engine with multiple oscillators and real‑time audio output

---

## Features

- Simple real‑time audio stream using sounddevice.
- Computer keyboard acts as a piano: notes from `A` through `Return` (C4–B4).
- Multiple keys can be held at once for basic polyphony.
- Small, readable script intended as Stage 3 of a multi‑stage synth/drum machine project.

---
## Structure
- main.py –  Entry point; starts the audio engine and handles input events.
- audio_engine.py – Audio callback, stream setup, voice mixing, volume control.
- oscillators.py – Oscillator definitions and waveform generation helpers.
- keymap.py – Maps keys (e.g., QWERTY rows) to musical note frequencies.


---
## Requirements

- Python 3.x +
- [Pygame](https://www.pygame.org/)
- [python-sounddevice](https://python-sounddevice.readthedocs.io/)
- NumPy

Install with:

```bash
pip install pygame sounddevice numpy
```

## How to Run

- Clone or download this repository.

- Install dependencies (see Requirements above).

- Run the Stage 3 script (filename example):
```bash
python stage3_streaming_synth.py
```
- Press keys A through Return to play notes.

- Close the Pygame window to exit.

---
## How It Works

-  main.py creates and starts the audio stream via start_audio_engine().

- A background callback in audio_engine.py pulls pressed_keys and generates audio each block.

- oscillators.py generates the raw waveforms for each oscillator and note.

- Keyboard events add/remove entries in pressed_keys so you can play notes.



#### Each callback:

- Builds a time array for the requested number of samples.

- Sums sine waves for all currently pressed keys using their mapped frequencies.

- Normalizes by the number of active notes and applies a global volume to avoid clipping.

- Writes the resulting buffer into outdata as mono audio.

#### Pygame is responsible for:

- Opening a window and running the main event loop.

- Tracking which keys are currently pressed (pressed_keys set).
---
## Roadmap

#### Planned next stages:

##### Stage 4 – Add oscillator controls and envelopes:

- Simple ADSR‑style amplitude shaping.

- Optional drone voices.

- Delays and Reverb

##### Stage 5 – Add drum machine/Looper:

- Key‑triggered drum pads (kick/snare/hat) using samples.

- A simple step sequencer to play drum patterns automatically.

- Stage 6 – Port the project to a Raspberry Pi and tune audio settings for low latency.

- Stage 7 – Integrate a MIDI controller to trigger notes,drums,effects,etc.
