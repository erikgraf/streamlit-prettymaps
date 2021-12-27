import streamlit as st
import prettymaps
from matplotlib import pyplot as plt
import json



st.title("🌇 Artsymaps")

st.write("")

ex1, ex2, ex3, ex4, ex5 = st.columns(5)
ex1.image("./prints/macao.png")
button_ex1 = ex1.button("Macau")
ex2.image("./prints/palmanova.png")
button_ex2 = ex2.button("Palma Nova")
ex3.image("./prints/barcelona.png")
button_ex3 = ex3.button("Barcelona")
ex4.image("./prints/erbil.png")
button_ex4 = ex4.button("Erbil")
ex5.image("./prints/bomfim-farroupilha-cidadebaixa.png")
button_ex5 = ex5.button("Cidadebaixa")


st.write("")
form = st.form(key="form_params")
form.markdown("**Or select your own location & style**")
col1, col2, col3 = form.columns([1.5,1, 0.5])

address = col1.text_input(
    "Enter address or location", "Praça Ferreira do Amaral, Macau" #"Matthias-Ehrenfried-Str. 16, 97074, Wuerzburg"
)
radius = col1.slider("Select radius", 1, 1500, 1100)

style = col2.selectbox("Select style", ["1", "2", "3"])

expander = col2.expander("More styling options")
expander.checkbox("Add location name", True)
expander.checkbox("Add coordinates")
expander.color_picker("Background color")

submit_button = form.form_submit_button(label='Submit')

st.markdown("---")

if submit_button:
    with open(f'./styles/{style}.json') as f:
        style_json = json.load(f)

    fig, ax = plt.subplots(figsize=(12, 12), constrained_layout=True)

    with st.spinner("Creating new map..."):
        prettymaps.plot(
            address, radius=radius, ax=ax, layers=style_json["layers"], drawing_kwargs=style_json["drawing_kwargs"]
        )
        st.pyplot(fig)

elif any([button_ex1, button_ex2, button_ex3, button_ex4, button_ex5]):
    if button_ex1:
        st.image("./prints/macao.png")
        st.write("Macau")
    elif button_ex2:
        st.image("./prints/palmanova.png")
        st.write("Palma Nova")

else:
    st.image("./prints/erbil.png")
    st.write("Macau")
