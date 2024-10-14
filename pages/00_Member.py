import streamlit as st

st.markdown("<br><br>", unsafe_allow_html=True)
st.title("小組成員")

# 第一位成員
st.write("""
<span style="font-size:20px;">機械設計系 41023130 林奇川 </span><br>
<span style="color:red; font-size:23px;">座右銘:</span><span style="font-size:20px;">在尿都憋不住的年紀卻憋住了想你。</span>
""", unsafe_allow_html=True)
st.image("./img/1.jpg", width=350)

st.markdown("<br><br><br>", unsafe_allow_html=True)

# 第二位成員
st.write("""
<span style="font-size:20px;">機械設計系 41023118 吳政憲</span><br>
""", unsafe_allow_html=True)
st.image("./img/2.jpg", width=350)
