import streamlit as st
import pandas as pd
st.title("称号")
position=st.radio("",("投手","野手"))
go=st.radio("称号はどう決めますか。",("","自分で","おまかせ"))
if go=="自分で":
  if position=="投手":
    target=st.selectbox("上げたい能力①は何ですか",["球威","制球","スタミナ","スピリッツ"])
    if target=="球威" or "制球" or "スタミナ":
      sta1=st.slider("この能力をどの程度上げたいですか。",min_value=0,max_value=3)
  if go=="おまかせ":
    target=st.multiselect("称号の目的は何ですか。",["同値","能力をAに","弱点克服","得意強化","スピリッツ補強"],)
start=st.button("実行")
if start==True:
  st.write("よし")
