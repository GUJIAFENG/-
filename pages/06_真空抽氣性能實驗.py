import streamlit as st

st.markdown(""" <h1 style='text-align: center;'>實驗六:真空抽氣性能實驗 </h1> """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>第七組實驗報告</span><br/>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>壹、 實驗目的</span><br/>
真空抽氣之目的在造就一低壓力或極低壓力的空間，而所能達到之壓力視真空系統內氣 體負荷與真空幫浦抽氣速率大小而定， 
如果抽氣量大於氣體負荷，則系統壓力會逐漸降低， 直到兩者相等後，則系統維持在終極壓力而不再改變。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>貳、 儀器與設備</span><br/>
真空幫浦 腔體 真空值量測器
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/06/06-1.png")
st.image("./img/06/06-2.png")
st.image("./img/06/06-3.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>參、 實驗原理</span><br/>
真空幫浦之功能是將一特定空間之氣體抽除，使氣體密度降低，達到某一壓力狀態。但 是,氣體在真空系統中之流動特性隨壓力之不同而有很大差異,如表1所示。
因此,對不同 壓力範圍必須依相對應之抽氣原理來設計不同型態幫浦。
同時，針對特定抽氣要求，需組合 搭配不同性能與型態之真空幫浦來使用，才能達到有效又經濟之真空抽氣目的。
""", unsafe_allow_html=True)

st.image("./img/06/06-4.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>肆、實驗步驟</span><br/>

1. 將閥門轉至全開(約16圈,每個人手徑不同)。
2. 將腔體蓋子蓋上，管路末端的出口開關關上，接著開啟幫浦，開始抽真空，一段時間後，可以嘗試打開蓋子(打不開的，如果打開了代表有出錯)。
3. 開始觀察測量器上的數值,直到數值穩定,就將閥門準10圈至半開狀態,再重複1、2步驟,然後觀測數值。
4. 查看數據下圖為半開(最為穩定的數值)。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>伍、實驗結果與討論</span><br/>

在真空技術中，真空數值越大，通常表示真空度越低（接近大氣壓）；相反，真空數值越小，則表示真空度越高（接近理論上的絕對真空）。以下是詳細解釋：
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
1. <span style='color:red;'>真空等級的理解 • 高壓（低真空）:</span><br/>
    
    當壓力值較大（例如 760 Torr,101.3 kPa)時，表示系統內的氣體較多,真空度較低,抽氣效果較弱。
    • 低壓（高真空）： 當壓力值較小（例如 10⁻³ Torr,1 mPa)時,表示系統內的氣體較少，真空度較高，接近理想真空。

2. <span style='color:red;'>真空技術中的壓力單位 • Torr（托）： 真空技術中常用單位</span><br/>
  一.  1 Torr ≈ 133.3 帕斯卡(Pa)。 
  二.  • 帕斯卡(Pa): 國際單位制壓力單位，真空工程中也常用。 
  三.  • Micron(微米汞柱): 1 微米汞柱 = 0.001 Torr,用於非常細微的真空測量。      
""", unsafe_allow_html=True)


st.write("""
例如： 
1. • 大氣壓： 約 760 Torr 或 101,325 Pa。 
2. • 中真空： 約 1 Torr 或 133.3 Pa。 • 高真空： 小於 10⁻³ Torr 或 0.133 Pa。 
3. • 超高真空： 小於 10⁻⁹ Torr 或 10⁻⁷ Pa。
""")

st.write("""
<span style='color:blue; font-size:25px;'>陸、實驗數據</span><br/>
暫無
""", unsafe_allow_html=True)

st.image("./img/06/06-5.png")