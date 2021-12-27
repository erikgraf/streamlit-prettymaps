import streamlit as st
import prettymaps
from matplotlib import pyplot as plt
import json


form = st.form(key="form_params")
address = form.text_input(
    "Enter address or location", "Praça Ferreira do Amaral, Macau" #"Matthias-Ehrenfried-Str. 16, 97074, Wuerzburg"
)
radius = form.slider("Select radius", 1, 1500, 1100)

style = form.slider("Select style", 1, 3, 1)

submit_button = form.form_submit_button(label='Submit')


if submit_button:
    with open(f'./styles/{style}.json') as f:
        style_json = json.load(f)


    fig, ax = plt.subplots(figsize=(12, 12), constrained_layout=True)
    prettymaps.plot(
        address, radius=radius, ax=ax, layers=style_json["layers"], drawing_kwargs=style_json["drawing_kwargs"]
    )

    st.pyplot(fig)
