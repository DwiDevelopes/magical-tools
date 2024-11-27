from ascii_magic import AsciiArt
from PIL import Image, ImageDraw, ImageFont

def tampilkan_gambar(nama_file):
    try:
        gambar = AsciiArt.from_image(nama_file)
        gambar.to_terminal()
        return gambar  # Kembalikan objek gambar untuk disimpan
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan. Silakan coba lagi.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def simpan_gambar(gambar, nama_file_simpan):
    try:
        # Mengambil representasi ASCII dari gambar
        ascii_art = gambar.to_ascii()
        lines = ascii_art.splitlines()
        
        # Ukuran gambar berdasarkan jumlah karakter
        width = max(len(line) for line in lines)
        height = len(lines)

        # Buat gambar baru dengan latar belakang putih
        img = Image.new('RGB', (width * 10, height * 20), color='white')  # Mengatur ukuran gambar
        draw = ImageDraw.Draw(img)

        # Menggunakan font default
        font = ImageFont.load_default()

        # Menggambar teks ASCII ke dalam gambar
        for y, line in enumerate(lines):
            draw.text((0, y * 20), line, fill='black', font=font)  # Menggambar setiap baris

        # Simpan gambar ke dalam format yang diinginkan
        img.save(nama_file_simpan)
        print(f"Gambar berhasil disimpan sebagai '{nama_file_simpan}'.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan gambar: {e}")

def main():
    while True:
        print("Masukkan nama file gambar (atau ketik 'keluar' untuk mengakhiri):")
        nama_file = input("Nama file: ")

        if nama_file.lower() == 'keluar':
            print("Keluar dari program.")
            break

        gambar = tampilkan_gambar(nama_file)

        if gambar:
            # Tanyakan kepada pengguna apakah mereka ingin menyimpan gambar
            simpan = input("Apakah Anda ingin menyimpan gambar ASCII ini? (ya/tidak): ").strip().lower()
            if simpan == 'ya':
                nama_file_simpan = input("Masukkan nama file untuk menyimpan (misalnya: gambar.png): ")
                simpan_gambar(gambar, nama_file_simpan)

if __name__ == "__main__":
    main()