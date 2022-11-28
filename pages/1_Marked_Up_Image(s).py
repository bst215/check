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
st.write("Page Two")



for i in range(len(c_pages)):
    st.image(c_pages[i])