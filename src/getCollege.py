import os
import re
import PyPDF2

def getCollege(path, code):
  pdfFileObj = open(path, 'rb') 
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  pages = list()

  for pageNO in range(pdfReader.getNumPages()):
    pageObj = pdfReader.getPage(pageNO) 
    revInfo = pageObj.extractText()[123:135]
    if code in revInfo:
      print(revInfo)
      pages.append(int(pageNO)+1)
  pdfFileObj.close() 
  return pages