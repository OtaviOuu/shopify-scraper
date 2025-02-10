from spider import ShopiFyHandler
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/scrape")
async def scrape_website(
    request: Request, store_name: str = Form(...), site_url: str = Form(...)
):
    shopify = ShopiFyHandler(site_url, store_name)

    products = await shopify.collect()

    return templates.TemplateResponse(
        "scrape.html",
        {"request": request, "products": products, "store_name": store_name},
    )


@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return RedirectResponse(url="/home")
    raise exc  # Se for outro erro, mantém o comportamento normal
