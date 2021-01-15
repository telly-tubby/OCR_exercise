
import re
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread('sample.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(gray)
pattern = r"[A-Z]{5}[0-9]{4}[A-Z]"
pan_no = re.findall(pattern, text)
date_pattern = r"[0-9]{2}[/][0-9]{2}[/][0-9]{4}"
date = re.findall(date_pattern, text)

print("PAN no.: " + pan_no[0])
print("DOB: " + date[0])
cv2.waitKey(0)
