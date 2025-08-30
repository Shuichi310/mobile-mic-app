import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.set_page_config(page_title="モバイル集音器", layout="centered")
st.title("📱 モバイル集音器（試作）")
st.markdown("スマホのマイクを使って、Bluetoothイヤホンに音を送ります。")

if st.button("マイクを起動"):
    webrtc_streamer(
        key="mic-stream",
        mode=WebRtcMode.SENDRECV,
        media_stream_constraints={"video": False, "audio": True},
        async_processing=True
    )
