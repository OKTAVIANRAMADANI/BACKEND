def hitung_gaji(nama, golongan, jam_kerja):
    upah = {
        'A': 5000,
        'B': 7000,
        'C': 8000,
        'D': 10000
    }
    
    if golongan in upah:
        upah_dasar = upah[golongan]
    else:
        return "Golongan tidak valid"
    
    gaji = jam_kerja * upah_dasar
   
    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        uang_lembur = jam_lembur * 4000
        total_gaji = gaji + uang_lembur
    else:
        total_gaji = gaji
    
    print("Nama Karyawan: ", nama)
    print("Golongan: ",golongan)
    print("Jumlah jam kerja: ",jam_kerja)
    print("Karyawan Menerima Upah Rp.  per minggu ",total_gaji)
    
hitung_gaji("Fikri", 'A', 100)