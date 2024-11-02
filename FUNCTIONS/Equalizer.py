from pydub import AudioSegment
from pydub.effects import low_pass_filter, high_pass_filter

class Equalizer:
    def __init__(self):
        self.modes = {
            "Normal": self.normal,
            "Pop": self.pop,
            "Rock": self.rock,
            "Jazz": self.jazz,
            "Classical": self.classical,
            "Bass Boost": self.bass_boost
        }
        self.current_mode = "Normal"

    def set_mode(self,mode):
        if mode in self.modes:
            self.current_mode = mode

    def apply_equalizer(self, audio_segment):
        return self.modes[self.current_mode](audio_segment)
    
    def normal(Self, audio_segment):
        return audio_segment
    
    def pop(self, audio_segment):
        return audio_segment.low_pass_filter(3000).high_pass_filter(500)
    
    def rock(self, audio_segment):
        return audio_segment.low_pass_filter(4000).high_pass_filter(1000)
    
    def jazz(self, audio_segment):
        return audio_segment.low_pass_filter(5000).high_pass_filter(200)
    
    def classical(self, audio_segment):
        return audio_segment.low_pass_filter(6000).high_pass_filter(300)
    
    def bass_boost(self, audio_segment):
        return audio_segment.low_pass_filter(100).high_pass_filter(20)