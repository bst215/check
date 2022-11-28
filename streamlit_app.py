import streamlit as st
import cv2
from PIL import Image, ImageDraw as D
from datetime import datetime
import io
import os
import fitz
import easyocr
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")
st.write("Welcome!")

m_cont = st.container()
c1, c2 = st.columns(2)
now = datetime.now()
reader = easyocr.Reader(['en'])
g = 0
t = 0
m_dict = {}
m_df = pd.DataFrame(columns=['bbox', 'text', 'confidence'])
c_pages = []
c_df = []
pic = None
t_read = None

#def page_to_image(t_read, show_bb = False):
    # st.image(pic.pil_tobytes(format="JPEG"))
#    if (show_bb == False):

t_file = st.sidebar.file_uploader("Pick a PDF File")

if (t_file != None):
   # t_contents = PdfReader(t_file)
   img = fitz.open(stream=t_file.getvalue(), filetype="pdf")
   # num_pages = len(t_contents.pages)
   with c1:
      for page in img:
        pic = page.get_pixmap()
        t_read = reader.readtext(pic.pil_tobytes(format="JPEG"), contrast_ths = 2.0)
        # page_to_image(t_read)
        for t in range(len(t_read)):
           # m_dict.update({t: reader.readtext(pic.pil_tobytes(format="JPEG"))[t][1]})
           m_dict.update({g: t_read[t][1]})
           g+=1
        #m_df = pd.DataFrame(t_read, columns=['bbox', 'text', 'confidence'])
        m_df = pd.DataFrame(t_read[t][[0][0]])
        c_pages.append(pic.pil_tobytes(format="JPEG"))
        c_df.append(m_df)
   with c2:
     if (len(c_pages) > 0):
        for j in range(len(c_df)-1):
            st.table(c_df[j])
        st.table(m_df)
        with c1:
            for i in range(len(c_pages)):
                st.image(c_pages[i])


