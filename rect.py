import streamlit as st
import numpy as np


st.set_page_config(page_title="Rounded Rectangles", page_icon=":guardsman:", layout="wide")

color_var = st.sidebar.selectbox("Select a color", ["red", "green", "blue"])

st.cache(persist=True)
def update_color_var():
    return color_var
color_var = update_color_var()

# Create a function to generate the rectangles
def rounded_rect(x, y, w, h, r):
    return np.array([
        [x+r, y],
        [x+w-r, y],
        [x+w, y+r],
        [x+w, y+h-r],
        [x+w-r, y+h],
        [x+r, y+h],
        [x, y+h-r],
        [x, y+r],
        [x+r, y]
    ])

# Create a function to change the color of the rectangles
def set_color(color_var):
    if color_var == "red":
        return "#ff0000"
    elif color_var == "green":
        return "#00ff00"
    elif color_var == "blue":
        return "#0000ff"
st.markdown( "<div style='position:relative;'>")
for i in range(6):
    x = 0
    y = 17*(i-1)
    w = 200
    h = 55
    r = 5
    color = set_color(color_var)
    st.markdown(f"<div style='outline-color: #000000; outline-style: solid; position:relative; width:{w}px; height:{h}px; background-color: {color}; border-radius: {r}px; margin:1px;  top:{y}px; left:{x}px;'></div>", unsafe_allow_html=True)
    
st.markdown("</div>", unsafe_allow_html=True)    
st.markdown("""
<div style='position:relative;'>
<div style='outline-color: #000000; outline-style: solid;position:relative; width:230px; height:230px; background-color: {color}; border-radius: 15px; margin:10px;  top:-300px; left:400px;'></div>, unsafe_allow_html=True
</div>", unsafe_allow_html=True """)
