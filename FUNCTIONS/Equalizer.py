import numpy as np
from scipy.fft import fft, ifft

class Equalizer:
    def __init__(self, sample_rate=44100, block_size=1024):
        self.sample_rate = sample_rate
        self.block_size = block_size
        self.freqs = np.fft.fftfreq(block_size, 1 / sample_rate)
        self.current_mode = "Normal"

        # Definir modos y ganancia para cada rango de frecuencias
        self.modes = {
            "Normal": (None, 1.0),  # Sin ganancia
            "Pop": ((250, 4000), 1.5),  # Frecuencias medias y algo de altas
            "Rock": ((100, 5000), 1.8),  # Bajos y medios
            "Jazz": ((200, 5000), 1.6),  # Predominancia de medios
            "Classical": ((300, 8000), 1.2),  # Mejora claridad de agudos
            "Bass Boost": ((20, 250), 2.0)  # Enfocado en bajos
        }

        self.mode_masks = {mode: None for mode in self.modes}

    def set_mode(self, mode):
        """Define el modo actual de ecualización."""
        if mode in self.modes:
            self.current_mode = mode
            freq_range, gain = self.modes[mode]
            if freq_range:
                low_cutoff, high_cutoff = freq_range
                self.mode_masks[mode] = self.create_mask(low_cutoff, high_cutoff, gain)

    def apply_mode(self, freq_domain):
        """Aplica el filtro en el dominio de la frecuencia."""
        if self.current_mode == "Normal":
            return freq_domain
        mask = self.mode_masks[self.current_mode]
        if mask is None:
            return freq_domain
        return freq_domain * mask[:len(freq_domain)]

    def apply_equalizer(self, samples):
        """Aplica el ecualizador en el array de muestras."""
        processed_samples = np.zeros_like(samples, dtype=np.float32)

        # Procesar en bloques
        for start in range(0, len(samples), self.block_size):
            end = min(start + self.block_size, len(samples))
            block = samples[start:end]

            # FFT y aplicación del filtro
            freq_domain = fft(block, n=self.block_size)
            filtered_block = self.apply_mode(freq_domain)

            # Inversa FFT y conversión a tiempo
            time_domain_block = ifft(filtered_block).real
            processed_samples[start:end] = time_domain_block[:end - start]

        return processed_samples.astype(np.int16)

    def create_mask(self, low_cutoff, high_cutoff, gain=1.0):
        """Crea una máscara de frecuencia con ganancia ajustada."""
        mask = np.ones(self.block_size, dtype=np.float32)
        mask[(self.freqs >= low_cutoff) & (self.freqs <= high_cutoff)] = gain
        return mask
