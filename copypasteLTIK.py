def login():
    pw = "Latihan"
    kesempatan = 3
    
    for i in range (kesempatan):
        print("Username: Daspro2023")
        password = input("Masukkan password: ")
        
        if password == pw:
            print("Login berhasil!Selamat Datang!")
            break
        else:
            sisa = kesempatan - (i + 1)
            if sisa > 0:
                print(f"Password salah! Kesempatan tersisa {sisa}")
            else:
                print("Kesempatan habis! Anda keluar dari login")
                
login()

