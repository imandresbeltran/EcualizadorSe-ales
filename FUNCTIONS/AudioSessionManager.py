import os
import shutil
import tempfile
from pydub import AudioSegment

class AudioSessionManager:
    def __init__(self):
        self.session_dir = tempfile.mkdtemp(prefix="audio_session_")
        self.file_path = None

    def save_audio_copy(self, original_path):
        self.file_path = os.path.join(self.session_dir, os.path.basename(original_path))

        try:
            shutil.copy2(original_path, self.file_path)
            return self.file_path
        except IOError as e:
            print(f"Error al copiar el archivo de audio a la carpeta de sesión: {e}")
            return None
        
    def get_session_audio_path(self):
        return self.file_path
    
    def clean_up(self):
        if os.path.exists(self.session_dir):
            shutil.rmtree(self.session_dir, ignore_errors=True)