import streamlit as st

st.set_page_config(page_title="熱流力實驗", layout="wide")

st.title("熱流力實驗第七組")

st.write("歡迎來到熱流力實驗報告。請從左側選單選擇要查看的實驗項目。")

# 不需要在這裡定義實驗項目列表，因為Streamlit會自動生成側邊欄

st.write("""
<span style="font-size:20px;">hello 我是第七組川哥。</span>
<br>
<span style="color:red; font-size:25px;">座右銘:</span><span style="font-size:20px;">在尿都憋不住的年紀卻憋住了想你。</span>
""", unsafe_allow_html=True)



st.image("./img/82123.jpg", width=300)