import streamlit as st
from fewshots import FewShotPosts
from post_generator import generate_post

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]


def main():
    st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")

    st.markdown(
        "<h2 style='text-align: center; margin-bottom: 0;'>LinkedIn Post Generator</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; color: gray; font-size: 0.9em;'>Generate clean, relevant LinkedIn posts in one click.</p>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    fs = FewShotPosts()
    tags = fs.get_tags()

    with st.form(key="post_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            selected_tag = st.selectbox("Topic", options=tags)

        with col2:
            selected_length = st.selectbox("Length", options=length_options)

        with col3:
            selected_language = st.selectbox("Language", options=language_options)

        submit = st.form_submit_button("Generate")

    if submit:
        with st.spinner("Generating..."):
            post = generate_post(selected_length, selected_language, selected_tag)

        st.markdown("---")
        st.markdown("#### Your Post")
        st.text_area("Post Output", value=post.strip(), height=220, label_visibility="collapsed")
        st.markdown("---")

    st.markdown(
        "<p style='text-align: center; color: lightgray; font-size: 0.8em;'>© 2025 - Minimal by design</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
