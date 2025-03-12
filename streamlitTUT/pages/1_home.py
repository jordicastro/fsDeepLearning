import streamlit as st

st.write("# Home")

st.link_button("About", "about")
st.link_button("Contact", url="contact")
st.link_button("Profile", "/profile?id=1234")