import streamlit as st
import cv2
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from datetime import datetime
from pdf2image import convert_from_bytes, convert_from_path
import io
import os

st.write("Welcome!")

m_cont = st.container()
now = datetime.now()

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   dst_pdf = PdfWriter()
   # t_contents = PdfReader(t_file)
   img = convert_from_path(t_file)
   # num_pages = len(t_contents.pages)
   num_pages = len(img)
   if (num_pages > 0):
      page_one = img[0]
      # page_one_text = page_one.extract_text()
      with m_cont:
         st.write("Number of pages in the .PDF: " + str(num_pages))
      for k in range(num_pages):
         st.image(img[k])


