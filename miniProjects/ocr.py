from PIL import Image
import pytesseract


image_path = "image.png"
image = Image.open(image_path)


text = pytesseract.image_to_string(image)


txt_path = "ocr.txt"
with open(txt_path, 'w') as file:
    file.write(text)

txt_path