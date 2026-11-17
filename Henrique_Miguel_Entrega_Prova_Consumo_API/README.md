# API Meteorológica Offline

API REST desenvolvida por Henrique Miguel com **Python e FastAPI**.

## Tecnologias fornecidas

- Python
- FastAPI
- Uvicorn
- JSON
- Requests (para aplicações consumidoras)

## Estrutura que foi feita no projeto
```text
api-meteorologica-offline/
├── Henrique_Miguel_Entrega_Prova_Consumo_API/
│   ├── .venv/
│   ├── __pycache__/
│   │   ├── consumidor_api.cpython-314.pyc
│   ├── consumidor_api.py
│   ├── frontend.py
│   ├── .gitignore
│   └── README.md
```

## Instalação

### Clonar o repositório

```text
git clone https://github.com/jpsvalentim/api-meteorologica-offline.git
```

Acessar a pasta:

```text
abri o repositório clonado (api-meteorologica-offline)
```

### Criar ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
```

Ativar o ambiente:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Instalar dependências

```bash
pip install -r requirements.txt
```

## Executar a API

Com o ambiente virtual em utilização, digite o comando:

```bash
uvicorn app.main:app --reload
```

A API rodará em:

```text
http://127.0.0.1:8000
```

## Consulta das informações da API

O endpoint `/v1/forecast` disponibiliza as informações necessárias.

### Parâmetros

| Parâmetro | Tipo | Descrição |
|---|---|---|
| latitude | float | Latitude da localidade |
| longitude | float | Longitude da localidade |
| current | string | Variáveis meteorológicas atuais desejadas |

Localidade disponível:

- Latitude: `-26.4851`
- Longitude: `-49.0713`

### Variáveis utilizadas

- `temperature_2m`
- `relative_humidity_2m`
- `apparent_temperature`
- `precipitation`
- `wind_speed_10m`