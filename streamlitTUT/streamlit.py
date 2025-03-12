import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello World")
x = st.text_input("Favorite Movie")
st.write("Your favorite movie is", x)
st.write(f"The movie: {x} is a great movie")


is_clicked = st.button("Click me")

# markdown formatting
st.write("### Markdown")
st.write("```sh\n$ pip install streamlit\n```")
st.write("highlighting code: `print('Hello World')`")
st.write("highlight text: ")
st.write("Latex: $$\int_0^\infty x^2 dx$$")

# Displaying data
# data = pd.read_csv("data.csv")
# st.write(data)

# chart data
st.write("### `My Cool Chart`")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.bar_chart(chart_data)
st.line_chart(chart_data)


### pages
"""
project
|
|--- streamlit.py
|--- pages
     |--- 1_home.py
     |--- 2_about.py
     |--- 3_contact.py

"""