# Shopify Scraper API



![github](https://github.com/user-attachments/assets/d1aa3a3b-b569-4ec9-92fe-6e969c8efe64)
![image](https://github.com/user-attachments/assets/605a3b0c-39c5-43f8-b1d7-523a3174359b)


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






