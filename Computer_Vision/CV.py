try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("test.png")

print(pytesseract.image_to_string(img))
print()
