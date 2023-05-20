# FROM PDF TO IMAGE CONVERTER
from pdf2image import convert_from_path

temp_img = convert_from_path("Report_hotel_booking_analysis.pdf", poppler_path=r"C:\Users\DELL\PycharmProjects\pythonProject\PythonProjects\poppler-23.01.0\Library\bin")

for img in range(len(temp_img)):
    temp_img[img].save("image" + str(img) + ".jpg","JPEG")