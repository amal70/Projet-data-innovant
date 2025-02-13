import streamlit as st # type: ignore
import pandas as pd # type: ignore
from streamlit_echarts import st_echarts # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
import numpy as np # type: ignore

# Configuration de la page
st.set_page_config(
    page_title="Mobilité Douce UGA",
    page_icon="🚲",
    layout="wide"
)

# Appliquer un fond de couleur avec du CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #fff0d1 !important; /* Vert foncé */
        }
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

# 📌 Charger les données depuis Excel
df = pd.read_excel("data/DATA_UGA.xlsx")

# 🎯 Configuration de la page
image_path = "images/4.png"  # Chemin absolu
st.image(image_path, use_container_width=True)


###### KPI1
#import streamlit as st
import pandas as pd # type: ignore
from streamlit_echarts import st_echarts # type: ignore

# 📊 **Calories brûlées par 100 km**
st.subheader("Calories brûlées par 10 km")

# Données
data = {
    "Mode de transport": ["Vélo Classique", "Vélo Électrique", "Voiture"],
    "Calories brûlées": [500, 150, 0]
}
df = pd.DataFrame(data)

# Configuration du graphique ECharts
options = {
    "title": {
        "text": "Calories brûlées par mode de transport",
        "left": "center",
        "textStyle": {"fontSize": 18}
    },
    "tooltip": {"trigger": "axis"},
    "xAxis": {
        "type": "category",
        "data": df["Mode de transport"].tolist(),
        "axisLabel": {"rotate": 15}  # Incline les étiquettes si besoin
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "Calories brûlées",
            "type": "bar",
            "data": df["Calories brûlées"].tolist(),
            "itemStyle": {
                "color": {
                    "type": "linear",
                    "x": 0, "y": 0, "x2": 0, "y2": 1,
                    "colorStops": [
                        {"offset": 0, "color": "#2ECC71"},  # Vert pour le vélo classique
                        {"offset": 0.5, "color": "#F39C12"},  # Orange pour vélo électrique
                        {"offset": 1, "color": "#E74C3C"}   # Rouge pour voiture
                    ]
                },
                "barBorderRadius": [6, 6, 0, 0]  # Bords arrondis en haut
            }
        }
    ]
}

# 📊 Affichage du graphique
st_echarts(options=options, height="400px")
st.markdown(
    """
    <div style="text-align: right; font-size: 0.8em; color: black;">
        <i><a href="https://www.canyon.com/fr-fr/blog-content/conseils/bruler-calories-perdre-poids-vae/b21122021.html" target="_blank" style="color: black; text-decoration: none;">
        https://www.canyon.com/fr-fr/blog-content/conseils/bruler-calories-perdre-poids-vae/b21122021.html
        </a></i>
    </div>
    """,
    unsafe_allow_html=True
)




################







# 📊 **Niveau de Stress par Mode de Transport**
st.subheader("Niveau de Stress par Mode de Transport")

# Données des niveaux de stress
df_stress = pd.DataFrame({
    "Mode de transport": ["Vélo Classique", "Vélo Électrique", "Voiture"],
    "Niveau de Stress": [2, 4, 8]  # 1 = Très Bas, 10 = Très Haut
})

# Conversion explicite en int natif pour éviter l'erreur JSON
df_stress["Niveau de Stress"] = df_stress["Niveau de Stress"].astype(int)

# Définition des couleurs fixes pour chaque mode de transport
colors = ["#2ECC71", "#F39C12", "#E74C3C"]  # Vert, Orange, Rouge

# 📊 **Graphique en barres horizontales**
options = {
    "title": {
        "text": "Niveau de Stress par Mode de Transport",
        "left": "center",
        "textStyle": {"fontSize": 18}
    },
    "tooltip": {"trigger": "axis"},
    "xAxis": {
        "type": "value",
        "name": "Niveau de Stress",
        "max": 10,
        "min": 0
    },
    "yAxis": {
        "type": "category",
        "data": df_stress["Mode de transport"].tolist()
    },
    "series": [
        {
            "name": "Niveau de Stress",
            "type": "bar",
            "data": [
                {"value": int(df_stress["Niveau de Stress"].iloc[i]), "itemStyle": {"color": colors[i]}}
                for i in range(len(df_stress))
            ],
            "label": {"show": True, "position": "insideRight"},
            "itemStyle": {"borderRadius": [5, 5, 5, 5]}
        }
    ]
}

