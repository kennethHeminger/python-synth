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

- The script uses a streaming audio output with an audio_callback(outdata, frames, time, status) function to generate sound in real time.

#### Each callback:

- Builds a time array for the requested number of samples.

- Sums sine waves for all currently pressed keys using their mapped frequencies.

- Normalizes by the number of active notes and applies a global volume to avoid clipping.

- Writes the resulting buffer into outdata as mono audio.

#### Pygame is responsible for:

- Opening a window and running the main event loop.

- Tracking which keys are currently pressed (pressed_keys set).

- This replaces earlier stages that used precomputed wave buffers and pygame.mixer.Sound.play(loops=-1).
---
## Roadmap

#### Planned next stages:

##### Stage 4 – Add oscillator controls and envelopes:

- Multiple waveforms (sine/square/saw).

- Simple ADSR‑style amplitude shaping.
- Optional drone voices.
- Delays and Reverb

##### Stage 5 – Add drum machine/Looper:

- Key‑triggered drum pads (kick/snare/hat) using samples.

- A simple step sequencer to play drum patterns automatically.

- Stage 6 – Port the project to a Raspberry Pi and tune audio settings for low latency.

- Stage 7 – Integrate a Teensy/MIDI controller to trigger notes and drums.
