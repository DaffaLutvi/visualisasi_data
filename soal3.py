import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Penghasilan_Per_Bulan": [250000, 5000000, 8000000, 15000000, 7000000, 12000000]
})

def kategori_penghasilan(penghasilan):
    if penghasilan < 3_000_000:
        return "Sangat Rendah"
    elif penghasilan < 7_000_000:
        return "Rendah"
    elif penghasilan < 12_000_000:
        return "Menengah"
    else:
        return "Tinggi"

df = df.dropna(subset=["Penghasilan_Per_Bulan"])

df["Kategori_Penghasilan"] = df["Penghasilan_Per_Bulan"].apply(kategori_penghasilan)

kategori_counts = df["Kategori_Penghasilan"].value_counts().sort_index()

plt.figure(figsize=(8, 8))
plt.pie(
    kategori_counts,
    labels=kategori_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=['#ff9999', '#66b3ff','#99ff99','#ffcc99']
)
plt.title('Distribusi Kategori Penghasilan Warga')
plt.axis('equal')
plt.tight_layout()
plt.show()