import streamlit as st

st.markdown(""" <h1 style='text-align: center;'>期末報告 </h1> """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(""" <h1 style='text-align: center;'>國立虎尾科技大學機械設計工程系 </h1> """, unsafe_allow_html=True)
st.markdown(""" <h1 style='text-align: center;'>113學年度『機械工程實驗(二)：熱流力實驗』: </h1> """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.write("<span style='font-size:25px;'>期末報告主題</span><br/>", unsafe_allow_html=True)

st.write("""
<span style='font-size:15px;'>一. 創新夾持裝置機械設計</span><br/>
<br>
<span style='font-size:15px;'>二. 環境量測與控制裝置機械設計</span>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<span style='font-family: SimHei; font-weight: bold; font-size: 18px;'>指導教授：</span><span style='font-family: SimHei; font-size: 18px;'>周榮源</span>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='font-family: SimHei; font-weight: bold; font-size: 18px;'>班級：</span><span style='font-family: SimHei; font-size: 18px;'>四設四甲</span>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='font-family: SimHei; font-weight: bold; font-size: 18px;'>組別：</span><span style='font-family: SimHei; font-size: 18px;'>第七組</span>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='font-family: SimHei; font-weight: bold; font-size: 18px;'>組員：</span><span style='font-family: SimHei; font-size: 18px;'>林奇川 吳政憲 白松桓 王翔楷 凃家豐 </span>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.write("""
<span style='font-family: SimHei; font-weight: bold; font-size: 18px;'>日期：</span><span style='font-family: SimHei; font-size: 18px;'>12月31日 </span>

""", unsafe_allow_html=True)

st.markdown(""" <h1 style='text-align: center;'> 一、概論 </h1> """, unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題一、創新夾持裝置機械設計</span><br/>
 1. 真空產生器的特點:
""", unsafe_allow_html=True)

st.write("""
●單段真空產生器：低成本、輕便小巧
●超靜音真空產生器：高效率、超靜音、可靠度高、堅固耐用

""")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
 2. 真空產生器的產品與功能介紹:
""")

st.write("""

●單段真空產生器:EV單段式真空產生器,提供了一個低成本、輕便小巧的真空產生器,二件式的設計可選配直通式的消音器使吸入的雜物可以從排出口排出,
直通式消音器是一種無堵塞的設計,被吸入的雜物會經過真空的通道由消音器排出。本
體結構是以鋁合金NC加工製作後做黑色陽級處理,噴嘴以鍍電解鎳的提高表面硬度的處理,
本系列的規格依噴嘴直徑0.5mm,1.0mm,1.5mm,2.0mm四種規格。
""")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-1.png")

st.write("""

超靜音真空產生器：本體鋁合金底座,銅合金的噴管以NC加工製作,產品可靠度高,堅固耐用,多段式、高效率雙噴管抽氣設計
，低壓力(3.5Bar)作動，空氣消耗量最小、真空度高（-660mmHg)、真空抽氣量大,
抽氣性能較一般產生器大約2倍,氣壓控制閥+真空破壞閥+真空過濾器+真空檢知開關多機能一體結構,
亦可分別選項組合,1/8"及1/2"堅固的鋁合金配管底座可供選擇。

""")

st.image("./img/07/07-2.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題二、環境量測與控制裝置機械設計</span><br/>
 1. 真空產生器的特點:
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

st.write("""

1.	散熱器元件或模組的特點與功能介紹
    散熱片，以導熱性佳、質輕、易加工之金屬，貼附於發熱表面，以複合的熱交換模式來散熱。
    散熱片不需要額外的驅動能源就能執行散熱，是最典型的被動性散熱元件。
    每種散熱片材質材料其導熱性能是不同的，按導熱性能從高到低排列，分別是銀，銅，鋁，鋼，
    不過如果用銀來作散熱片會太昂貴，最好的方案為採用銅質。雖然鋁便宜得多，但顯然導熱性就不如銅好（大約只有銅的百分之五十多點）。
    常用的散熱片材質是銅和鋁合金，二者各有其優缺點。
    銅的導熱性好，但價格較貴，加工難度較高，重量過大，熱容量較小，而且容易氧化。
    純鋁太軟，不能直接使用，都是使用的鋁合金才能提供足夠的硬度。
    鋁合金的優點是價格低廉，重量輕，但導熱性比銅就要差很多。
    有些散熱器就各取所長，在鋁合金散熱器底座上嵌入一片銅板。

""")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-3.png")