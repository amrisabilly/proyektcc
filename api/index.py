from fastapi import FastAPI

app = FastAPI()

# Data contoh (Simulasi Database)
data_psikotes = [
    {"id": 1, "nama": "Bila", "kategori": "Kognitif", "harga": 150000},
    {"id": 2, "nama": "Billy", "kategori": "Kepribadian", "harga": 100000},
    {"id": 3, "nama": "Zahirah", "kategori": "Karier", "harga": 200000},
]

@app.get("/")
def read_root():
    return {"message": "API Berhasil di Hosting!"}


# Endpoint 1: Data Retrieval (Mengambil semua jenis tes)
@app.get("/tes")
def get_semua_tes():
    return {"status": "success", "data": data_psikotes}

# Endpoint 2: Searching (Mencari tes berdasarkan kategori)
@app.get("/tes/cari")
def cari_tes(kategori: str):
    hasil = [t for t in data_psikotes if kategori.lower() in t["kategori"].lower()]
    return {"keyword": kategori, "hasil": hasil}

# Endpoint 3: Komputasi (Menghitung total harga jika mengambil semua tes)
@app.get("/tes/total-biaya")
def hitung_biaya():
    total = sum(t["harga"] for t in data_psikotes)
    # Komputasi sederhana: menjumlahkan harga dari list
    return {
        "pesan": "Total biaya paket lengkap tes psikologi",
        "total_harga": f"Rp {total}"
    }