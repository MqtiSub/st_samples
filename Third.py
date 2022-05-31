import streamlit as st
import matplotlib.pyplot as plt
import math 
import numpy as np
st.title("Cubic function")
graph_a = st.slider('coordinateOfA',-4,4,0)
graph_b = st.slider('coordinateOfB',-4,4,0)
graph_c = st.slider('coordinateOfC',-4,4,0)
graph_d = st.slider('coordinateOfD',-4,4,0)
graph_x = np.linspace(-8,8,100)
graph_y = graph_a*graph_x**3+graph_b*graph_x**2+graph_c*graph_x+graph_d
fig = plt.figure()
plt.xlabel('x')  # 横軸のラベル
plt.ylabel('y',  rotation=0)  # 縦軸のラベル
plt.grid()
plt.plot(graph_x,graph_y)
st.pyplot(fig)