# Afficher le graphique interactif ECharts
st_echarts(options=options, height="400px")
st.markdown(
    """
    <div style="text-align: right; font-size: 0.8em; color: black;">
        <i><a href="https://www.ornikar.com/code/cours/conducteur/psychologique/peur-stress-volant#:~:text=27%20%25%20des%20conducteurs%20fran%C3%A7ais%20sont,m%C3%A9rites%20des%20assistants%20%C3%A0%20la" target="_blank" style="color: black; text-decoration: none;">
        https://www.ornikar.com/code/cours/conducteur/psychologique/peur-stress-volant#:~:text=27%20%25%20des%20conducteurs%20fran%C3%A7ais%20sont,m%C3%A9rites%20des%20assistants%20%C3%A0%20la
        </a></i>
    </div>
    """,
    unsafe_allow_html=True
)

# 📝 **Ajout d'un texte explicatif**
st.markdown("""
### **Interprétation des niveaux de stress :**  
🟢 **Vélo Classique (2/10)** → Très faible stress, liberté de mouvement et pas d’embouteillage.   
🟠 **Vélo Électrique (4/10)** → Un peu plus de stress (partage de la route, vitesse).   
🔴 **Voiture (8/10)** → Très stressant (trafic, stationnement, coûts élevés).   

💡 Moins on utilise la voiture, plus le niveau de stress diminue !  
""")

















import streamlit as st # type: ignore
from streamlit_echarts import st_echarts # type: ignore

# Données des différents modes de transport
modes_de_transport = ["Voiture essence", "Voiture diésel", "Vélo electrique", "Vélo normal"]
cout_annuel = [6063, 6063, 500, 741, 650]

# Définir les options pour le graphique en barres
options = {
    "xAxis": {
        "type": "category",
        "data": modes_de_transport,  # Utilisation des modes de transport comme catégories sur l'axe X
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "data": [{"value": val, "itemStyle": {"color": "#1E88E5"}} if val <= 1000 else {"value": val, "itemStyle": {"color": "#D32F2F"}} for val in cout_annuel],
            "type": "bar",
        }
    ],
}

# Affichage du graphique
st.markdown("### **Frais d'entretien annuel des différents modes de transport**")
st_echarts(options=options, height="400px")



st.markdown(
    """
    <div style="text-align: right; font-size: 0.8em; color: black;">
        <i><a href="https://pro.mobicoop.fr/cout-utilisation-voiture/#:~:text=6%20063%E2%82%AC.,du%20budget%20d'un%20m%C3%A9nage🚴‍♂️🚗" target="_blank" style="color: black; text-decoration: none;">
        https://pro.mobicoop.fr/cout-utilisation-voiture/#:~:text=6%20063%E2%82%AC.,du%20budget%20d'un%20m%C3%A9nage🚴‍♂️🚗
        </a></i>
    </div>
    """,
    unsafe_allow_html=True
)

# Message incitant à la réflexion
st.markdown("""
    **Le coût du transport peut rapidement augmenter.**
    Choisissez des modes de transport plus économiques pour réduire vos dépenses et votre empreinte carbone. 🌍🚴‍♂️🚗
""")


# Message incitant à la réflexion

st.markdown("---")

# 📢 **Message engageant**
st.info("🌱 Chaque choix compte ! Pensez à l’impact de votre moyen de transport sur l’environnement. Adoptez des habitudes plus durables !")

# 🔜 Bouton pour continuer vers la page suivante
if st.button("Explorer les impacts visuels 🌍"):
    st.switch_page("pages/4_Sensibilisation.py")
