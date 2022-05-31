import streamlit as st
import matplotlib.pyplot as plt
import math 
import numpy as np
st.title("quadratic function")
graph_a = st.slider('coordinateOfA',-4,4,0)
graph_b = st.slider('coordinateOfB',-4,4,0)
graph_c = st.slider('coordinateOfC',-4,4,0)
graph_x = np.linspace(-8,8,100)
graph_y = graph_a*graph_x*graph_x+graph_b*graph_x+graph_c
plt.xlabel('x')  # 横軸のラベル
plt.ylabel('y',  rotation=0)  # 縦軸のラベル
plt.grid()  # グリッド（目盛り線）を表示
fig = plt.figure()
plt.plot(graph_x,graph_y)
st.pyplot(fig)
