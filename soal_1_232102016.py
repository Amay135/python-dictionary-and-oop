D={"INF004": "Matematika Teknik",
    "INF005": "Fotografi",
    "INF007": "Instalasi Hardware",
    "INF008": "Sistem Operasi",
    "INF013": "Pendidikan Pancasila",
    "INF015": "Algoritma Komputer & Struktur Data"}
for i in range(5):
    key = input(f"Masukan kode mata kuliah{i+1}: ")
    val = input(f"Masukan nama mata kuliah{i+1}: ")
    D[key] = val

D["INF011"] = "Pemrograman Python"
D["INF023"] = "Bahasa Indonesia"

for key, val in D.items():
  print(f"{key} ==> {val}")