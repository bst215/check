import streamlit as st
import cv2
from PIL import Image
from datetime import datetime
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
c_pages = []
pic = None

def page_to_image(t_page, show_bb):
    pic = t_page.get_pixmap()
    # st.image(pic.pil_tobytes(format="JPEG"))
    if (show_bb == False):
        t_read = reader.readtext(pic.pil_tobytes(format="JPEG"))
    for t in range(len(t_read)-1):
        # m_dict.update({t: reader.readtext(pic.pil_tobytes(format="JPEG"))[t][1]})
        m_dict.update({g: t_read[t][1]})
        g+=1
    return pic

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   # t_contents = PdfReader(t_file)
   img = fitz.open(stream=t_file.getvalue(), filetype="pdf")
   # num_pages = len(t_contents.pages)
   with c1:
      for page in img:
         c_pages.append(page_to_image(page, False))
   with c2:
     st.write(m_dict)
     for i in range(len(c_pages)):
        st.image(c_pages[i])


