import math
import numpy as np
                        # Static Tone
oscillators = [
    {"wave": "saw", "detune": 0.0, "level": 0.7},
    {"wave": "square", "detune": 0.02, "level": 0.5}
]

def osc_wave(wave_type: str, freq: float, t: np.ndarray) -> np.ndarray:
    # Generates one oscillator waveform for given type, frequency and time axis
    phase = 2.0 * math.pi * freq * t

    if wave_type == "sine":
        return np.sin(phase, dtype = np.float32)

    if wave_type == "square":
        return np.sign(np.sin(phase)).astype(np.float32)

    if wave_type == "saw":
        ft = (freq * t) % 1.0
        return (2.0 * ft - 1.0).astype(np.float32)

    # Fallback
    return np.sin(phase, dtype = np.float32)

