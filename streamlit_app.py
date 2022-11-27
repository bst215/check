import streamlit as st
import cv2
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from datetime import datetime
from pdf2image import convert_from_bytes, convert_from_path
import io
import os
import fitz
import easyocr

st.write("Welcome!")

m_cont = st.container()
c1, c2 = st.columns(2)
now = datetime.now()
reader = easyocr.Reader(['en'])
g = 0
m_dict = {}

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   dst_pdf = PdfWriter()
   # t_contents = PdfReader(t_file)
   img = fitz.open(stream=t_file.getvalue(), filetype="pdf")
   # num_pages = len(t_contents.pages)
   with c1:
      for page in img:
         pic = page.get_pixmap()
         st.image(pic.pil_tobytes(format="JPEG"))
         with c2:
            t_read = reader.readtext(pic.pil_tobytes(format="JPEG"))
            for t in range(len(t_read)):
               # m_dict.update({t: reader.readtext(pic.pil_tobytes(format="JPEG"))[t][1]})
               m_dict.update({g: t_read[g][1]})
               g+=1
       with c2:
         st.write(m_dict)


