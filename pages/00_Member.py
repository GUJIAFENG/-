import streamlit as st

st.title("小組成員")

# 定義成員信息
members = [
    {"name": "我是林奇川 可以叫我川哥。", "motto": "在尿都憋不住的年紀卻憋住了想你。", "image": "./img/82123.jpg"},
    {"name": "我是陳濬祺 可以叫我地精。", "image": "./img/1.png"}
    
]

# 佈局每行兩個成員
for i in range(0, len(members), 2):
    cols = st.columns(2)
    for j in range(2):
        if i + j < len(members):
            with cols[j]:
                st.write(f"""
                <span style="font-size:20px;">{members[i + j]['name']}</span><br>
                """, unsafe_allow_html=True)
                if 'motto' in members[i + j]:
                    st.write(f"""
                    <span style="color:red; font-size:25px;">座右銘:</span><span style="font-size:20px;">{members[i + j]['motto']}</span>
                    """, unsafe_allow_html=True)
                st.image(members[i + j]['image'], width=300)
    st.write("")  # 添加空行

