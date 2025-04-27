import streamlit as st

# 🔧 Custom style to fix dropdown cursor (early setup)
def apply_custom_styles():
    st.markdown("""
        <style>
            .css-1wa3eu0-placeholder, .stSelectbox, .stSelectbox div, .stSelectbox span {
                cursor: pointer !important;
            }
        </style>
    """, unsafe_allow_html=True)

# 🧠 Page Title + Styles
st.title("🔍 Keyword Duplicator & Performance Recommender")
apply_custom_styles()

# 📁 Upload Section
uploaded_file = st.file_uploader(
    "📁 Upload your keyword file (.csv or .docx)", 
    type=["csv", "docx"]
)

# 🧪 Test: Show uploaded file name
if uploaded_file is not None:
    st.success(f"Uploaded file: {uploaded_file.name}")
