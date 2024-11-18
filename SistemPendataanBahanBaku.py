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

    def login_page(self):
        for widget in self.apk.winfo_children():
            widget.destroy()
        
        gambar = Image.open("Bahan Baku.jpeg") 
        gambar = gambar.resize((700,128)) 
        gambar = gambar.filter(ImageFilter.GaussianBlur(2))
        self.photo = ImageTk.PhotoImage(gambar)  
        label_image = tk.Label(self.apk, image = self.photo) 
        label_image.place(x=0, y=0) 
        label_image.lower() 

        
        label1 = tk.Label(self.apk, text="LOGIN PAGE",font=("Helvetica",20),bg=self.bg_color) 
        label1.place(x=270, y=175) 
        
        self.entry_nama = tk.Entry(self.apk, font=self.font_stlye)
        self.entry_nama.place(x=248, y=272) 
        self.entry_password = tk.Entry(self.apk, show="*", font=self.font_stlye)
        self.entry_password.place(x=248, y=337) 
       
        label_nama = tk.Label(self.apk , text= "Name" , font=self.font_stlye, bg=self.bg_color) 
        label_nama.place(x=248,y=244) 
        label_password = tk.Label(self.apk, text="Password", font=self.font_stlye, bg=self.bg_color) 
        label_password.place(x=248,y=305) 
        
        Submit= tk.Button(self.apk, text="Login",font=self.font_stlye, command=self.validate_login) 
        Submit.place(x=496,y=474) 

    def validate_login(self):
        nama = self.entry_nama.get()
        password = self.entry_password.get()
        if nama == "1" and password == "1":
            self.dashboard()
        else:
            messagebox.showerror("Login Failed", "Incorrect username or password")

    def dashboard(self):
        for widget in self.apk.winfo_children():
            widget.destroy()

        gambar = Image.open("Bahan Baku.jpeg") 
        gambar = gambar.resize((700,128)) 
        gambar = gambar.filter(ImageFilter.GaussianBlur(2))
        self.photo = ImageTk.PhotoImage(gambar)  
        label_image = tk.Label(self.apk, image = self.photo) 
        label_image.place(x=0, y=0) 
        label_image.lower()

        self.apk.configure(bg=self.bg_color)
        label2 = tk.Label(apk, text="SELAMAT BEKERJA",font=("Helvetica", 20),bg=self.bg_color)
        label2.place(x=210, y=164)
        label3 = tk.Label(apk, text="Jangan Lupa Tersenyum",font=("Helvetica", 10),bg=self.bg_color)
        label3.place(x=260, y=195)

        # Tombol
        tambahbahan_button = tk.Button(self.apk, text="Tambah Bahan Baku", font=self.font_stlye, command=self.tambah_bahan_page)
        tambahbahan_button.place(x=20, y=250)
        tambahmenu_button = tk.Button(self.apk, text="Tambah Menu", font=self.font_stlye, command=self.tambah_menu_page)
        tambahmenu_button.place(x=220, y=250)
        masak_button = tk.Button(self.apk, text="Masak Menu", font=self.font_stlye, command=self.masak_menu_page)
        masak_button.place(x=370, y=250)
        logout_button = tk.Button(self.apk, text="Logout", font=self.font_stlye, command=self.logout)
        logout_button.place(x=700, y=20)

        # Inisialisasi Treeview untuk menampilkan Tabel bahan baku
        tk.Label(self.apk, text="Data Bahan Baku", font=("Helvetica", 16), bg="#C9A66B").place(x=20, y=300)
        self.bahan_tree = ttk.Treeview(self.apk, columns=("Nama Bahan", "Stok"), show="headings", height=8)
        self.bahan_tree.heading("Nama Bahan", text="Nama Bahan")
        self.bahan_tree.heading("Stok", text="Stok")
        self.bahan_tree.column("Nama Bahan", anchor="center", width=150)
        self.bahan_tree.column("Stok", anchor="center", width=100)
        self.bahan_tree.place(x=20, y=330)

        # Inisialisasi Treeview untuk Tabel menu
        tk.Label(self.apk, text="Data Menu", font=("Helvetica", 16), bg="#C9A66B").place(x=320, y=300)
        self.menu_tree = ttk.Treeview(self.apk, columns=("Nama Menu", "Bahan Baku"), show="headings", height=8)
        self.menu_tree.heading("Nama Menu", text="Nama Menu")
        self.menu_tree.heading("Bahan Baku", text="Bahan Baku")
        self.menu_tree.column("Nama Menu", anchor="center", width=150)
        self.menu_tree.column("Bahan Baku", anchor="center", width=200)
        self.menu_tree.place(x=320, y=330)

    def update_tables(self):
        """Perbarui data tabel bahan baku dan menu"""
        # Tabel bahan baku
        for item in self.bahan_tree.get_children():
            self.bahan_tree.delete(item)
        for nama, stok in self.bahan_baku.items():
            self.bahan_tree.insert("", "end", values=(nama, stok))
            if stok <= 1:  # Peringatan stok rendah
                messagebox.showwarning("Stok Sedikit", f"Stok bahan baku {nama} hampir habis! ({stok})")

        # Tabel menu
        for item in self.menu_tree.get_children():
            self.menu_tree.delete(item)
        for nama_menu, bahan in self.menu.items():
            bahan_str = ", ".join([f"{k}({v})" for k, v in bahan.items()])
            self.menu_tree.insert("", "end", values=(nama_menu, bahan_str))

    def tambah_bahan_page(self):
        """Halaman tambah bahan baku"""
        self.popup = tk.Toplevel(self.apk)
        self.popup.title("Tambah Bahan Baku")
        self.popup.geometry("400x300")

        tk.Label(self.popup, text="Nama Bahan", font=("Helvetica", 14)).place(x=50, y=50)
        self.entry_bahan_nama = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_bahan_nama.place(x=180, y=50)

        tk.Label(self.popup, text="Stok", font=("Helvetica", 14)).place(x=50, y=100)
        self.entry_bahan_stok = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_bahan_stok.place(x=180, y=100)

        tk.Button(self.popup, text="Simpan", font=("Helvetica", 14), command=self.simpan_bahan).place(x=150, y=200)

    def simpan_bahan(self):
        """Simpan bahan baku ke database"""
        nama = self.entry_bahan_nama.get()
        try:
            stok = int(self.entry_bahan_stok.get())  # Konversi stok menjadi angka
            if stok < 0:
                raise ValueError("Stok tidak boleh negatif!")
            if nama in self.bahan_baku:
                self.bahan_baku[nama] += stok  # Tambahkan ke stok yang sudah ada
            else:
                self.bahan_baku[nama] = stok  # Tambahkan bahan baru
            self.update_tables()
            self.popup.destroy()
        except ValueError:
            messagebox.showerror("Error", "Stok harus berupa angka positif!")

    def tambah_menu_page(self):
        """Halaman tambah menu"""
        self.popup = tk.Toplevel(self.apk)
        self.popup.title("Tambah Menu")
        self.popup.geometry("400x400")

        tk.Label(self.popup, text="Nama Menu", font=("Helvetica", 14)).place(x=50, y=50)
        self.entry_menu_nama = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_menu_nama.place(x=180, y=50)

        tk.Label(self.popup, text="Bahan (format: nama1,jumlah1;nama2,jumlah2)", font=("Helvetica", 10)).place(x=50, y=100)
        self.entry_menu_bahan = tk.Entry(self.popup, font=("Helvetica", 14), width=30)
        self.entry_menu_bahan.place(x=50, y=140)

        tk.Button(self.popup, text="Simpan", font=("Helvetica", 14), command=self.simpan_menu).place(x=150, y=200)

    def simpan_menu(self):
        """Simpan menu ke database"""
        nama = self.entry_menu_nama.get()
        bahan_input = self.entry_menu_bahan.get()
        try:
            bahan = {}
            for item in bahan_input.split(";"):
                nama_bahan, jumlah = item.split(",")
                bahan[nama_bahan.strip()] = int(jumlah.strip())  # Pastikan jumlah berbentuk angka
            self.menu[nama] = bahan
            self.update_tables()
            self.popup.destroy()
        except ValueError:
            messagebox.showerror("Error", "Jumlah bahan harus berupa angka!")
        except Exception as e:
            messagebox.showerror("Error", f"Format bahan salah!\n{e}")


    def masak_menu_page(self):
        """Halaman masak menu"""
        self.popup = tk.Toplevel(self.apk)
        self.popup.title("Masak Menu")
        self.popup.geometry("400x300")

        tk.Label(self.popup, text="Nama Menu", font=("Helvetica", 14)).place(x=50, y=50)
        self.entry_masak_menu = tk.Entry(self.popup, font=("Helvetica", 14))
        self.entry_masak_menu.place(x=180, y=50)

        tk.Button(self.popup, text="Masak", font=("Helvetica", 14), command=self.masak_menu).place(x=150, y=150)

    def masak_menu(self):
        """Kurangi stok bahan baku sesuai menu"""
        nama_menu = self.entry_masak_menu.get()
        if nama_menu in self.menu:
            bahan_menu = self.menu[nama_menu]
            try:
                for bahan, jumlah in bahan_menu.items():
                    if self.bahan_baku.get(bahan, 0) < jumlah:
                        raise ValueError(f"Bahan {bahan} tidak mencukupi!")
                for bahan, jumlah in bahan_menu.items():
                    self.bahan_baku[bahan] -= jumlah  # Pastikan pengurangan dilakukan pada angka
                messagebox.showinfo("Success", f"Menu {nama_menu} berhasil dimasak!")
                self.update_tables()
                self.popup.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Menu tidak ditemukan!")

    def logout(self):
        self.login_page()

if __name__ == "__main__": 
    apk = tk.Tk() 
    app = MainApp(apk) 
    apk.geometry("700x550")
    apk.configure(bg='#C9A66B') 
    apk.resizable(False, False) 
    apk.mainloop() 