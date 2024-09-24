# Kata sandi yang sudah ditetapkan
password_benar = "12345"

# Input: kata sandi pengguna
password_input = input("Masukkan kata sandi Anda: ")

# Kondisi if/else untuk memeriksa kata sandi
if password_input == password_benar:
    print("Selamat datang, bos!")
else:
    print("Kata sandi salah, coba lagi!")
    print("Terimakasih sudah menggunakan aplikasi kami.")
