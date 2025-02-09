import aiohttp
import asyncio

import json


base_url = "url"
name = "name"


async def get_product_data(url, session):
    async with session.get(url) as response:
        print(url)
        if response.status == 200:
            data = await response.json()
            book_data = {
                "title": data["product"]["title"],
                "editor": data["product"]["vendor"],
                "published_at": data["product"]["published_at"],
                "updated_at": data["product"]["updated_at"],
                "price": data["product"]["variants"][0]["price"],
                "images": data["product"]["image"]["src"],
            }
            with open(f"{name}.jsonl", "a") as f:
                f.write(json.dumps(book_data) + "\n")
        else:
            print(f"Error: {response.status}")


async def get_collection(url, session):
    async with session.get(url) as response:
        data = await response.json()
        urls = []
        for product in data["products"]:
            product_slug = product["handle"]
            urls.append(f"{url.replace('.json', '')}/{product_slug}.json")
        tasks = [get_product_data(url, session) for url in urls]
        await asyncio.gather(*tasks)


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{base_url}/collections.json") as response:
            data = await response.json()
            urls = []
            for product in data["collections"]:
                collection_slug = product["handle"]
                urls.append(f"{base_url}/collections/{collection_slug}/products.json")

            tasks = [get_collection(url, session) for url in urls]
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
