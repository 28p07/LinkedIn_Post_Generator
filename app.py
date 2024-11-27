import streamlit as st
from fewshots import fewshot
from post_generator import generate_post

def main():
    st.title("LinkedIN Post Generator")

    col1,col2,col3 = st.columns(3)
    fs = fewshot()
    with col1:
        selected_tag = st.selectbox("Title",options=fs.get_tags())
    with col2:
        selected_len = st.selectbox("Length",options =['Short','Medium','Long'])
    with col3:
        selected_lang = st.selectbox("Language",options=['English','Hinglish'])

    if st.button("Generate"):
        post = generate_post(selected_tag,selected_len,selected_lang)
        st.write(f"Generated post for {selected_tag}, {selected_len}, {selected_lang}")
        st.success(post)

if __name__=="__main__":
    main()
