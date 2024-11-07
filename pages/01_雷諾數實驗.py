import streamlit as st



st.markdown(""" <h1 style='text-align: center;'>實驗一: 雷諾數實驗</h1> """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>第七組實驗報告</span><br/>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>壹、 實驗目的</span><br/>
以墨汁流入透明之壓克力管流中，觀察流體在管路中流動的情形，並配合計算出 Re(雷諾數) ，以膫解層流和紊流與雷諾數(Re)之間的關係。
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>貳、 儀器與設備</span><br/>
""", unsafe_allow_html=True)

st.image("./img/01/01-1.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>參、 實驗原理</span><br/>
研究流體力學的過程中，我們會遇到為數不少的無因次參數,如Re、Fr、Ma等, 但其中最為大家所熟知的則為Re,及雷諾數。
其物理意義維慣性力與黏性力之比值，式中<span style='color:red;'>ρ、V、L、μ</span>分別為密度、平均速度、特徵長度、絕對黏度(或動力黏度)，對一管流而言，特徵長度為直徑<span style='color:red; '>D</span><br/>

""", unsafe_allow_html=True)

st.write("""則 <span style='color:red; font-size:25px;'>Re=ρVL/μ ; Re=ρVD/μ</span><br/>   """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.image("./img/01/01-2.png")

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>肆、實驗步驟</span><br/>
1. 墨水加水稀釋(約1:5)後裝入點滴液瓶內並裝置在儀器上端。
2. 打開進水口閥及內管出水口閥，並將進出口流量控制在穩定流動狀 態(即外管水位維持在某一固定位置不變)。 
3. 將墨水之控制閥打開讓墨水穩定的滴入套筒中。 
4. 觀察墨水於管路中流動的情形(層流、紊流或於臨界區域)同時用 量杯(或水筒)量取流量並用碼錶確實測量時間(秒)將此等資料數據(流動情形、流量、測量時間)詳細計錄。 
5. 改變流量(由小到大)至少取五種不同的流量，以確實觀察由層流變化到完全紊流的情形。
6. 實驗結束，將墨水關閉，且洗淨針頭後置淸水桶內，以免墨汁乾化，堵塞針孔，同時開大進水閥(出口閥維持略開)讓淸水充滿套筒內 部(此時會有多餘的水從溢水口流出)讓其自然循環數分鐘將墨汁 淸洗掉。 
7. 最後再將進水閥關閉，並打開出口閥和洩水閥將水排乾。 
8. 擦淨儀器本身及四周地板。 
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>伍、實驗結果與討論</span><br/>

""", unsafe_allow_html=True)

st.write("""
<span style='color:red;'>1. 依實驗之觀察和計算結果，試判斷層流和紊流的臨界區域値在何種範圍。 </span><br/>
<span style='color:red;'>2. 爲何在靠近管路之進出口端點處，流動均呈不穩定現象。 </span><br/>
<span style='color:red;'>3. 試繪出層流和紊流之流動情形？並說明層流和紊流時水分子的流動情形。 </span><br/>
<span style='color:red;'>4. 依據實驗數據及觀察結果，本實驗和一般衆多書籍所敍述之數據是否符合？若不符合，你認爲原因出在那裡，應如何改善。 </span><br/>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>陸、測驗題</span><br/>

1. 雷諾數公式<span style='color:red;'>Re=ρVD/μ</span>方程式。  

2. Re 之物理意義<span style='color:red;'>慣性力與黏性力之比值</span>。

3. 一般而言,Re大於 <span style='color:red;'>4000</span>,爲湍流,小於<span style='color:red;'>2300</span>爲層流。        

4. 推導Re之單位:<span style='color:red;'>無因次</span>。   

5. 以實驗室之 D=2.5cm 而言，若水之 μ =1x10-3N-s/m2,則在層流之狀況，其 V 應小於<span style='color:red;'>0.092</span>。          

6. 在同上,在擾流之情況,V應大於:<span style='color:red;'>0.16</span>。

7. 若管徑2cm,Q=10l/min,請問此時之Re=<span style='color:red;'>10600</span> N,，其流場應爲<span style='color:red;'>湍流</span>。    
     
8. Re 數之功用位:<span style='color:red;'>判斷流體為層流or擾流</span>。          

""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

st.write("""
<span style='color:blue; font-size:25px;'>柒、實驗數據</span><br/>
暫無
""", unsafe_allow_html=True)

# 在這裡添加實驗一的具體內容，如圖表、數據等

