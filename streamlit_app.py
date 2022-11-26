import streamlit as st
import cv2
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from datetime import datetime
import io
import os

st.write("Welcome!")

m_cont = st.container()
now = datetime.now()

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   dst_pdf = PdfWriter()
   t_contents = PdfReader(t_file)
   num_pages = len(t_contents.pages)
   if (num_pages > 0):
      page_one = t_contents.pages[0]
      page_one_text = page_one.extract_text()
      with m_cont:
         st.write("Number of pages in the .PDF: " + str(num_pages))
         for i in range(num_pages):
            curr_page_content = t_contents.pages[i]
            curr_page_txt = curr_page_content.extract_text()
            st.write(curr_page_txt)
            dst_pdf.addPage(t_contents.getPage(i))
      st.write(t_contents.pages)
      pdf_bytes = io.BytesIO()
      dst_pdf.write(pdf_bytes)
      pdf_bytes.seek(0)
      st.image(pdf_bytes)
      # img = Image.open(pdf_bytes)
      # t_fileName = now.strftime("%H%M%S") + ".jpg"
      # img.save(t_fileName, 'JPG')
      # pdf_bytes.flush()
