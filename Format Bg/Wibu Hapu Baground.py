from rembg import remove
from PIL import Image

# Memasukkan nama file gambar input
input_file = input("Masukkan nama file gambar (misalnya 'yang ingin di hapus latar belakang.jpg' formatnya bebas kalian bisa masukan untuk di pindahkan ): ")
# Membaca gambar
image_input = Image.open(input_file)

# Menghapus latar belakang
output = remove(image_input)

# Memasukkan nama file output dan format
output_file = input("Masukkan nama file output (tanpa ekstensi, misalnya 'Nama Dari Gambar') : ")
output_format = input("Masukkan format gambar ( Masukan Format Gambar, misalnya 'png' atau 'jpg' Dan File Lainya Bebas ) : ")

# Menentukan ekstensi berdasarkan format
if output_format.lower() == "png":
    extension = ".png"
elif output_format.lower() in ["jpg", "jpeg"]:
    extension = ".jpg"
elif output_format.lower() == "bmp":
    extension = ".bmp"
elif output_format.lower() == "gif":
    extension = ".gif"
elif output_format.lower() == "webp":
    extension = ".webp"
elif output_format.lower() == "tiff":
    extension = ".tiff"
elif output_format.lower() == "ico":
    extension = ".ico"
elif output_format.lower() == "svg":
    extension = ".svg"
elif output_format.lower() == "psd":
    extension = ".psd"
elif output_format.lower() == "raw":
    extension = ".raw"
elif output_format.lower() == "tga":
    extension = ".tga"
elif output_format.lower() == "tif":
    extension = ".tif"
elif output_format.lower() == "iff":
    extension = ".iff"
elif output_format.lower() == "lbm":
    extension = ".lbm"
elif output_format.lower() == "iff":
    extension = ".iff"
elif output_format.lower() == "rle":
    extension = ".rle"
elif output_format.lower() == "pcx":
    extension = ".pcx"
elif output_format.lower() == "xbm":
    extension = ".xbm"
elif output_format.lower() == "xpm":
    extension = ".xpm"
elif output_format.lower() == "pgm":
    extension = ".pgm"
elif output_format.lower() == "ppm":
    extension = ".ppm"
elif output_format.lower() == "pbm":   
    extension = ".pbm"
else:
    print("Format tidak valid. Silakan gunakan 'png' atau 'jpg' jikalau format tersebut gagal, silakan coba lagi.")
    exit()

# Menyimpan gambar hasil
output.save(output_file + extension)
print(f"Gambar berhasil disimpan sebagai '{output_file + extension}'")