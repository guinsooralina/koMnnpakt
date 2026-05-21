from PIL import Image

# Создание изображения 300×100 с белым фоном
img = Image.new('RGB', (300, 100), color='white')

# Сохранение файла
img.save('image.png')
