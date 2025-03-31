from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from typing import List
import logging
from .config import settings
from .transcriber import WhisperTranscriber

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION
)

transcriber = WhisperTranscriber()

@app.post("/transcribe")
async def transcribe_audio(files: List[UploadFile] = File(...)):
    try:
        if not files:
            raise HTTPException(status_code=400, detail="No files provided")

        for file in files:
            # Validação de extensão
            if not any(file.filename.lower().endswith(ext) for ext in settings.ALLOWED_EXTENSIONS):
                raise HTTPException(
                    status_code=400,
                    detail=f"File type not allowed. Allowed types: {settings.ALLOWED_EXTENSIONS}"
                )
            
            # Validação de tamanho
            content = await file.read()
            file_size_mb = len(content) / (1024 * 1024)
            if file_size_mb > settings.MAX_FILE_SIZE_MB:
                raise HTTPException(
                    status_code=400,
                    detail=f"File too large. Maximum size is {settings.MAX_FILE_SIZE_MB}MB"
                )
            await file.seek(0)

        results = await transcriber.process_files(files)
        return JSONResponse(content={"results": results})

    except Exception as e:
        logger.error(f"Error processing transcription: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"
