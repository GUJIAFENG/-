import streamlit as st

# 本地視頻文件的路徑
video_file = 'C:/milktea/img/03/03-1.mp4'  # 請替換為您的視頻文件路徑

# 播放本地視頻
st.video(video_file)
st.video(video_file, start_time=0, format="video/mp4", width=640, height=480)