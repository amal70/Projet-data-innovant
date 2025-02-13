import streamlit as st # type: ignore

# Configuration de la page principale
st.set_page_config(
    page_title="Votre Impact Environnemental",
    page_icon="🚴‍♂️",
    layout="wide"
)

# 🌍 Barre latérale pour la navigation
st.sidebar.title("📌 Navigation")
st.sidebar.page_link("1_Accueil.py", label="🏠 Accueil")
st.sidebar.page_link("2_Impact_Environnemental.py", label="📊 Impact Environnemental")
st.sidebar.page_link("3_Benefices.py", label="🔍 Les Bénéfices du Vélo Mécanique")
st.sidebar.page_link("4_Sensibilisation.py", label="🌍 Sensibilisation")
st.sidebar.page_link("5_Passons_à_l'action.py", label="✅ Passons à l'action !")

# 🎯 Page d'accueil (accueil par défaut)
st.title("🚗➡️🚴‍♂️ Bienvenue sur Votre Impact Environnemental")
st.write("""
Cette application vous permet de découvrir l’impact écologique de vos choix de transport 🚲 🚗.
Explorez les données et découvrez comment réduire votre empreinte carbone ! 🌍  
Utilisez la barre latérale pour naviguer entre les sections.
""")

# Bouton pour démarrer directement
if st.button("Commencer l’analyse 🌱"):
    st.switch_page("1_Accueil.py")  # Redirige vers la page d'accueil interactive
