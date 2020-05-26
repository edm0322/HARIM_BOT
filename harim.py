# -*- coding: utf-8 -*-

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import HTMLConverter, TextConverter
# from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO, BytesIO

def convert_pdf_to_text():
   path = "판교05월03주(7).pdf"
   rsrcmgr = PDFResourceManager() #PDF 처리 Manager 객체 생성
   retstr = StringIO() #문자열데이터를 파일처럼 처리하도록. StringIO -> PDF
   HTML_retstr = BytesIO()
   codec = "utf-8"
   laparams = LAParams()
   #device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
   device = HTMLConverter(rsrcmgr, HTML_retstr)
   fp = open(path, 'rb')
   interpreter = PDFPageInterpreter(rsrcmgr, device)
   password = ""
   maxpages = 0
   caching = True
   pagenos = set()

   for page in PDFPage.get_pages(fp):
      interpreter.process_page(page)
   text = HTML_retstr.getvalue()

   fp.close()
   device.close()
   retstr.close()
   return text

v = convert_pdf_to_text()
print(v)