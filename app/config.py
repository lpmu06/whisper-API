from pydantic_settings import BaseSettings
import torch

class Settings(BaseSettings):
    # API Settings
    API_TITLE: str = "Whisper Transcription API"
    API_VERSION: str = "1.0.0"
    
    # Whisper Settings
    WHISPER_MODEL: str = "base"
    DEVICE: str = "cuda" if torch.cuda.is_available() else "cpu"
    LANGUAGE: str = "pt"
    
    # File Settings
    MAX_FILE_SIZE_MB: int = 25
    ALLOWED_EXTENSIONS: set = {"mp3", "wav", "m4a", "ogg"}

    class Config:
        env_file = ".env"

settings = Settings()
