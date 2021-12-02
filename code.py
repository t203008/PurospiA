import streamlit as st
import pandas as pd
batter=st.file_uploader("野手", type='csv')
pitcher=st.file_uploader("投手", type='csv')
st.write(pd.read_csv(batter))