import streamlit as st
import random


st.set_page_config(
    page_title="REM Waste: English Accent Detector",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("🎤 English Accent Detector for Hiring")


video_url = st.text_input(
    "Enter Public Video URL:",
    placeholder="e.g., https://www.loom.com/share/your-video-id or https://example.com/video.mp4"
)


if st.button("Analyze Accent"):
    if video_url:
        st.subheader("Analysis in Progress...")
        st.info(f"Attempting to process video from: `{video_url}`")

        st.markdown("---")
        st.write("1. **Simulating Audio Extraction...**")
        st.write("*(In a real application, this step would use `moviepy` or `ffmpeg` to extract audio.)*")
        st.success("Audio extraction simulated successfully!")
        st.markdown("---")

        st.write("2. **Simulating Accent Analysis...**")
        st.write("*(In a real application, this step would involve a pre-trained ML model or an external API.)*")
        possible_accents = [
            "American English",
            "British English",
            "Australian English",
            "Canadian English",
            "Indian English",
            "Non-Native English (Neutral)",
            "Irish English",
            "South African English"
        ]
        classified_accent = random.choice(possible_accents)
        confidence_score = random.randint(70, 99) # Score between 70-99%

        st.success("Accent analysis simulated successfully!")
        st.markdown("---")

        st.subheader("📊 Analysis Results:")

        st.markdown(f"### Detected Accent: **{classified_accent}**")
        st.metric(label="Confidence in English Accent", value=f"{confidence_score}%")

        st.markdown("#### Summary/Explanation:")
        if "Non-Native" in classified_accent:
            st.info(f"The speaker's accent was classified as **{classified_accent}** with a confidence of **{confidence_score}%**. This suggests a strong grasp of English, potentially with subtle influences from another native language, or a very clear, standardized pronunciation.")
        else:
            st.info(f"The speaker's accent was classified as primarily **{classified_accent}** with a confidence of **{confidence_score}%**. This indicates a clear and recognizable pronunciation consistent with this regional dialect of English.")

        st.markdown("""
        ---
        *Disclaimer: The results above are simulated for demonstration purposes.
        A production-ready system would require robust audio processing and
        advanced machine learning models for accurate accent detection.*
        """)

    else:
        st.warning("Please enter a video URL to analyze.")

st.markdown("---")
st.caption("AI Hiring Agent")

