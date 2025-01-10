import barcode
from barcode.writer import ImageWriter
from PIL import Image
import win32print
import win32ui
import os

def generate_barcode(data, filename):
    # Generate barcode
    code128 = barcode.get('code128', data, writer=ImageWriter())
    code128.save(filename)


if __name__ == "__main__":
    print('Vul hier de tekst van de barcode in:')
    data = input()  # Replace with your data
    filename = "barcode - " + data  # Filename without extension

    generate_barcode(data, filename)
    os.system(r"move-barcodes.bat")
