import streamlit as st


st.markdown(""" <h1 style='text-align: center;'>王沛沛自拍照</h1> """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>王沛沛照片區</span><br/>
</div>
""", unsafe_allow_html=True)


# 生成圖片列表
images = [f"./img/02/02-{i}.jpg" for i in range(1, 6)]

# 每行顯示的圖片數量
num_columns = 2

# 創建相簿佈局
rows = len(images) // num_columns + 1
for row in range(rows):
    cols = st.columns(num_columns)
    for col in range(num_columns):
        index = row * num_columns + col
        if index < len(images):
            cols[col].image(images[index], use_column_width=True)




# 在這裡添加實驗一的具體內容，如圖表、數據等