# Shopify Scraper API



https://github.com/user-attachments/assets/2d840b89-b6e9-4dd2-b64f-442d4caaa5d5

## Tecnologias Utilizadas
- **FastAPI** - Framework para construir APIs em Python
- **Jinja2** - Motor de templates para renderizar HTML
- **Aiohttp** - Para requisições assíncronas
- **Docker** - Para containerização do projeto

## Estrutura do Projeto
```
.
├── Dockerfile
├── requirements.txt
├── src
│   ├── app.py
│   ├── __init__.py
│   ├── spider.py
└── templates
    ├── index.html
    └── scrape.html
```


## Endpoints
### `GET /`
Redireciona para a página inicial.

### `GET /home`
Renderiza a página inicial (`index.html`).

### `POST /scrape`
Inicia o scraping de uma loja Shopify.
- **Parâmetros:**
  - `store_name` (str) - Nome da loja
  - `site_url` (str) - URL da loja
- **Retorno:**
  - Lista de produtos coletados com:
    - `title`
    - `editor`
    - `published_at`
    - `updated_at`
    - `price`
    - `images`






