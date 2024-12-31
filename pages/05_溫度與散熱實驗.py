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
溫度與散熱實驗基於熱力學與熱傳導的原理。 這些實驗旨在分析熱能如何在不同條件下轉移、儲存及散失於各種材料或系統中。以下是核心原理：
""", unsafe_allow_html=True)

st.write("""
熱傳導機制 熱傳導通過三種主要機制發生： • 熱傳導：通過材料中粒子或分子之間的直接接觸來進行熱能傳遞。
熱傳導的速度由傅立葉定律(Fourier's Law)所決定：
""")

st.image("./img/05/0501.png")

st.write("""
其中 q 是熱傳遞速率,k 是熱導率,A 是橫截面積，而 dT/dx是溫度梯度。  
對流:由於流體或空氣的運動所引起的熱傳遞,可由牛頓冷卻定律Newton's Law of Cooling)描述：
""")

st.image("./img/05/0502.png")

st.write("""
其中 h 是對流熱傳遞係數,A 是表面積,Ts 是表面溫度,T∞ 是環境溫度。 
• 輻射：通過電磁波進行的熱傳遞，受斯特藩-玻尔兹曼定律(Stefan-Boltzmann Law)支配：
""")

st.image("./img/05/0503.png")

st.write("""
熱平衡 當進入系統的熱量等於離開系統的熱量時，便達到熱平衡。實驗通常集中於研究達到平衡所需的時間以及穩態溫度分佈。
""")

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

st.image("./img/05/0504.png")

st.write("""
<span style='color:blue; font-size:25px;'>伍、實驗結果與討論</span><br/>
1. <span style='color:red;'>溫度對LED的影響 LED的工作溫度升高主要由以下幾方面影響:</span><br/>
    
    半導體材料的能隙隨溫度升高而縮小，導致光子能量降低，影響發光效率。 
    • 載流子復合效率下降： 高溫會增加非輻射復合(Non-Radiative Recombination)的概率，從而降低光輸出。 
    • 材料特性改變： 高溫會導致材料內部應力、結構變化或加速老化。

2. <span style='color:red;'>熱阻的變化與影響 熱阻(Thermal Resistance)是LED芯片與散熱結構之間的熱傳導性能指標,主要由兩部分構成</span><br/>
         
    • 結構熱阻： LED內部芯片與基板之間的熱阻。 
    • 散熱熱阻： 散熱器與周圍環境的熱阻。 熱阻的變化現象： 
    • 當LED芯片內部或散熱結構的熱阻過高,會導致熱量積聚,升高結溫(Junction Temperature)。 
    • 結溫升高使熱阻進一步增加，形成惡性循環。 

    熱阻的影響：  

    • 高熱阻會降低LED的可靠性,加速老化,導致壽命縮短。 
    • 發光效率（光通量/電功率）降低，特別是在高電流操作下表現更明顯。
    
3. <span style='color:red;'>發光效率的變化 現象:</span><br/>
         
     光通量降低： 隨著溫度升高,LED的發光效率降低,表現為光通量減少。 
     • 熱輻射損失增加： 一部分能量以熱的形式損失而非轉化為光,
     原因： 
     • 量子效率下降： 高溫增加非輻射復合，降低內部量子效率(IQE)。 
     • 光提取效率下降： 高溫可能導致封裝材料的折射率變化或光學性能降低，影響光提取效率(EQE)。

4. <span style='color:red;'>實驗中觀察到的變化 • 結溫與熱阻:</span>。
         
    當驅動電流增大或散熱不良時，結溫顯著升高，導致熱阻曲線變陡。
     • 發光效率曲線： 隨著結溫上升，發光效率呈現非線性下降。
     • 壽命縮短： 長期高溫操作下,LED可能發生光衰減(Lumen Depreciation)。

5. <span style='color:red;'>改善措施 • 優化散熱設計：</span>。
         
    使用高導熱材料或改善散熱器結構以降低熱阻。 
     • 控制工作溫度： 減少過高電流運行，或使用主動冷卻技術（如風冷或液冷）。 
     • 改進封裝技術： 選擇高穩定性的封裝材料，提高光提取效率和耐熱性。
""", unsafe_allow_html=True)



st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>陸、實驗數據</span><br/>
暫無
""", unsafe_allow_html=True)