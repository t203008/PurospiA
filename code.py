import streamlit as st
import pandas as pd
st.title("称号")
position=st.radio("",("投手","野手"))
go=st.radio("称号はどう決めますか。",("自分で","おまかせ"))
target=st.multiselect("称号の目的は何ですか。",["同値","能力をAに","弱点克服","得意強化"],)
start=st.button("実行")
if start==True:
  st.write("よし")
