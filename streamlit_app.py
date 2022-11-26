import streamlit as st
import cv2
from PyPDF2 import PdfReader

st.write("Welcome!")

m_cont = st.container()

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   t_contents = PdfReader(t_file)
   num_pages = len(t_contents.pages)
   with m_cont:
      st.write("Number of pages in the .PDF: " + str(num_pages))
