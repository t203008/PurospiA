import streamlit as st
import pandas as pd
st.title("称号")
position=st.radio("",("投手","野手"))
go=st.radio("称号はどう決めますか。",("ランダム","自分で","おまかせ"))
st.write("※おまかせは現在使えません")
tarL1=["球威","制球","スタミナ","スピリッツ"]
tarL2=["球威","制球","スタミナ","特になし"]
TarL2=["球威","制球","スタミナ","特になし"]
TARl1=["ミート","パワー","走力","スピリッツ"]
TARl2=["ミート","パワー","走力","特になし"]

if go=="自分で":
  if position=="投手":
    shogo=pd.read_csv("投手称号.csv")
    target1=st.selectbox("上げたい能力①は何ですか",tarL1)
    one=tarL1.index(target1)
    if target1=="球威" or target1=="制球" or target1=="スタミナ":
      tarL2.remove(target1)
      sta1=st.slider("この能力を最低どのくらい上げたいですか。",min_value=-1,max_value=3,step=1)
      target2=st.selectbox("上げたい能力②は何ですか",tarL2)
      two=TarL2.index(target2)
      sta2=st.slider("この能力をどの程度上げたいですか。",min_value=-1,max_value=3)
    else:
      sta1=st.slider("この能力を最低どのくらい上げたいですか。",min_value=0,max_value=30,step=15)
      
  if position=="野手":
    shogo=pd.read_csv("野手称号.csv")
    target1=st.selectbox("上げたい能力①は何ですか",TARl1)
    if target1=="ミート" or target1=="パワー" or target1=="走力":
      TARl2.remove(target1)
      sta1=st.slider("この能力を最低どのくらい上げたいですか。",min_value=-1,max_value=3,step=1)
      target2=st.selectbox("上げたい能力②は何ですか",TARl2)
      sta2=st.slider("この能力をどの程度上げたいですか。",min_value=-1,max_value=3)
    else:
      sta1=st.slider("この能力を最低どのくらい上げたいですか。",min_value=0,max_value=30,step=15)

#if go=="おまかせ":
#  if position=="投手":
#    shogo=pd.read_csv("投手称号.csv")
#    target=st.multiselect("称号の目的は何ですか。",["同値","能力をAに","弱点克服","得意強化","スピリッツ補強"],)
#    st.write("選手の詳細を教えてください")
#    st.number_input("球威",0,100,60)   
#    st.number_input("制球",0,100,60)
#    st.number_input("スタミナ",0,100,60)
#  else:
#    shogo=pd.read_csv("野手称号.csv")
#    target=st.multiselect("称号の目的は何ですか。",["同値","能力をAに","弱点克服","得意強化","スピリッツ補強"],)
#    st.write("選手の詳細を教えてください")
#    st.number_input("ミート",0,100,60)   
#    st.number_input("パワー",0,100,60)
#    st.number_input("走力",0,100,60)
    
start=st.button("実行")
if start==True:
  if go=="おまかせ":
      st.write("現在未実装です")
  if go=="自分で":
    shogo.fillna(0,inplace=True)
    if target1=="スピリッツ" or target2=="特になし":
      star=shogo[shogo[target1]>=sta1]
    else:
      star=shogo[(shogo[target1]>=sta1)&(shogo[target2]>=sta2)]
    st.write("称号一覧")
    st.write(star)
    per=pd.DataFrame(data={"星":[1,2,3,4],
                    "該当数":[1,4,5,5],
                    "確率":[1/3,4,4,4]})
    per=per.set_index("星")
    st.write(per)
    
    
