import streamlit as st
from fewshots import fewshot
from post_generator import generate_post

def main():
    st.set_page_config(page_title="LinkedIn Post Generator", page_icon="📱", layout="wide")
    st.markdown("<h1 style='text-align: center; color: #4CAF50;'>LinkedIn Post Generator</h1>", unsafe_allow_html=True)
    st.markdown("---")  # Horizontal line separator

    # Add some padding and space around the elements
    st.markdown("<div style='padding: 10px;'></div>", unsafe_allow_html=True)

    # Adjust column widths for a clean and spaced layout
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
    
    fs = fewshot()

    # Column 1 (Purpose): Selectbox with custom input
    with col1:
        selected_purp = st.selectbox(
            "Purpose", 
            options=fs.get_purpose() + ["Other (Custom Input)"], 
            help="Choose the purpose of the post or add your own"
        )
        if selected_purp == "Other (Custom Input)":
            selected_purp = st.text_input("Enter Custom Purpose", help="Enter the purpose of your post (e.g., Awareness, Engagement)")

    # Column 2 (Target Audience): Selectbox with custom input
    with col2:
        selected_aud = st.selectbox(
            "Target Audience", 
            options=fs.get_audience() + ["Other (Custom Input)"], 
            help="Choose the target audience or add your own"
        )
        if selected_aud == "Other (Custom Input)":
            selected_aud = st.text_input("Enter Custom Audience", help="Enter the target audience (e.g., Entrepreneurs, Students)")

    # Column 3 (Domain): Selectbox with custom input
    with col3:
        selected_dom = st.selectbox(
            "Domain", 
            options=fs.get_domain() + ["Other (Custom Input)"], 
            help="Choose the domain of the post or add your own"
        )
        if selected_dom == "Other (Custom Input)":
            selected_dom = st.text_input("Enter Custom Domain", help="Enter the domain (e.g., Technology, Health, Education)")

    # Column 4 (Title): Selectbox with custom input
    with col4:
        selected_tag = st.selectbox(
            "Title", 
            options=fs.get_tags() + ["Other (Custom Input)"], 
            help="Choose the title of the post or add your own"
        )
        if selected_tag == "Other (Custom Input)":
            selected_tag = st.text_input("Enter Custom Title", help="Enter the title of your post (e.g., Growth Hacking Tips)")

    # Column 5 (Length): Selectbox for length of the post
    with col5:
        selected_len = st.selectbox("Length", options=['Short', 'Medium', 'Long'], help="Choose the length of the post")

    # Column 6 (Language): Selectbox for language of the post
    with col6:
        selected_lang = st.selectbox("Language", options=['English', 'Hinglish'], help="Choose the language of the post")

    # Add some space between the input fields and button
    st.markdown("<div style='padding: 20px;'></div>", unsafe_allow_html=True)

    # Add a styled button to trigger post generation
    if st.button("Generate Post", key="generate_button", use_container_width=True):
        post = generate_post(selected_tag, selected_len, selected_lang, selected_purp, selected_aud, selected_dom)
        st.write(f"Here is your post for {selected_purp}, {selected_aud}, {selected_dom}, {selected_tag}, {selected_len}, {selected_lang}")
        st.success(post)

if __name__ == "__main__":
    main()
