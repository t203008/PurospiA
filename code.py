import streamlit as st
import pandas as pd
st.title("称号")
position=st.radio("",("投手","野手"))
go=st.radio("称号はどう決めますか。",("ランダム","自分で","おまかせ"))
tarL1=["球威","制球","スタミナ","スピリッツ"]
tarL2=["球威","制球","スタミナ","特になし"]
tarL1.remove("スタミナ")

if go=="自分で":
  if position=="投手":
    target1=st.selectbox("上げたい能力①は何ですか",tarL1)
    if target1=="球威" or "制球" or "スタミナ":
      st.write(tarL1.remove(target1))
      sta1=st.slider("この能力をどの程度上げたいですか。",min_value=0,max_value=3)
    target2=st.selectbox("上げたい能力②は何ですか",tarL2)
    sta2=st.slider("この能力をどの程度上げたいですか。",min_value=0,max_value=3)
  if go=="おまかせ":
    target=st.multiselect("称号の目的は何ですか。",["同値","能力をAに","弱点克服","得意強化","スピリッツ補強"],)
start=st.button("実行")
if start==True:
  st.write("よし")
