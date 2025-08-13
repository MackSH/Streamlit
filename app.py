import streamlit as st
import pandas as pd

# Titres et texte
st.title("Titre principal")
st.header("En-tête")
st.subheader("Sous-en-tête")
st.text("Texte simple")
st.markdown("**Texte en gras** avec *markdown*")

# Affichage de données
df = pd.DataFrame({
    'col1': [1, 2, 3, 4, 5, 6],
    'col2': [10, 20, 30, 40, 50, 60]
})
st.dataframe(df)
st.table(df)  # Table statique


import matplotlib.pyplot as plt
import plotly.express as px

# Matplotlib
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
st.pyplot(fig)

# Plotly (interactif)
fig = px.line(x=[1, 2, 3, 4], y=[1, 4, 2, 3])
st.plotly_chart(fig)

# Graphiques simples intégrés
st.line_chart(df)
st.bar_chart(df)

# Boutons
if st.button("Cliquez-moi"):
    st.write("Bouton cliqué!")

# Cases à cocher
checkbox = st.checkbox("Cochez-moi")
if checkbox:
    st.write("Case cochée!")

# Sélecteurs
option = st.selectbox(
    "Choisissez une option",
    ["Option 1", "Option 2", "Option 3"]
)
st.write(f"Vous avez choisi : {option}")

# Multi-sélection
options = st.multiselect(
    "Choisissez plusieurs options",
    ["A", "B", "C", "D"],
    ["A", "C"]  # valeurs par défaut
)

# Curseurs
age = st.slider("Sélectionnez votre âge", 0, 100, 25)
st.write(f"Votre âge : {age} ans")

# Champs de texte
name = st.text_input("Entrez votre nom")
message = st.text_area("Votre message")

# Upload de fichiers
uploaded_file = st.file_uploader("Choisissez un fichier", type=['csv', 'txt'])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)