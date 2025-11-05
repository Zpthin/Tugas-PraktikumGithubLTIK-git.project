def hitung_selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    #ubah ke detik
    total_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai
    
    #hitung selisih
    selisih = total_selesai - total_mulai
    
    #ubah kembali ke jam, menit, dan detik
    jam = selisih // 3600
    sisa = selisih % 3600
    menit = sisa // 60
    detik = sisa % 60
    
    print(f"Selisih waktu: {jam} jam - {menit} menit - {detik} detik")
    
hitung_selisih_waktu(8, 10, 20, 9, 15, 30)
