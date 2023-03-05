from PIL import Image, ImageChops

# membaca gambar pertama
img1 = Image.open('gambar1.jpg')

# membaca gambar kedua
img2 = Image.open('gambar2.jpg')

# menghitung perbedaan antara dua gambar
diff = Image.eval(ImageChops.difference(img1, img2), lambda x: 255 if x != 0 else 0)

# menyimpan difference image sebagai file baru
diff.save('difference_image.jpg')

# menampilkan gambar pertama, gambar kedua, dan difference image
img1.show()
img2.show()
diff.show()
