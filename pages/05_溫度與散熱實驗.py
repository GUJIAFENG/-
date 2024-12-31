import streamlit as st

st.markdown(""" <h1 style='text-align: center;'>實驗五:溫度與散熱實驗 </h1> """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>第七組實驗報告</span><br/>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>壹、 實驗目的</span><br/>
量測液體黏滯係數，實驗中改變液體溫度，紀錄黏滯係數與溫度變化的關係
""", unsafe_allow_html=True)



st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>貳、 儀器與設備</span><br/>
供電機  LED燈   安培計  亮度值測量器
""", unsafe_allow_html=True)


images = [f"./img/05/05-{i}.png" for i in range(1, 5)]

# 每行顯示的圖片數量
num_columns = 4

# 創建相簿佈局
rows = len(images) // num_columns + 1
for row in range(rows):
    cols = st.columns(num_columns)
    for col in range(num_columns):
        index = row * num_columns + col
        if index < len(images):
            cols[col].image(images[index], use_container_width=True)


st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>參、 實驗原理</span><br/>

""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>肆、實驗步驟</span><br/>
1. 調至欲量測之電壓電流。(約2.5-3.3 V (伏特),A (安培)不調)。
2. 將電供應給LED燈(兩處:紅對紅，黑對黑)。
3. 即可開始量測溫度、亮度。
4. 亮度量測方法，如圖示,用量測器蓋住LED燈即可。
5. 測量溫度方法，如圖示，量測線路觸碰 LED 燈面板的上下面(兩處)。
6. 查看數據。

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>伍、實驗結果與討論</span><br/>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>陸、實驗數據</span><br/>
暫無
""", unsafe_allow_html=True)