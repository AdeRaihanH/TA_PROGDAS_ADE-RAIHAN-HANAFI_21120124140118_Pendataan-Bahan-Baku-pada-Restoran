import tkinter as tk 
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox, ttk
 
class MainApp: 
    def __init__(self, apk): 
        self.apk = apk
        self.font_stlye= ("Helvetica",14) 
        self.bg_color= '#C9A66B'
        self.apk.title("Pendataan Bahan Baku") 
        self.bahan_baku = {}  
        self.menu = {}
        self.login_page()

    # Membuat page login
    def login_page(self):
        for widget in self.apk.winfo_children():
            widget.destroy()
        
        # Memberikan gambar pada header
        gambar = Image.open("Bahan Baku.jpeg") 
        gambar = gambar.resize((700,128)) 
        gambar = gambar.filter(ImageFilter.GaussianBlur(2))
        self.photo = ImageTk.PhotoImage(gambar)  
        label_image = tk.Label(self.apk, image = self.photo) 
        label_image.place(x=0, y=0) 
        label_image.lower() 

        # Memberi output tulisan
        label1 = tk.Label(self.apk, text="LOGIN PAGE",font=("Helvetica",20),bg=self.bg_color) 
        label1.place(x=270, y=175) 
        
        # Membuat close button
        close_button = tk.Button(self.apk, text="Close", font=self.font_stlye, bg="#261F12", fg="#8E7448", command=self.close_program)
        close_button.place(x=160, y=474)

        # Membuat label nama 
        label_nama = tk.Label(self.apk , text= "Name" , font=self.font_stlye, bg=self.bg_color) 
        label_nama.place(x=248,y=244) 
        self.entry_nama = tk.Entry(self.apk, font=self.font_stlye)
        self.entry_nama.place(x=248, y=272)

        # Membuat label password 
        label_password = tk.Label(self.apk, text="Password", font=self.font_stlye, bg=self.bg_color) 
        label_password.place(x=248,y=305)
        self.entry_password = tk.Entry(self.apk, show="*", font=self.font_stlye)
        self.entry_password.place(x=248, y=337)
        
        # Membuat submit button
        Submit= tk.Button(self.apk, text="Login",font=self.font_stlye, bg="#261F12", fg="#8E7448", command=self.validate_login) 
        Submit.place(x=496,y=474) 

    # Agar yang dapat login khusus pegawai
    def validate_login(self):
        username = self.entry_nama.get()
        password = self.entry_password.get()
        if username == "pekerja" and password == "123":
            self.dashboard()
        else:
            messagebox.showerror("Error", "Username atau password salah!")


    # Membuat page baru(Dashboard)
    def dashboard(self):
        for widget in self.apk.winfo_children():
            widget.destroy()

        # Menambahkan gambar
        gambar = Image.open("Bahan Baku.jpeg") 
        gambar = gambar.resize((700,128)) 
        gambar = gambar.filter(ImageFilter.GaussianBlur(2))
        self.photo = ImageTk.PhotoImage(gambar)  
        label_image = tk.Label(self.apk, image = self.photo) 
        label_image.place(x=0, y=0) 
        label_image.lower()

        gambar1 = Image.open("backgroundcoklat.png")
        gambar1 = gambar1.resize((700,128))
        self.photo1 = ImageTk.PhotoImage(gambar1)  
        label_image1 = tk.Label(self.apk, image = self.photo1)
        label_image1.place(x=0, y=37) 
        label_image1.lower()

        # Memberi output tulisan
        self.apk.configure(bg=self.bg_color)
        label2 = tk.Label(apk, text="SELAMAT BEKERJA",font=("Helvetica", 20),bg=self.bg_color)
        label2.place(x=210, y=200)
        label3 = tk.Label(apk, text="Jangan Lupa Tersenyum",font=("Helvetica", 10),bg=self.bg_color)
        label3.place(x=265, y=230)

        # Membuat tombol
        tambahbahan_button = tk.Button(self.apk, text="Tambah Bahan Baku", font=self.font_stlye, bg="#261F12", fg="#8E7448", command=self.tambah_bahan_page)
        tambahbahan_button.place(x=185, y=130)
        tambahmenu_button = tk.Button(self.apk, text="Tambah Menu", font=self.font_stlye, bg="#261F12", fg="#8E7448", command=self.tambah_menu_page)
        tambahmenu_button.place(x=375, y=130)
        masak_button = tk.Button(self.apk, text="Masak Menu", font=self.font_stlye, bg="#261F12", fg="#8E7448", command=self.masak_menu_page)
        masak_button.place(x=505, y=130)
        logout_button = tk.Button(self.apk, text="Logout", font=self.font_stlye, bg="#261F12", fg="#8E7448", command=self.logout)
        logout_button.place(x=625, y=130)
        close_button = tk.Button(self.apk, text="Close", font=self.font_stlye, bg="#261F12", fg="#8E7448", command=self.close_program)
        close_button.place(x=20, y=500)
        
        # Inisialisasi Treeview untuk menampilkan Tabel bahan baku
        tk.Label(self.apk, text="Data Bahan Baku", font=("Helvetica", 16), bg=self.bg_color).place(x=20, y=270)
        self.bahan_tree = ttk.Treeview(self.apk, columns=("Nama Bahan", "Stok"), show="headings", height=8)
        self.bahan_tree.heading("Nama Bahan", text="Nama Bahan")
        self.bahan_tree.heading("Stok", text="Stok")
        self.bahan_tree.column("Nama Bahan", anchor="center", width=150)
        self.bahan_tree.column("Stok", anchor="center", width=100)
        self.bahan_tree.place(x=20, y=300)

        # Inisialisasi Treeview untuk Tabel menu
        tk.Label(self.apk, text="Data Menu", font=("Helvetica", 16), bg=self.bg_color).place(x=320, y=270)
        self.menu_tree = ttk.Treeview(self.apk, columns=("Nama Menu", "Bahan Baku"), show="headings", height=8)
        self.menu_tree.heading("Nama Menu", text="Nama Menu")
        self.menu_tree.heading("Bahan Baku", text="Bahan Baku")
        self.menu_tree.column("Nama Menu", anchor="center", width=150)
        self.menu_tree.column("Bahan Baku", anchor="center", width=200)
        self.menu_tree.place(x=320, y=300)

    # Membuat fungsi agar table auto update
    def update_tables(self):
        # Tabel bahan baku
        for item in self.bahan_tree.get_children():
            self.bahan_tree.delete(item)
        for nama, stok in self.bahan_baku.items():
            self.bahan_tree.insert("", "end", values=(nama, stok))
            if stok <= 1:  # Peringatan stok sedikit
                messagebox.showwarning("Stok Sedikit", f"Stok bahan baku {nama} hampir habis! ({stok})") #Peringatan jika stok sedikit

        # Tabel menu
        for item in self.menu_tree.get_children():
            self.menu_tree.delete(item)
        for nama_menu, bahan in self.menu.items():
            bahan_str = ", ".join([f"{k}({v})" for k, v in bahan.items()]) #k=nama bahan, v= jumlah yang diperlukan
            self.menu_tree.insert("", "end", values=(nama_menu, bahan_str))

    # Membuat halaman untuk menambah bahan baku
    def tambah_bahan_page(self):
        self.popup = tk.Toplevel(self.apk)
        self.popup.title("Tambah Bahan Baku")
        self.popup.geometry("400x300")

        # Membuat label untuk nama bahan
        tk.Label(self.popup, text="Nama Bahan", font=("Helvetica", 14)).place(x=50, y=50)
        self.entry_bahan_nama = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_bahan_nama.place(x=180, y=50)

        # Membuat label untuk jumlah stok
        tk.Label(self.popup, text="Stok", font=("Helvetica", 14)).place(x=50, y=100)
        self.entry_bahan_stok = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_bahan_stok.place(x=180, y=100)

        # Membuat button simpan
        tk.Button(self.popup, text="Simpan", font=("Helvetica", 14), command=self.simpan_bahan).place(x=150, y=200)

    # Fungsi untuk menyimpan bahan ke database
    def simpan_bahan(self):
        nama = self.entry_bahan_nama.get().strip().lower()
        try:
            stok = int(self.entry_bahan_stok.get())  # Agar stok yang dimasukan harus berbentuk angka
            if stok < 0:
                raise ValueError
            if nama in self.bahan_baku:
                self.bahan_baku[nama] += stok  # Menambahkan ke stok jika sudah ada stok bahan sebelumnya
            else:
                self.bahan_baku[nama] = stok  # Menambahkan bahan baku baru
            self.update_tables()
            self.popup.destroy()
        except ValueError:
            messagebox.showerror("Error", "Stok harus berupa angka dan merupakan bilangan positif!")

    # Membuat halaman untuk menambah menu
    def tambah_menu_page(self):
        self.popup = tk.Toplevel(self.apk)
        self.popup.title("Tambah Menu")
        self.popup.geometry("400x400")

        # Membuat label untuk nama menu
        tk.Label(self.popup, text="Nama Menu", font=("Helvetica", 14)).place(x=50, y=50)
        self.entry_menu_nama = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_menu_nama.place(x=180, y=50)

        # Membuat label untuk nama bahan dan jumlah yang dibutuhkan
        tk.Label(self.popup, text="Bahan (format: nama1,jumlah1;nama2,jumlah2)", font=("Helvetica", 10)).place(x=50, y=100)
        self.entry_menu_bahan = tk.Entry(self.popup, font=("Helvetica", 14), width=30)
        self.entry_menu_bahan.place(x=50, y=140)

        # Membuat button simpan
        tk.Button(self.popup, text="Simpan", font=("Helvetica", 14), command=self.simpan_menu).place(x=150, y=200)

    # Fungsi untuk menyimpan menu ke database
    def simpan_menu(self):
        nama = self.entry_menu_nama.get().strip().lower()
        bahan_input = self.entry_menu_bahan.get()
        try:
            bahan = {}
            for item in bahan_input.split(";"):     #Sebagai pemisah antar bahan baku
                nama_bahan, jumlah = item.split(",")    #Sebagai pemisah nama bahan baku dan jumlah
                bahan[nama_bahan.strip()] = int(jumlah.strip())    # Pastikan jumlah berbentuk angka
            self.menu[nama] = bahan
            self.update_tables()
            self.popup.destroy()
        except ValueError:
            messagebox.showerror("Error", "Jumlah bahan harus berupa angka dan sesuai dengan format!")

    # Membuat halaman untuk memasak menu
    def masak_menu_page(self):
        self.popup = tk.Toplevel(self.apk)
        self.popup.title("Masak Menu")
        self.popup.geometry("400x300")

        # Membuat label untuk memasukkan nama menu yang sudah terdaftar
        tk.Label(self.popup, text="Nama Menu", font=("Helvetica", 14)).place(x=50, y=50)
        self.entry_masak_menu = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_masak_menu.place(x=180, y=50)

        # Membuat button masak
        tk.Button(self.popup, text="Masak", font=("Helvetica", 14), command=self.masak_menu).place(x=150, y=150)

    # Fungsi agar mengurangi otomatis bahan jika ada menu yang dimasak
    def masak_menu(self):
        nama_menu = self.entry_masak_menu.get().strip().lower()
        if nama_menu in self.menu:
            bahan_menu = self.menu[nama_menu]
            try:
                # Cek bahan satu per satu untuk memastikan cukup
                for bahan, jumlah in bahan_menu.items():
                    # Pastikan bahan ada dalam bahan baku, jika tidak ada, anggap 0
                    bahan_tersedia = self.bahan_baku.get(bahan, 0)
                    if bahan_tersedia < jumlah:
                        raise ValueError(f"Bahan {bahan} tidak mencukupi! Tersedia {bahan_tersedia}, dibutuhkan {jumlah}.")
                
                # Jika semua bahan cukup, lakukan pengurangan
                for bahan, jumlah in bahan_menu.items():
                    self.bahan_baku[bahan] -= jumlah  # Pengurangan bahan baku
                messagebox.showinfo("Success", f"Menu {nama_menu} berhasil dimasak!")
                self.update_tables()
                self.popup.destroy()
            except ValueError as e:
                # Menampilkan pesan error spesifik untuk bahan tidak mencukupi
                messagebox.showerror("Error", str(e))  # Menampilkan pesan kesalahan yang lebih spesifik
        else:
            messagebox.showerror("Error", "Menu tidak ditemukan!")


    # Fungsi agar ketika logout kembali ke homepage
    def logout(self):
        self.login_page()
    
    # Fungsi agar ketika button close di klik program berakhir
    def close_program(self):
        result = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin keluar?") # Mengonfirmasi ke pengguna
        if result:  
            self.apk.destroy()

if __name__ == "__main__": 
    apk = tk.Tk() 
    app = MainApp(apk) 
    apk.geometry("700x550")
    apk.configure(bg='#C9A66B') 
    apk.resizable(False, False) 
    apk.mainloop() 
