import pytesseract
from PIL import Image
img = Image.open("funtern-handwrite.JPG")
# converts the image to result and saves it into result variable
result = pytesseract.image_to_string(img)

print(result)