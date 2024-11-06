import streamlit as st

st.markdown(""" <h1 style='text-align: center;'>實驗四: 黏滯係數量測</h1> """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>第七組實驗報告</span><br/>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>壹、 實驗目的</span><br/>
黏滯係數量測實驗是測定液體或氣體在特定條件下的黏滯性質，了解流體性質、測量不同溫度、壓力和組成下的黏滯係數。
""", unsafe_allow_html=True)
# 在這裡添加實驗一的具體內容，如圖表、數據等

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>貳、 儀器與設備</span><br/>
測黏滯定儀、燒杯 、測量電壓機、測黏滯定儀。
""", unsafe_allow_html=True)

st.image("./img/04/04設備.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>參、 實驗原理</span><br/>
黏滯力 f 和施力 F 方向相反，黏滯力 f 的 大小和平行板的面積 A 以及平行板的相對速度 dv 成正比，和平 板間的距離 dr 成反比 
""", unsafe_allow_html=True)

st.image("./img/04/04-3-1.png")
st.image("./img/04/04-3-2.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>肆、實驗步驟</span><br/>

1. 先將黏度計安裝完成並調整水平調整使水瓶氣泡至於黑圈中且打開黏度計電源

2. 將恆溫箱加入所要測的樣品，開啟電源與冷凍開關將溫度設定20℃

3. 取一個600ml標準燒杯，將樣品加至轉針測量高度，黏度計準備好參數設定完成，將護架裝
   置上去
4. 將黏度計放置於測量樣品中，裝上轉針

5. 設定轉針號碼與轉速並打開馬達開關鈕測量樣品黏度。帶黏度穩定後，讀取顯示幕數據並記
   錄，將冷凍開關關閉，再依序設定40、60℃進行量測。

6.  轉針號碼設定說明
    
    調整轉針設定轉針號碼(例:由1號變換至3號針)。
    選擇轉子換轉速組合，使扭矩百分比讀值在10-100%範圍內。黏度大的樣品，使用面積小的
    轉子換較低的轉速，對於低黏度的樣品，情況相反
""", unsafe_allow_html=True)

st.image("./img/04/04-4-1.png")
st.image("./img/04/04-4-2.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>伍、實驗結果與討論</span><br/>

水的溫度越高時，黏滯係數就越小，表示液體在高溫中，流動性越好，在低溫時流動性較差，
在不同轉速下 所測的黏滯係數相差不多。 

  因為低黏滯係數在轉子表面與液面產生相對摩擦力在轉速不同，相差不大，所得到的絕對黏度
也較相近。

問 <span style='color:red;'>請描述本次實驗心得及在學習上或未來工作上可以應用之(設計)案例?</span>


""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>陸、 實驗數據</span><br/>

""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

with open('report/實驗四.xlsx', 'rb') as file: st.download_button( label="實驗四", data=file, file_name='實驗四.xlsx', mime='application/vnd.ms-excel' )