import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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

plt.figure()

for i in range(3):
    rectangle = Rectangle((50*i + 10, 50), 40, 40, linewidth=1, edgecolor='black', facecolor=set_color(color_var), rounded_corners=True)
    plt.gca().add_patch(rectangle)

plt.axis('scaled')
st.pyplot()
