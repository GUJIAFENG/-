import streamlit as st

st.markdown(""" <h1 style='text-align: center;'>王沛沛影片區</h1> """, unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)

st.write("""
<div style='text-align: center;'>
    <span style='font-size:30px;'>沛沛豬的自言自語</span><br/>
</div>
""", unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)






# 使用 GitHub 的 "raw" URL
video_url = "https://raw.githubusercontent.com/GUJIAFENG/Streamlit-hw/live/img/03/03-1.mp4"

# 使用 HTML 嵌入視頻，並調整大小
video_html = f"""
    <video width="300" height="400" controls>
        <source src="{video_url}" type="video/mp4">
        您的瀏覽器不支持播放此視頻。
    </video>
    """

# 使用 st.markdown 嵌入 HTML
st.markdown(video_html, unsafe_allow_html=True)
