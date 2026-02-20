import math
import numpy as np

lfo = [
    {
        "name": "LFO1",
        "wave": "triangle",    # "sine", "triangle", "saw", "square"
        "rate": 5.0,           # Hz
        "pitch_depth": 0.01,   # +/- fraction of base pitch
        "cutoff_depth": 0.0,   # for filter
        "amp_depth": 0.0,      # tremolo
        "phase": 0.0,          # 0..1
        "enabled": True,
        "sync": False,
    },
    {
        "name": "LFO2",
        "wave": "sine",
        "rate": 0.3,
        "pitch_depth": 0.0,
        "cutoff_depth": 0.0,
        "amp_depth": 0.0,
        "phase": 0.0,
        "enabled": False,
        "sync": False,
    },
]

def lfo_waveform(wave: str, cycles: np.ndarray) -> np.ndarray:
    frac = cycles % 1.0 # 0..1 per cycle

    if wave == "saw":
        out = 2.0 * frac - 1.0
    elif wave == "square":
        out = np.sign(np.sin(2.0 * math.pi * frac))
    elif wave == "sine":
        out = np.sin(2.0 * math.pi * frac)
    else:  # triangle (default!)
        frac = cycles % 1.0
        out = 2.0 * np.abs(2.0 * frac - 1.0) - 1.0

    return out.astype(np.float32)

def render_lfos(t: np.ndarray, frames: int, sample_rate: int):
    outputs = []

    for l in lfo:
        if not l["enabled"]:
            outputs.append(np.zeros_like(t, dtype=np.float32))
            continue

        cycles = l["rate"] * t + l["phase"]
        sig = lfo_waveform(l["wave"], cycles)

        block_cycles = l["rate"] * (frames / sample_rate)
        l["phase"] = (l["phase"] + block_cycles) % 1.0

        outputs.append(sig)

    return outputs