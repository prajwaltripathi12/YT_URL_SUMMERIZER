import streamlit as st
import validators

from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.documents import Document

from langchain_groq import ChatGroq

from langchain_community.document_loaders import (
    UnstructuredURLLoader
)

from youtube_transcript_api import YouTubeTranscriptApi


# =========================================================
# Load Environment Variables
# =========================================================

load_dotenv()

# =========================================================
# Streamlit Page Config
# =========================================================

st.set_page_config(
    page_title="LangChain URL/YT Summarizer",
    page_icon="🦜",
    layout="centered"
)

# =========================================================
# App Title
# =========================================================

st.title("🦜 LangChain URL & YouTube Summarizer")

st.markdown(
    """
    Summarize:
    - YouTube Videos
    - Website URLs

    using Groq + LangChain LCEL
    """
)

# =========================================================
# Sidebar
# =========================================================

with st.sidebar:

    st.header("🔑 API Configuration")

    groq_api_key = st.text_input(
        "Enter Groq API Key",
        type="password"
    )

# =========================================================
# URL Input
# =========================================================

generic_url = st.text_input(
    "Enter YouTube or Website URL"
)

# =========================================================
# Prompt Template
# =========================================================

prompt = ChatPromptTemplate.from_template(
    """
    You are an expert text summarizer.

    Summarize the following content in approximately
    300 words.

    Focus on:
    - Main ideas
    - Key insights
    - Important conclusions

    Content:
    {text}
    """
)

# =========================================================
# Output Parser
# =========================================================

output_parser = StrOutputParser()

# =========================================================
# Summarize Button
# =========================================================

if st.button("Summarize Content"):

    # =====================================================
    # Validation
    # =====================================================

    if not groq_api_key:

        st.error("Please enter your Groq API Key")
        st.stop()

    if not generic_url:

        st.error("Please enter a URL")
        st.stop()

    if not validators.url(generic_url):

        st.error("Please enter a valid URL")
        st.stop()

    try:

        with st.spinner("Loading content and generating summary..."):

            docs = []

            # =====================================================
            # Initialize LLM
            # =====================================================

            llm = ChatGroq(
                model="llama-3.3-70b-versatile",
                groq_api_key=groq_api_key
            )

            chain = prompt | llm | output_parser

            # =====================================================
            # YouTube Handling
            # =====================================================

            if (
                "youtube.com" in generic_url
                or "youtu.be" in generic_url
            ):

                # =============================================
                # Extract Video ID
                # =============================================

                if "v=" in generic_url:

                    video_id = (
                        generic_url
                        .split("v=")[1]
                        .split("&")[0]
                    )

                elif "youtu.be/" in generic_url:

                    video_id = (
                        generic_url
                        .split("youtu.be/")[1]
                        .split("?")[0]
                    )

                else:

                    st.error("Invalid YouTube URL")
                    st.stop()

                # =============================================
                # Fetch Transcript
                # =============================================

                try:

                    ytt_api = YouTubeTranscriptApi()

                    transcript = ytt_api.fetch(video_id)

                    transcript_text = ""

                    for snippet in transcript:
                        transcript_text += snippet.text + " "

                    # =========================================
                    # Debug Preview
                    # =========================================

                    st.subheader("📺 Transcript Preview")

                    st.write(transcript_text[:500])

                    # =========================================
                    # Store As Document
                    # =========================================

                    docs = [
                        Document(
                            page_content=transcript_text
                        )
                    ]

                except Exception as e:

                    st.error(
                        f"Could not fetch transcript: {e}"
                    )

                    st.stop()

            # =====================================================
            # Website Handling
            # =====================================================

            else:

                try:

                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={
                            "User-Agent": "Mozilla/5.0"
                        }
                    )

                    docs = loader.load()

                except Exception as e:

                    st.error(
                        f"Could not load website content: {e}"
                    )

                    st.stop()

            # =====================================================
            # Validate Documents
            # =====================================================

            if not docs:

                st.error("No content loaded.")
                st.stop()

            # =====================================================
            # Combine Text
            # =====================================================

            text = "\n\n".join(
                doc.page_content
                for doc in docs
                if doc.page_content
            )

            # =============================================
            # Debug Information
            # =============================================

            st.subheader("📊 Debug Info")

            st.write("Documents Loaded:", len(docs))
            st.write("Extracted Text Length:", len(text))

            # =============================================
            # Empty Text Check
            # =============================================

            if len(text.strip()) == 0:

                st.error("No text extracted.")
                st.stop()

            # =============================================
            # Limit Token Size
            # =============================================

            text = text[:12000]

            # =====================================================
            # Generate Summary
            # =====================================================

            summary = chain.invoke({
                "text": text
            })

            # =====================================================
            # Display Result
            # =====================================================

            st.success("Summary Generated Successfully!")

            st.subheader("📄 Summary")

            st.write(summary)

    except Exception as e:

        st.error("An error occurred")

        st.exception(e)