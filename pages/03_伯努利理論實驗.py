import streamlit as st

st.markdown(""" <h1 style='text-align: center;'>實驗三:伯努利理論實驗 </h1> """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>第七組實驗報告</span><br/>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>壹、 實驗目的</span><br/>
藉由此實驗來檢驗伯努利方程式中能量守恆的概念。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>貳、 儀器與設備</span><br/>
乾溼球溫度計 控制箱與操作面板 測試段與測試件 標準流量產生裝置 標準流量產生器用AMCA噴嘴
""", unsafe_allow_html=True)

st.image("./img/03/03-02-1.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>參、 實驗原理</span><br/>
流體力學中，伯努利定理描述流體沿著一條穩定、非粘滯性，不可壓縮的流線移動，其壓力、速度及高度的變化形成一關係式，此一關係式對於流體力學
中許多運動的特性做了合理的解釋。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>肆、實驗步驟</span><br/>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# 步驟 1
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-1.png")
with col2:
    st.markdown("""
    ### STEP1
    <span style='font-size:25px;'>開啟控制面板上的System Power:系統源開關。</span><br/> """, unsafe_allow_html=True)

# 步驟 2
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-2.png")
with col2:
    st.markdown("""
    ### STEP2
    <span style='font-size:25px;'>確認乾溼求溫度計的濕球水箱有水。</span><br/> """, unsafe_allow_html=True)

# 步驟 3
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-3.png")
with col2:
    st.markdown("""
    ### STEP3
    <span style='font-size:25px;'>系統開機後需暖機10分鐘後方可開始測試。 
    紀錄乾溼球溫度及大氣壓力。</span><br/> """, unsafe_allow_html=True)

# 步驟 4
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-4.png")
with col2:
    st.markdown("""
    ### STEP4
    <span style='font-size:25px;'>確認輔助風機頻率調整旋鈕往逆時針旋轉至底 
 輔助風機頻率顯示器:顯示目前輔助風機運轉頻率值0.0 Hz。 </span><br/> """, unsafe_allow_html=True)

# 步驟 5
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-5.png")
with col2:
    st.markdown("""
    ### STEP5
    <span style='font-size:25px;'>根據所需實驗的風量選擇合適的噴嘴後,於標準流量產生器安裝噴嘴,噴嘴安裝方式可參考3.2 標準風量產生裝置操作。</span><br/> """, unsafe_allow_html=True)

# 步驟 6
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-6.png")
with col2:
    st.markdown("""
    ### STEP6
    <span style='font-size:25px;'>將5.4PL6噴嘴腔室往前輕推,關閉噴嘴前後腔室。並且將噴嘴腔室兩側5.8固定扣拑扣上，以固定噴嘴腔室。</span><br/> """, unsafe_allow_html=True)

# 步驟 7
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-7.png")
with col2:
    st.markdown("""
    ### STEP7
    <span style='font-size:25px;'>選擇欲測試之測試件，以及相對應之手輪，如左圖中選擇孔口板測試件。</span><br/> """, unsafe_allow_html=True)

# 步驟 8
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-8.png")
with col2:
    st.markdown("""
    ### STEP8
    <span style='font-size:25px;'>將測試件安裝於標準流量產生器上之測試段。</span><br/> """, unsafe_allow_html=True)

# 步驟 9
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-9.png")
with col2:
    st.markdown("""
    ### STEP9
    <span style='font-size:25px;'>按下面板RUN按鍵,使變頻器與風機產生連動關係。</span><br/> """, unsafe_allow_html=True)

# 步驟 10
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-10.png")
with col2:
    st.markdown("""
    ### STEP10
    <span style='font-size:25px;'>觀察噴嘴前後差壓(P56)並記錄,將此數值與Step2中紀錄的環境狀態，輸入AMCA210軟體中，計算出當前流量。</span><br/> """, unsafe_allow_html=True)

# 步驟 11
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-11.png")
with col2:
    st.markdown("""
    ### STEP11
    <span style='font-size:25px;'>記錄其他溫度、壓力的參數數值,以利帶入AMCA 210 風量計算軟體。</span><br/> """, unsafe_allow_html=True)

# 步驟 12
col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-12.png")
with col2:
    st.markdown("""
    ### STEP12
    <span style='font-size:25px;'>記錄水柱壓力計之壓力分佈數值,或使用dP表紀錄其顯示值。 </span><br/> """, unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.image("./img/03/03-04-13.png")
with col2:
    st.markdown("""
    ### STEP13
    <span style='font-size:25px;'>將標準流量產生裝置參數值輸入AMCA210軟體,得到標準流量值。</span><br/> """, unsafe_allow_html=True)



st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>伍、實驗結果與討論</span><br/>

""", unsafe_allow_html=True)


st.image("./img/03/03-1.png")
st.image("./img/03/03-2.png")
st.image("./img/03/03-3.png")
st.image("./img/03/03-4.png")
st.image("./img/03/03-5.png")
st.image("./img/03/03-6.png")

st.markdown("<br>", unsafe_allow_html=True)

























# 在這裡添加實驗一的具體內容，如圖表、數據等

