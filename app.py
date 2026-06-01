import streamlit as st
from agent import generate_document
from docx import Document
import io

st.set_page_config(
    page_title="AI Document Generator",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Document Generator")
st.subheader("Generate professional documents using AI")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    doc_type = st.selectbox(
        "Select Document Type",
        ["BRD", "BPD", "FD", "TD", "Custom"]
    )
    st.markdown("---")
    st.markdown("**Document Types:**")
    st.markdown("- **BRD** — Business Requirements")
    st.markdown("- **BPD** — Business Process")
    st.markdown("- **FD** — Functional Design")
    st.markdown("- **TD** — Technical Design")
    st.markdown("- **Custom** — Any Document")

# Main area
requirements = st.text_area(
    "Enter your requirements here:",
    height=200,
    placeholder="Example: Build an e-commerce platform with user login, product catalog, cart, and payment gateway..."
)

if st.button("🚀 Generate Document", type="primary"):
    if requirements.strip() == "":
        st.error("Please enter requirements first!")
    else:
        with st.spinner("AI is generating your document..."):
            # Generate content
            content = generate_document(doc_type, requirements)

        st.success("Document generated successfully!")

        # Show content
        st.markdown("## 📋 Generated Document")
        st.markdown(content)

        # Create downloadable docx
        doc = Document()
        doc.add_heading(f"{doc_type} Document", 0)
        for line in content.split('\n'):
            if line.strip():
                if line.startswith('#'):
                    doc.add_heading(line.replace('#', '').strip(), 1)
                else:
                    doc.add_paragraph(line)

        # Save to buffer
        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        # Download button
        st.download_button(
            label="📥 Download as Word Document",
            data=buffer,
            file_name=f"{doc_type}_document.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )