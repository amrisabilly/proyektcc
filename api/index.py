from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Data Produk Coffee Shop Lengkap dengan Image URL
products = [
    {
        "category_id": 1,
        "name": "Espresso",
        "description": "Kopi hitam pekat dengan rasa yang kuat.",
        "price": 18000,
        "image_url": "https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=800&q=80"
    },
    {
        "category_id": 2,
        "name": "Cappuccino",
        "description": "Perpaduan espresso, susu panas, dan busa susu.",
        "price": 24000,
        "image_url": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?auto=format&fit=crop&w=800&q=80"
    },
    {
        "category_id": 1,
        "name": "Caffè Latte",
        "description": "Espresso dengan susu yang lembut (steamed milk).",
        "price": 26000,
        "image_url": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80"
    },
    {
        "category_id": 2,
        "name": "Americano",
        "description": "Espresso yang ditambahkan air panas.",
        "price": 20000,
        "image_url": "https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=800&q=80"
    },
    {
        "category_id": 1,
        "name": "Iced Coffee",
        "description": "Kopi dingin menyegarkan dengan es batu.",
        "price": 22000,
        "image_url": "https://images.unsplash.com/photo-1559496417-e7f25cb247f3?auto=format&fit=crop&w=800&q=80"
    }
]

@app.get("/menu")
def get_all_menu():
    return {"status": "success", "data": products}

@app.get("/menu/search")
def search_coffee(name: Optional[str] = None):
    if name:
        hasil_cari = [p for p in products if name.lower() in p["name"].lower()]
        return {"keyword": name, "results": hasil_cari}
    return {"message": "Silakan masukkan parameter nama."}

@app.get("/menu/stats")
def get_coffee_stats():
    prices = [p["price"] for p in products]
    return {
        "total_harga": sum(prices),
        "rata_rata": sum(prices) / len(prices) if prices else 0,
        "jumlah_menu": len(products)
    }