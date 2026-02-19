import math
import numpy as np

lfo = {
    "wave": "triangle",   # "saw", "triangle", "square"
    "rate": 5.0,          # Hz
    "pitch_int": 0.01,    # +/-1% pitch
    "phase": 0.0,         # cycles
}

def lfo_waveform(t: np.ndarray) -> np.ndarray:
    rate = lfo["rate"]
    phase = lfo["phase"]
    cycles = rate * t + phase

    if lfo["wave"] == "saw":
        frac = cycles % 1.0
        out = 2.0 * frac - 1.0
    elif lfo["wave"] == "square":
        out = np.sign(np.sin(2.0 * math.pi * cycles))
    else:  # triangle
        frac = cycles % 1.0
        out = 2.0 * np.abs(2.0 * frac - 1.0) - 1.0

    return out.astype(np.float32)

def advance_lfo(frames: int, sample_rate: int):
    lfo["phase"] += (lfo["rate"] * frames) / sample_rate
    lfo["phase"] %= 1.0