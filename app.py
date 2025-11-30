import streamlit as st
from llm_module import load_llm, generate_blog
from utils import validate_input, clean_text, save_blog_to_file
import os
import io


# Streamlit UI setup
st.set_page_config(page_title="Blog Generator", page_icon="✍", layout='centered')
st.title("✍ AI Blog Generator")
st.markdown("Generate high-quality blogs for different job profiles using Llama 2 Chat 7B.")


# Sidebar Settings
with st.sidebar:
    st.header("Settings")
    max_tokens = st.slider("Max words per blog", 100, 1000, 256, 50)
    temperature = st.slider("Creativity (Temperature)", 0.0, 1.0, 0.01, 0.01)
    gpu_layers = st.slider("GPU layers (for speed)", 0, 50, 50, 1)


# Load model (once)
llm = load_llm(gpu_layers=gpu_layers, max_tokens=max_tokens, temperature=temperature)


# User Inputs
input_text = st.text_input("Enter the blog topic")

col1, col2 = st.columns([5,5])
with col1:
    no_of_words = st.text_input("Number of words", "300")
with col2:
    blog_style = st.selectbox("Target audience", ('Researchers', 'Data Scientist', 'Common People'))


# Generate Blog
# if st.button("Generate Blog"):
#     valid, msg = validate_input(input_text, no_of_words)
#     if not valid:
#         st.warning(msg)
#     else:
#         with st.spinner("Generating blog..."):
#             response = generate_blog(llm, input_text, no_of_words, blog_style)
#             response = clean_text(response)
#             st.text_area("Generated Blog", value=response, height=400)

#             # Save option
#             save_path = save_blog_to_file(response)
#             st.success(f"Blog saved to: {save_path}")

#             # Download button
#             with open(save_path, "rb") as f:
#                 st.download_button(
#                     label="Download Blog as TXT",
#                     data=f,
#                     file_name=os.path.basename(save_path),
#                     mime="text/plain"
#                 )

if st.button("Generate Blog"):
    valid, msg = validate_input(input_text, no_of_words)
    if not valid:
        st.warning(msg)
    else:
        with st.spinner("Generating blog..."):
            response = generate_blog(llm, input_text, no_of_words, blog_style)
            response = clean_text(response)
            st.text_area("Generated Blog", value=response, height=400)

            # Download Blog as TXT (in-memory)
            blog_filename = f"{blog_style}_{input_text[:20].replace(' ', '_')}.txt"
            blog_bytes = io.BytesIO(response.encode("utf-8"))

            if st.download_button(
                label="Download Blog as TXT",
                data=blog_bytes,
                file_name=blog_filename,
                mime="text/plain"
            ):
                # Optional: save to disk when download is clicked
                output_dir = "generated_blogs"
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                save_path = os.path.join(output_dir, blog_filename)
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(response)
                st.success(f"Blog saved to: {save_path}")


