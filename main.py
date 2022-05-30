import streamlit as st
import matplotlib.pyplot as plt
import math 
import numpy as np
st.title("Linear function")
graph_a = st.slider('coordinateOfA',-4,4,0)
graph_b = st.slider('coordinateOfB',-4,4,0)
graph_x = np.linspace(-8,8,100)
graph_y = graph_a*graph_x+graph_b
plt.plot(graph_x,graph_y)
plt.show()
