# Whisper-API

API REST desenvolvida com FastAPI para transcrição de áudio para texto utilizando o modelo Whisper da OpenAI. A API é containerizada usando Docker e otimizada para transcrições em português brasileiro.

## 🚀 Funcionalidades

- Transcrição de áudio para texto usando o modelo Whisper
- Suporte para múltiplos arquivos de áudio
- Otimizado para português brasileiro
- Interface Swagger UI para testes (/docs)
- Suporte a GPU (CUDA) quando disponível
- Validação de arquivos e tratamento de erros
- Healthcheck endpoint

## 📋 Pré-requisitos

- Docker
- Docker Compose
- Git
- (Opcional) NVIDIA GPU com CUDA para melhor performance

## 🔧 Instalação e Execução

### 1. Clone o repositório
```bash
git clone https://github.com/lpmu06/whisper-API
cd whisper-api
```

### 2. Execute com Docker Compose
```bash
docker-compose up --build
```

A API estará disponível em `http://localhost:8000`

## 📝 Como Usar

### Endpoint Principal

- **URL**: `/transcribe`  # Atualizado de /whisper para /transcribe
- **Método**: `POST`
- **Content-Type**: `multipart/form-data`

### Exemplo de uso com cURL
```bash
curl -X POST "http://localhost:8000/transcribe" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "files=@seu_audio.mp3"
```

### Exemplo de uso com Python
```python
import requests

url = "http://localhost:8000/transcribe"
files = [
    ('files', ('audio.mp3', open('audio.mp3', 'rb'), 'audio/mpeg'))
]

response = requests.post(url, files=files)
print(response.json())
```

### Formatos de Áudio Suportados
- MP3 (.mp3)
- WAV (.wav)
- M4A (.m4a)
- OGG (.ogg)

### Limitações
- Tamanho máximo do arquivo: 25MB
- Apenas formatos de áudio suportados serão aceitos

### Resposta
A API retorna um JSON no seguinte formato:
```json
{
    "results": [
        {
            "filename": "audio.mp3",
            "transcript": "Texto transcrito do áudio..."
        }
    ]
}
```

## 🔍 Testando a API

1. Acesse a documentação Swagger UI em `http://localhost:8000/docs`
2. Expanda o endpoint POST `/transcribe`
3. Clique em "Try it out"
4. Faça upload de um arquivo de áudio
5. Execute e verifique a resposta

## ⚙️ Configuração Avançada

### Variáveis de Ambiente
- `WHISPER_MODEL`: Modelo Whisper a ser usado (default: "base")
  ```bash
  # Exemplo: usar modelo medium
  WHISPER_MODEL=medium docker-compose up

  # Modelos disponíveis:
  # - tiny
  # - base
  # - small
  # - medium
  # - large
  ```
- `MAX_FILE_SIZE_MB`: Tamanho máximo do arquivo em MB (default: 25)
- `LANGUAGE`: Idioma para transcrição (default: "pt")

### Usando GPU
A API automaticamente detecta e utiliza GPU se disponível. Para usar com GPU:

1. Instale os drivers NVIDIA
2. Instale o NVIDIA Container Toolkit
3. Execute com Docker Compose (configuração GPU já incluída)

## 🛠️ Desenvolvimento

### Estrutura do Projeto

whisper-api/
├── app/

│   ├── main.py         # Aplicação principal

│   ├── config.py       # Configurações

│   └── transcriber.py  # Lógica de transcrição

├── requirements.txt    # Dependências Python

├── Dockerfile         # Configuração Docker

├── docker-compose.yml # Configuração Docker Compose

└── README.md         # Documentação


### Dependências Principais
- FastAPI (0.104.1)
- Uvicorn (0.15.0)
- OpenAI Whisper
- PyTorch (2.1.2)
- NumPy (1.24.3)
- python-multipart (0.0.6)
- aiofiles (23.2.1)
- pydantic (2.5.3)
- pydantic-settings (2.1.0)

## 📈 Performance

- O modelo base do Whisper é usado por padrão
- Para melhor precisão em português, considere usar modelos maiores (medium/large)
- O tempo de processamento varia conforme o hardware e tamanho do áudio
- Em CPU, o modelo usa precisão FP32
- Em GPU, o modelo usa precisão FP16 para melhor performance

## ✨ Melhorias Implementadas

- [x] Implementar limite de tamanho de arquivo (25MB)
- [x] Implementar validação de tipos de arquivo
- [x] Otimizar configurações para português brasileiro
- [x] Adicionar tratamento de erros
- [x] Adicionar suporte a variáveis de ambiente
- [x] Adicionar healthcheck endpoint
- [x] Especificar versões das dependências
- [x] Otimizar configuração do Docker

## 🔜 Próximos Passos

- [ ] Implementar sistema de filas para processamento assíncrono
- [ ] Adicionar mais opções de configuração do modelo Whisper
- [ ] Implementar rate limiting
- [ ] Adicionar sistema de cache para otimização
- [ ] Implementar autenticação e autorização
- [ ] Adicionar métricas e monitoramento
- [ ] Implementar logs estruturados
- [ ] Adicionar testes automatizados