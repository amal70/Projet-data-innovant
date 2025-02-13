import streamlit as st # type: ignore
import pandas as pd # type: ignore
from streamlit_echarts import st_echarts # type: ignore

# Configuration de la page
st.set_page_config(
    page_title="Mobilité Douce UGA",
    page_icon="🚲",
    layout="wide"
)

# Appliquer un fond de couleur avec du CSS
st.markdown("""
    <style>
        /* Modifier la couleur de fond de la page entière */
        .stApp {
            background-color: #fff0d1 !important; /* Vert foncé */
        }
        
        /* Optionnel : Changer la couleur du texte pour améliorer la visibilité */
        .stMarkdown, .stTextInput, .stButton {
            color: #555 !important; /* Texte blanc */
        }
              /* Boutons */
.button {
    background-color: #3498DB; /* Bleu clair pour le bouton */
    color: white;
    padding: 15px 35px;
    border-radius: 30px;
    font-size: 20px;
    display: block;
    margin: 40px auto;
    width: 60%;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease, transform 0.3s ease;
    border: none;
    cursor: pointer;
}

.button:hover {
    background-color: #2980B9; /* Bleu foncé au survol */
    transform: translateY(-3px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
}

/* Style spécifique pour les boutons Streamlit */
.stButton>button {
    background-color: #3498DB !important; /* Bleu clair */
    color: white !important; /* Texte en blanc */
    padding: 12px 30px !important;
    border-radius: 30px !important;
    font-size: 18px !important;
    border: none !important;
    cursor: pointer !important;
    transition: background-color 0.3s ease, transform 0.3s ease !important;
}

.stButton>button:hover {
    background-color: #2980B9 !important; /* Bleu foncé */
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2) !important;
}
    </style>
""", unsafe_allow_html=True)

# 📌 Charger les données du questionnaire
df_reponses = pd.read_excel("data/Réponses_par_années.xlsx")

# 🎯 Configuration de la page
st.title("✅ Appel à l’Action")

# 📢 **Message motivant**
st.markdown("""
### 🌍 **Chaque choix compte !**
En partageant vos **habitudes de transport**, vous aidez à **enrichir les données** et à **améliorer les analyses**. 🚀  
**Plus nous avons de réponses, plus l’impact sera visible !**
""")

st.markdown("---")

# 📊 **Graphique interactif : Nombre de réponses par année**
st.subheader("📈 Évolution des réponses au questionnaire UGA")

df_reponses_grouped = df_reponses.groupby("année_saisie")["n_obs"].sum()

# 🔥 Graphique interactif avec `streamlit-echarts`
line_chart_options = {
    "xAxis": {"type": "category", "data": df_reponses_grouped.index.tolist()},
    "yAxis": {"type": "value", "name": "Nombre de réponses"},
    "series": [{"data": df_reponses_grouped.tolist(), "type": "line", "color": "#007BFF"}],
}

st_echarts(options=line_chart_options, height="400px")

import streamlit as st
from streamlit_echarts import st_echarts

# Titre principal
st.title("Appel à l'Action - Participez au Questionnaire")

# Affichage du nombre d'étudiants en grand pour choquer
st.markdown("### **57 000 Étudiants à l'UGA**")
st.markdown("#### **Un potentiel incroyable... mais...**")

# Pause avant d'afficher les autres informations pour créer l'effet
import time
time.sleep(1)

# Affichage du nombre de participants chaque année avec une animation
st.markdown("### **Et voici combien ont réellement répondu...**")

# Données pour les camemberts
participants_2023 = 3282
participants_2024 = 4867
participants_2025 = 558
total_etudiants = 57000

# Créer un camembert pour chaque année
options_2023 = {
    "tooltip": {"trigger": "item"},
    "legend": {"top": "5%", "left": "center"},
    "series": [
        {
            "name": "Réponses 2023",
            "type": "pie",
            "radius": ["40%", "70%"],
            "avoidLabelOverlap": False,
            "itemStyle": {
                "borderRadius": 10,
                "borderColor": "#fff",
                "borderWidth": 2,
            },
            "label": {"show": False, "position": "center"},
            "emphasis": {
                "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
            },
            "labelLine": {"show": False},
            "data": [
                {"value": participants_2023, "name": f"Répondus ({participants_2023})"},
                {"value": total_etudiants - participants_2023, "name": f"Non répondus ({total_etudiants - participants_2023})"},
            ],
        }
    ],
}

options_2024 = {
    "tooltip": {"trigger": "item"},
    "legend": {"top": "5%", "left": "center"},
    "series": [
        {
            "name": "Réponses 2024",
            "type": "pie",
            "radius": ["40%", "70%"],
            "avoidLabelOverlap": False,
            "itemStyle": {
                "borderRadius": 10,
                "borderColor": "#fff",
                "borderWidth": 2,
            },
            "label": {"show": False, "position": "center"},
            "emphasis": {
                "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
            },
            "labelLine": {"show": False},
            "data": [
                {"value": participants_2024, "name": f"Répondus ({participants_2024})"},
                {"value": total_etudiants - participants_2024, "name": f"Non répondus ({total_etudiants - participants_2024})"},
            ],
        }
    ],
}

options_2025 = {
    "tooltip": {"trigger": "item"},
    "legend": {"top": "5%", "left": "center"},
    "series": [
        {
            "name": "Réponses 2025",
            "type": "pie",
            "radius": ["40%", "70%"],
            "avoidLabelOverlap": False,
            "itemStyle": {
                "borderRadius": 10,
                "borderColor": "#fff",
                "borderWidth": 2,
            },
            "label": {"show": False, "position": "center"},
            "emphasis": {
                "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
            },
            "labelLine": {"show": False},
            "data": [
                {"value": participants_2025, "name": f"Répondus ({participants_2025})"},
                {"value": total_etudiants - participants_2025, "name": f"Non répondus ({total_etudiants - participants_2025})"},
            ],
        }
    ],
}

# Affichage des camemberts pour chaque année
st_echarts(options=options_2023, height="500px")
st_echarts(options=options_2024, height="500px")
st_echarts(options=options_2025, height="500px")

st.markdown("---")

# 📌 **Bouton vers le questionnaire UGA**
st.subheader("📝 Participez à l'étude UGA")
st.write("Cliquez ci-dessous pour répondre au questionnaire et contribuer aux analyses environnementales !")

if st.button("📋 Répondre au questionnaire UGA"):
    st.markdown("[Cliquez ici pour accéder au questionnaire UGA](https://www.uga.fr)")

st.markdown("---")

# 🔜 Bouton pour retourner à l’accueil
if st.button("🏠 Retour à l'accueil"):
    st.switch_page("pages/1_Accueil.py")
