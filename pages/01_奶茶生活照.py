import streamlit as st



st.markdown(""" <h1 style='text-align: center;'>奶茶生活照</h1> """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>奶茶照片區</span><br/>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

images = [f"./img/01/01-{i}.jpg" for i in range(1, 13)]

# 每行顯示的圖片數量
num_columns = 3

# 創建相簿佈局
rows = len(images) // num_columns + 1
for row in range(rows):
    cols = st.columns(num_columns)
    for col in range(num_columns):
        index = row * num_columns + col
        if index < len(images):
            cols[col].image(images[index], use_column_width=True)