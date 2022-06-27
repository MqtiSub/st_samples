import streamlit as st
import random
i = 0
a = 0
st.title("mendel thought")
number = st.number_input('append number for counts')
while i < number:
  i += 1
  if random.randint(1,4) == 1:
    a += 1

st.write(a/number)    
  

