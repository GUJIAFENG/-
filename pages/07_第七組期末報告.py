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

""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

st.write("""

1.	散熱器元件或模組的特點與功能介紹
散熱片是一種利用金屬材料高導熱性的元件，通過貼附在發熱表面來進行熱量傳導，並採用複合熱交換模式來達到散熱效果。
由於其無需額外的能源驅動，因此屬於典型的被動式散熱元件。散熱片材料的導熱性能比較散熱片的性能與其材質息息相關，
不同金屬的導熱性能從高到低排列依次為：銀>銅>鋁>鋼儘管銀的導熱性最佳，但由於成本過於昂貴，實際應用中最常見的是銅和鋁合金。
兩者各有優缺點：銅材散熱片:優點:導熱性極佳(比鋁高約2倍)。缺點：價格較高。加工難度大，適用範圍受限。
重量大，可能增加設備負擔。熱容量小，且容易氧化影響外觀和性能。鋁合金散熱片：優點：質量輕，適合需要減輕設備重量的應用。
價格低廉，加工性佳，適合大規模生產。缺點：導熱性僅為銅的一半左右，散熱性能相對較差。材料結合的應用與優化為了結合兩種材質的優勢，
有些散熱器在鋁合金底座中嵌入銅板，實現良好的散熱性能和成本控制。這種結構設計在性能與經濟性之間找到了平衡，是市場上的一種常見選擇。
""")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-3.png")

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(""" <h1 style='text-align: center;'> 二、 原理與設計方法(機械設計與繪圖) </h1> """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題一、創新夾持裝置機械設計</span><br/>
1. 真空產生器設計與要求規範:鋁塊大小76x53x26mm,管路連接口D=3。
 
2. 真空產生器設計方法
""", unsafe_allow_html=True)

st.image("./img/07/07-4.png")
st.image("./img/07/07-5.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""

3. 依據原理與工件大小之零組件設計圖

""")

st.image("./img/07/07-6.png")
st.write("接頭規格")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-6-1.png")
st.write("2D工程圖")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-6-2.png")
st.write("3D前視圖")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-6-3.png")
st.write("3D等角視圖")

st.image("./img/07/07-7.jpg")
st.write("實體圖1")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-8.jpg")
st.write("實體圖2")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題二、環境量測與控制裝置機械設計</span><br/>
""", unsafe_allow_html=True)

st.write("散熱片是通過熱的傳導方式進行散熱片。 傳導方式有：傳導、對流、輻射")

st.write("""
輻射： 熱能從熱源以電磁的形式直接發散出去,可以在真空中進行,傳熱效能取決於熱源的材料以及表面的顏色。

傳導： 指分子之間的動能交換，能量較低的粒子和能量較高的粒子碰撞從而獲得能量,單獨一塊散熱片不能實現熱能的傳導的。

對流： 透過熱的物質的運動來實現熱的傳遞,這意味着，熱能是來自於被氣體或者液體所包圍熱源,透過分子的移動來實現熱能的傳遞的,我們可以採用在散熱片上添加風扇的方法來實現強制對流。

""")

st.image("./img/07/07-9.png")
st.image("./img/07/07-10.png")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(""" <h1 style='text-align: center;'> 三、 實驗量測與數據分析 </h1> """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題一 創新夾持裝置機械設計</span><br/>

""", unsafe_allow_html=True)

st.write("1. 實驗測量數據")


st.image("./img/07/07-11.png")

st.write("1. 選擇模態")

st.image("./img/07/07-12.png")

st.write("2. 匯入圖檔")

st.image("./img/07/07-13.png")

st.write("3. 設置網格")

st.image("./img/07/07-14.png")

st.write("4. 設置入口、出口、牆壁")

st.image("./img/07/07-15.png")

st.image("./img/07/07-16.png")

st.image("./img/07/07-17.png")

st.write("5. 設置環境")

st.image("./img/07/07-18.png")

st.write("6. 設置邊界條件")

st.image("./img/07/07-19.png")

st.image("./img/07/07-20.png")

st.write("7. 最佳化設置、計算設置")

st.image("./img/07/07-21.png")

st.write("8. 結果分析")

st.image("./img/07/07-22.jpg")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題二、環境量測與控制裝置機械設計</span><br/>

""", unsafe_allow_html=True)

st.write("1. 實驗分析數據")

with open('report/07.xlsx', 'rb') as file: st.download_button( label="Heat Sink Design", data=file, file_name='Heat Sink Design.xlsx', mime='application/vnd.ms-excel' )

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.markdown(""" <h1 style='text-align: center;'> 四、 結果與討論 </h1> """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


st.image("./img/07/07-4-1.png")

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-4-2.jpg")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題一 創新夾持裝置機械設計</span><br/>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/07/07-23.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""實驗後發現電腦模擬出來和實際測量差距極大,我們認為因為圖和實際加工出來有稍微尺寸上的公差,
            還有鑽頭在鑽時的擴孔沒有考慮進去，在結果出來誤差數據相當的大，所以在實驗前應該將這些變數也考慮進去，
            在設計時也須注意這些細節。
            """)



st.write("""
<span style='color:blue; font-size:25px;'>主題二、環境量測與控制裝置機械設計</span><br/>

""", unsafe_allow_html=True)

st.image("./img/07/07-24.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write(""" 電腦模擬出的數據與實際測量的，會因為外界的因素而導致數據上的誤差，考試那天隨著濕氣上的不同、散熱片的狀態，是否有生鏽或有損壞等等的問題，
             都會影響測出來的數據，而電腦模擬出來的數據，是以無外界、無任何其他因素影響，以完美的情況所計算出來的，所以數據會因此而有誤差。
             """)




st.markdown(""" <h1 style='text-align: center;'> 五、結論 </h1> """, unsafe_allow_html=True)


st.write("""
<span style='color:blue; font-size:25px;'>主題一 創新夾持裝置機械設計</span><br/>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write(""" 透過這次的作業,老師利用課堂上介紹的真空原理,並看過操作示範,讓我們親手設計尺寸並製作實體,再利用Ansys程式進行模擬,
             比較實驗與模擬結果的數據差異。我們發現實驗結果的誤差值相當大，這促使我們深入思考並反省為何實驗結果會與模擬值不一致。經過組員討論後，
             我們認為造成誤差的主要原因可能包括以下幾點：繪圖時忽略了加工過程中鑽頭前端鑽唇的特性，
             以及實際加工中可能出現的公差。這些在繪圖階段未能充分考慮到的微小尺寸偏差，最終導致我們的實驗誤差值偏大。
             """)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>主題二、環境量測與控制裝置機械設計</span><br/>

""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write(""" 在這次實驗中，我們第一次測量的結果發現，散熱片頂部的溫度竟然比底部更高，這與模擬數據的預測完全不一致。
             經過組員討論並向老師請教問題可能的原因，我們了解到這可能是因為實驗裝置過於密集，導致散熱空間不足，熱量無法有效散出，
             反而使整個裝置溫度逐漸升高，未能達到理想的散熱效果。隨後，我們進行了第二次測量，這次採取了多次測量不同部位的方式，
             結果顯示數據與模擬結果更為接近。透過這次實驗，我們深刻體會到模擬在實驗設計中的重要性。在實驗前進行模擬並查閱相關資料，
             可以幫助我們提高實驗的準確性。同時，這次經驗也提醒我們，實驗過程中必須謹慎求證，不能掉以輕心。
             """)