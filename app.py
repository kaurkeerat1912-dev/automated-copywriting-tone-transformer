import streamlit as st 
from prompt import build_prompt
from generator import generate_copy
st.set_page_config(
    page_title ="Copywriting AI",
    page_icon ="🤖",
    layout="centered"
)
st.title("AUTOMATED COPYWRITNG AND TONE TRANSFORMER 🤖")
product_name = st.text_input("enter product name")
description = st.text_area("enter product description")
platform = st.selectbox(
    "select platform",
    ["instagram","linkedin","email"]
)
tone=st.selectbox(
    "select tone",
    ["professional","friendly","luxury","casual","witty"]
)
temperature=st.slider(
    "temperature",
    min_value=0.0,
    max_value=1.0,
    value=0.7,
    step=0.1
)
generate = st.button("Generate copy")
if generate:
    prompt = build_prompt(
        product_name,
        description,
        platform,
        tone,
        temperature
    )
    output = generate_copy(prompt, temperature)
    st.subheader("Generated Marketing Copy")
    st.write(output)