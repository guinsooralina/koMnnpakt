from flask import Flask, send_file
from PIL import Image
import io

app = Flask(__name__)

@app.route('/image')
def get_image():
    # Создание изображения 300×100 с белым фоном
    img = Image.new('RGB', (300, 100), color='white')
    
    # Сохранение изображения в байтовый поток
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Возврат изображения
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
