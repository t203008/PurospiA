import streamlit as st
import pandas as pd
st.title("称号")
position=st.radio("",("投手","野手"))
start=st.button("実行")
if start==True:
  st.write("よし")
