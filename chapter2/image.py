from PIL import Image
from PIL import ImageFilter, Image

# Memuat gambar
#image = Image.open('result.jpg')

# # Mengonversi gambar ke mode RGB
# rgb_image = image.convert('RGBA')

# # Menyimpan gambar
# image.save('result.jpg')

#cropped
#cropped_image = image.crop((10, 10, 200, 200))
#cropped_image.save('cropped_result.jpg')

#resizing
#resized_image = cropped_image.resize((100, 100))
#resized_image.save('resized_result.jpg')

#filtering
#filtered_image = resized_image.filter(ImageFilter.BLUR)

# Jika gambar dalam mode RGBA, ubah menjadi RGB
# if filtered_image.mode == 'RGBA':
#     filtered_image = filtered_image.convert('RGB')
# filtered_image.save('filtered2_result.jpg')

image = Image.open('gambar.png')
# Mengubah ukuran gambar
resized_image = image.resize((100, 100))

# Menambahkan efek blur
filtered_image = resized_image.filter(ImageFilter.BLUR)

# Menyimpan gambar hasil sebagai PNG tanpa perlu mengonversi mode warna
filtered_image.save('filtered_result.png')