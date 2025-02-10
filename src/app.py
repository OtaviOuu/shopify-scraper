from typing import Union
from spider import ShopiFyHandler
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

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
