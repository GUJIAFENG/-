import streamlit as st

st.markdown(""" <h1 style='text-align: center;'>實驗二: 水衝擊實驗</h1> """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>第七組實驗報告</span><br/>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>壹、 實驗目的</span><br/>
瞭解流體流動時，其動量變化與其承受力量間之關係，以驗証動量方程式。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>貳、 儀器與設備</span><br/>
水循環泵、驅動馬達、儲水槽、實驗台架、柏登壓力錶、流量控制閥、水衝擊台一套。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>參、 實驗原理</span><br/>
主要目的在驗証動量方程式。其應用頗為廣泛，如衝動式水輪機之分析、各型彎管、噴嘴之受力分析等均有賴動量方程式的計算
         一般可表為下列之形式
""", unsafe_allow_html=True)

st.image("./img/02/公式1.png")

st.write("""
<span style='color:blue; font-size:25px;'>肆、實驗步驟</span><br/>
1. 將 110V 之電源連接妥當。
2. 儲水槽加入之水量約九分滿。
3. 將噴嘴及硯板裝入水衝擊器內。
4. 將動量平衡器先預加上荷重約 350~450gms,使其壓縮彈簧約 80% 之壓縮量 (勿將彈簧完全壓縮，否則會產生很大的誤差)，並將平衡指標切口對準與平板同高，此時需將試重之實際重量［包括容器、即杯子］計錄下來，此即為預負荷。
5. 按下啟動馬達開關，並逐漸打開流量控制閥至某一特定流量。
6. 同時衝擊水流對硯板產生衝擊，而將硯板上推至最高點。此時開始加入荷重，至平板回到原來之平衡位置為止，取下容杯重新稱重，即得總負荷。總負荷減去預負荷，所得之重量即為水對硯板之衝擊力。
7. 逐漸打開流量控制閥（出口閥），以改變流量，重覆上述步驟，流量由小至大，至少取五種，並詳細記錄各值。
8. 關閉電源，並將出口閥關閉。
9. 依序更換噴嘴或硯扳，重覆 3~8 之步驟完成同樣之量測。
10. 實驗結束，關閉電源，並將流量測量槽內之水排放至儲水槽。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>伍、實驗結果與討論</span><br/>
1. <span style='color:red;'>討論硯板與噴嘴間之距離對硯板受力大小之影響。</span><br/>
    
    本實驗的主要目的是了解流體動量變化與其承受力之間的關係，並驗證動量方程式。透過對硯板受力的測量，
    我們探討了多個因素對受力的影響，包括硯板與噴嘴間的距離、噴嘴直徑以及硯板的形狀。

2. <span style='color:red;'>討論在同流量之情況下，噴嘴直徑與硯板受力之關係。</span><br/>
         
    實驗顯示，硯板與噴嘴之間的距離對硯板的受力有顯著影響。當距離增加時，水流在接觸硯板之前經過更長的路徑，流速可能因能量損失而減少，
    從而導致衝擊力下降。相反，當距離減少時，水流更直接地衝擊硯板，能夠最大化動量的傳遞，提高受力。
    在相同流量的情況下，噴嘴的直徑會顯著影響水流的速度及其動能。較大的噴嘴直徑會導致流速降低，使得每單位時間施加在硯板上的衝擊力減少。
    反之，較小的噴嘴直徑則會提高流速，從而增加衝擊力，因為水流在較小截面積中能保持較高速度，增強了動量的傳遞。

3. <span style='color:red;'>繪製流速與硯板受力之關係圖，比較三種硯板之受力情形。</span><br/>
         
    根據實驗數據，可以繪製流速與硯板受力的關係圖。該圖顯示了三種不同直徑噴嘴下，硯板所受的力隨流速變化的情況。通常，
    隨著流速的增加，硯板的受力也相應增強。不同直徑的噴嘴會呈現不同的斜率，顯示出受力增長的速率差異。

4. <span style='color:red;'>討論誤差大小與噴嘴直徑、硯板形狀間之關係</span>。
         
    實驗中可能出現的誤差來源與噴嘴直徑及硯板形狀密切相關。較小的噴嘴直徑可能增加測量誤差，因為流速的變化更明顯，
    流場的擾動也會更大，導致衝擊不均勻。此外，硯板的形狀（如平板或弧形）也會影響水流的分佈及衝擊效果，進一步引入測量誤差。
    例如，弧形硯板可能因水流的反射而導致誤差增加。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>陸、測驗題</span><br/>
1. 水衝擊實驗在驗証<span style='color:red;'>柏努力動量守恆</span>方程式。          
2. 本實驗有哪幾種硯板可供實驗：<span style='color:red;'>平板、45度圓錐形、半球形硯板</span>。                                                
3. 本實驗有那幾種規格之噴嘴： <span style='color:red;'>5mm、8mm</span>。                 
4. 在流量固定之下,使用同一硯板,配合那一個噴嘴衝擊力較大<span style='color:red;'>5mm</span>,為什麼<span style='color:red;'>口徑較小，流速越高，衝擊越大</span>。          
5. 在同一流量和噴嘴,那一種硯板衝擊力最大<span style='color:red;'>半球形硯板 平板</span>硯板衝擊力最小,最大約爲最小的<span style='color:red;'>2</span>倍。          
6. 在流量固定下何種噴嘴與硯板之組合衝擊力最大：<span style='color:red;'>5mm噴嘴半球形硯板</span>,何種組合衝擊力最小：<span style='color:red;'>8mm噴嘴平板</span>, 前者 約爲後者的<span style='color:red;'>2</span>倍。         
7. 1Kgw=<span style='color:red;'>9.8</span> N。          
8. 推導ρQV所得到之單位：<span style='color:red;'>(kg/m<sup>3</sup>) &times; (m<sup>3</sup>/s) &times; (m/s)</span> 。〈取ρ爲kg/m3,Q爲m3/s, V爲m/s〉          
9. 預負荷300gw,總負荷2800gw,Q=30l /min ,噴嘴5mm作用在半圓形硯板,則實際負荷為<span style='color:red;'>24.5</span>N ,理論衝擊力<span style='color:red;'>25</span>N,誤差爲<span style='color:red;'>2</span>％。         
""", unsafe_allow_html=True)

st.image("./img/02/02-9題.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>柒、 實驗記錄</span><br/>
""", unsafe_allow_html=True)



# 生成圖片列表
images = [f"./img/02/02-{i}.jpg" for i in range(1, 41)]

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
<span style='color:blue; font-size:25px;'>捌、 實驗數據</span><br/>

""", unsafe_allow_html=True)

with open('report/實驗2.xls', 'rb') as file: st.download_button( label="水衝擊實驗", data=file, file_name='水衝擊實驗.xls', mime='application/vnd.ms-excel' )

st.markdown("<br>", unsafe_allow_html=True)

# 在這裡添加實驗一的具體內容，如圖表、數據等