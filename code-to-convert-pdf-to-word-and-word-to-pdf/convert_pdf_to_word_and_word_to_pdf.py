# CONVERT FROM DOCX TO PDF
from docx2pdf import convert
convert("Report_hotel_booking_analysis.docx", "Report_hotel_booking_analysis.pdf")


# CONVERT FROM PDF TO DOCX
from pdf2docx import Converter

pdf_file = "Report_hotel_booking_analysis.pdf"
new_doc_file = "Report_hotel_booking_analysis.docx"

ob = Converter(pdf_file)
ob.convert(new_doc_file)
ob.close()
