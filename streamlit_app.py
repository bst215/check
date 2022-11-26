import streamlit as st
import cv2
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
from datetime import datetime
from pdf2image import convert_from_bytes, convert_from_path
import io
import os
import fitz

st.write("Welcome!")

m_cont = st.container()
now = datetime.now()

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   dst_pdf = PdfWriter()
   # t_contents = PdfReader(t_file)
   img = fitz.open(stream=t_file.getvalue(), filetype="pdf")
   # num_pages = len(t_contents.pages)
   for page in img:
      pic = page.get_pixmap()
      st.image(pic.pil_tobytes(format="JPEG"), output_format='PNG')


