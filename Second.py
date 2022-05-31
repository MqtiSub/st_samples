import streamlit as st
import matplotlib.pyplot as plt
import math 
import numpy as np
st.title("Linear function")
graph_a = st.slider('coordinateOfA',-4,4,0)
graph_b = st.slider('coordinateOfB',-4,4,0)
graph_c = st.slider('coordinateOfC',-4,4,0)
graph_x = np.linspace(-50,50,1000)
graph_y = graph_a*graph_x*graph_x+graph_b*graph_x+graph_c
fig = plt.figure()
plt.plot(graph_x,graph_y)
st.pyplot(fig)
