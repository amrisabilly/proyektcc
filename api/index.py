from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Data Produk Coffee Shop kamu
products = [
    {
        "category_id": 1,
        "name": "Espresso",
        "description": "Kopi hitam pekat dengan rasa yang kuat.",
        "price": 18000
    },
    {
        "category_id": 2,
        "name": "Cappuccino",
        "description": "Perpaduan espresso, susu panas, dan busa susu.",
        "price": 24000
    },
    {
        "category_id": 1,
        "name": "Caffè Latte",
        "description": "Espresso dengan susu yang lembut (steamed milk).",
        "price": 26000
    },
    {
        "category_id": 2,
        "name": "Americano",
        "description": "Espresso yang ditambahkan air panas.",
        "price": 20000
    },
    {
        "category_id": 1,
        "name": "Mocha",
        "description": "Kopi dengan campuran coklat dan susu.",
        "price": 25000
    }
    # ... tambahkan data lainnya sesuai keinginanmu ...
]

# 1. LAYANAN: DATA RETRIEVAL
# Mengambil seluruh daftar menu kopi
@app.get("/menu")
def get_all_menu():
    return {
        "status": "success",
        "total_items": len(products),
        "data": products
    }

# 2. LAYANAN: SEARCHING
# Mencari menu berdasarkan nama (Contoh: /menu/search?name=Latte)
@app.get("/menu/search")
def search_coffee(name: Optional[str] = None):
    if name:
        hasil_cari = [p for p in products if name.lower() in p["name"].lower()]
        return {"keyword": name, "found": len(hasil_cari), "results": hasil_cari}
    return {"message": "Silakan masukkan parameter nama untuk mencari."}

# 3. LAYANAN: KOMPUTASI SEDERHANA
# Menghitung statistik harga (Total, Rata-rata, dan Produk Termahal)
@app.get("/menu/stats")
def get_coffee_stats():
    prices = [p["price"] for p in products]
    total_harga = sum(prices)
    rata_rata = total_harga / len(prices) if prices else 0
    termahal = max(prices) if prices else 0
    
    return {
        "summary": "Statistik Menu Kopi",
        "total_harga_semua_menu": f"Rp {total_harga:,}",
        "rata_rata_harga": f"Rp {rata_rata:,.2f}",
        "harga_termahal": f"Rp {termahal:,}"
    }