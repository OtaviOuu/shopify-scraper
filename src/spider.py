import aiohttp
import asyncio
import json
import aiofiles


class ShopiFyHandler:
    def __init__(self, base_url, name):
        self.base_url = base_url
        self.name = name
        self.results = []

    async def _get_product_data(self, url, session):
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                product = data["product"]

                book_data = {
                    "title": product["title"],
                    "editor": product["vendor"],
                    "published_at": product["published_at"],
                    "updated_at": product["updated_at"],
                    "price": product["variants"][0]["price"],
                    "images": product["image"]["src"],
                }
                self.results.append(book_data)
            else:
                print(f"Error: {response.status}")

    async def _get_collection(self, url, session):
        async with session.get(url) as response:
            data = await response.json()
            urls = []
            for product in data["products"]:
                product_slug = product["handle"]
                urls.append(f"{url.replace('.json', '')}/{product_slug}.json")
            tasks = [self._get_product_data(url, session) for url in urls]
            await asyncio.gather(*tasks)

    async def collect(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/collections.json") as response:
                data = await response.json()
                urls = []
                for product in data["collections"]:
                    collection_slug = product["handle"]
                    urls.append(
                        f"{self.base_url}/collections/{collection_slug}/products.json"
                    )

                tasks = [self._get_collection(url, session) for url in urls]
                await asyncio.gather(*tasks)
                return self.results

    async def save_in_disk(self, data):
        async with aiofiles.open(f"{self.name}.jsonl", mode="a") as file:
            await file.write(json.dumps(data, ensure_ascii=False) + "\n")
