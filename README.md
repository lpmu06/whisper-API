# Whisper-API

API REST desenvolvida com FastAPI para transcrição de áudio para texto utilizando o modelo Whisper da OpenAI. A API é containerizada usando Docker e otimizada para transcrições em português brasileiro.

## 🚀 Funcionalidades

- Transcrição de áudio para texto usando o modelo Whisper
- Suporte para múltiplos arquivos de áudio
- Otimizado para português brasileiro
- Interface Swagger UI para testes (/docs)
- Suporte a GPU (CUDA) quando disponível

## 📋 Pré-requisitos

- Docker
- Git
- (Opcional) NVIDIA GPU com CUDA para melhor performance

## 🔧 Instalação e Execução

### 1. Clone o repositório
```bash
git clone <https://github.com/lpmu06/whisper-API>
cd whisper-api
```

### 2. Construa a imagem Docker
```bash
docker build -t whisper-api .
```

### 3. Execute o container
```bash
docker run -d -p 8000:8000 whisper-api
```

A API estará disponível em `http://localhost:8000`

## 📝 Como Usar

### Endpoint Principal

- **URL**: `/whisper`
- **Método**: `POST`
- **Content-Type**: `multipart/form-data`

### Exemplo de uso com cURL
```bash
curl -X POST "http://localhost:8000/whisper" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "files=@seu_audio.mp3"
```

### Exemplo de uso com Python
```python
import requests

url = "http://localhost:8000/whisper"
files = [
    ('files', ('audio.mp3', open('audio.mp3', 'rb'), 'audio/mpeg'))
]

response = requests.post(url, files=files)
print(response.json())
```

### Formatos de Áudio Suportados
- MP3 (.mp3)
- WAV (.wav)
- Outros formatos suportados pelo ffmpeg

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
2. Expanda o endpoint POST `/whisper`
3. Clique em "Try it out"
4. Faça upload de um arquivo de áudio
5. Execute e verifique a resposta

## ⚙️ Configuração Avançada

### Variáveis de Ambiente
- `PORT`: Porta da aplicação (default: 8000)
- Outras configurações podem ser adicionadas conforme necessidade

### Usando GPU
A API automaticamente detecta e utiliza GPU se disponível. Para usar com GPU:

1. Instale os drivers NVIDIA
2. Instale o NVIDIA Container Toolkit
3. Execute o container com suporte a GPU:
```bash
docker run --gpus all -d -p 8000:8000 whisper-api
```

## 🛠️ Desenvolvimento

### Estrutura do Projeto

whisper-api/
├── fastapi_app.py    # Aplicação principal
├── requirements.txt  # Dependências Python
├── Dockerfile       # Configuração Docker
└── README.md       # Documentação


### Dependências Principais
- FastAPI
- Uvicorn
- OpenAI Whisper
- PyTorch
- python-multipart
- aiofiles

## 📈 Performance

- O modelo base do Whisper é usado por padrão
- Para melhor precisão em português, considere usar modelos maiores (medium/large)
- O tempo de processamento varia conforme o hardware e tamanho do áudio

## ✨ Próximos Passos

- [ ] Implementar limite de tamanho de arquivo
- [ ] Implementar sistema de filas para processamento assíncrono
- [ ] Adicionar mais opções de configuração do modelo Whisper
- [ ] Implementar validação de tipos de arquivo
- [ ] Otimizar configurações para português brasileiro
- [ ] Adicionar tratamento de erros mais robusto
- [ ] Implementar rate limiting
- [ ] Adicionar suporte a variáveis de ambiente