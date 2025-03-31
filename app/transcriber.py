import whisper
import logging
from fastapi import UploadFile
from typing import List
import tempfile
import os
from .config import settings

logger = logging.getLogger(__name__)

class WhisperTranscriber:
    def __init__(self):
        logger.info(f"Initializing Whisper model '{settings.WHISPER_MODEL}' on {settings.DEVICE}")
        self.model = whisper.load_model(settings.WHISPER_MODEL, device=settings.DEVICE)

    async def process_files(self, files: List[UploadFile]):
        results = []
        
        for file in files:
            try:
                # Criar arquivo temporário
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as temp_file:
                    content = await file.read()
                    temp_file.write(content)
                    temp_file.flush()
                    
                    # Transcrever o áudio
                    result = self.model.transcribe(
                        temp_file.name,
                        language=settings.LANGUAGE,
                        task="transcribe"
                    )
                    
                    results.append({
                        "filename": file.filename,
                        "transcript": result["text"]
                    })
                    
                # Limpar arquivo temporário
                os.unlink(temp_file.name)
                
            except Exception as e:
                logger.error(f"Error processing file {file.filename}: {str(e)}")
                results.append({
                    "filename": file.filename,
                    "error": str(e)
                })
                
        return results
