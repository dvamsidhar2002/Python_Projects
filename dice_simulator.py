from venv import create
import pyqrcode

input_data = 'https://app.datacamp.com/learn/courses';

img = pyqrcode.create(input_data)

img.png('qr_code001.png',scale=10)