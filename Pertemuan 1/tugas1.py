# Input: jumlah total belanja
total_belanja = float(input("Masukkan total belanja Anda: "))

# Kondisi if/else untuk mengecek apakah total lebih dari 100,000
if total_belanja > 100000:
    print("Selamat, Anda dapat hadiah!")
else:
    print("Maaf, belanja Anda belum cukup.")
