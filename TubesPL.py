# Program menghitung luas dan keliling persegi panjang

def hitung_luas_panjang(lebar, panjang):
    return lebar * panjang

def hitung_keliling_panjang(lebar, panjang):
    return 2 * (lebar + panjang)

def main():
    print("Program Menghitung Luas dan Keliling Persegi Panjang")
    lebar = float(input("Masukkan lebar: "))
    panjang = float(input("Masukkan panjang: "))

    luas = hitung_luas_panjang(lebar, panjang)
    keliling = hitung_keliling_panjang(lebar, panjang)

    print(f"Luas persegi panjang adalah: {luas}")
    print(f"Keliling persegi panjang adalah: {keliling}")

if __name__ == "__main__":
    main()
