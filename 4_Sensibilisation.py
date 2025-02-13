import streamlit as st # type: ignore
import time
from streamlit_echarts import st_echarts # type: ignore
import pandas as pd # type: ignore
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

# 🎯 Configuration de la page
# Chemin de l'image locale (utilisez un chemin relatif ou absolu correct)
image_path = "images/5.png"  # Chemin absolu


# Afficher l'image en haut de la page
st.image(image_path, use_container_width=True)

st.markdown("---")

###KPI ----------------------------------------------------------------
# 📌 Charger les données depuis Excel
df = pd.read_excel("data/DATA_UGA.xlsx")

# Filtrer uniquement les 3 modes de transport (Vélo, Vélo électrique, Voiture)
df_filtered = df[df["mode_transport"].isin(["Vélo", "Vélo électrique", "Voiture"])]

# Regrouper les émissions de CO2 actuelles
df_co2_now = df_filtered.groupby("mode_transport")["CO2_total_kg"].sum()

# Estimer les émissions dans 10 ans (ex: +20% de croissance, à adapter si nécessaire)
df_co2_future = df_co2_now * 1.2

#----







# 📌 Calcul des indicateurs
arbres_non_sauves_total = int(df["arbres_equivalents_10ans"].sum())
co2_voiture = int(df[df["mode_transport"] == "Voiture"]["CO2_total_10ans"].sum())
co2_vae = int(df[df["mode_transport"] == "Vélo électrique"]["CO2_total_10ans"].sum())

# 📌 CSS pour améliorer le design
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

.big-title {
    font-size: 50px;
    font-weight: bold;
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    color: #1A5276;
}

.count-container {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    font-family: 'Montserrat', sans-serif;
}

.red { color: #E74C3C; }
.green { color: #27AE60; }
.grey-box {
    background-color: #F2F3F4;
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.why-important {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    color: #1A5276;
    padding-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# 📌 Titre principal
st.markdown('<p class="big-title">🚲 Impact Environnemental de Nos Déplacements 🌍</p>', unsafe_allow_html=True)

# 📌 Affichage des valeurs sans animation
st.markdown(f"""
<div class="grey-box">
    <p class="count-container red">🌳 <b>{arbres_non_sauves_total:,.0f}</b> arbres détruits en 10 ans !</p>
    <p class="count-container red">🚗 <b>{co2_voiture:,.0f} kg</b> de CO₂ émis par la voiture</p>
    <p class="count-container green">🚴‍♂️ 0 kg de CO₂ avec le vélo 💚</p>
</div>
""", unsafe_allow_html=True)

# 📌 Message final plus impactant
st.markdown("""
<p class="why-important">🌱 Pourquoi c'est grave ?</p>
<p style="text-align: center; font-size: 20px;">
Chaque trajet en voiture plutôt qu'à vélo <b>fait disparaître des arbres</b> et contribue au réchauffement climatique.  
Un <b>simple choix quotidien</b> peut faire la différence. 🌍💚
</p>
""", unsafe_allow_html=True)

st.markdown("---")

###KP2 ----------------------------------------------------------------

# 📌 Recalculer les valeurs pour une échelle de 10 km
distance_moyenne = df.groupby("mode_transport")[["vélo_km", "VAE_km", "voiture_km"]].sum().sum(axis=1)

# Regrouper les émissions et économies totales
df_co2_total = df.groupby("mode_transport")[["CO2_total_kg", "economie_CO2_velo"]].sum()

# Ramener toutes les valeurs à **une échelle de 10 km**
df_co2_10km = df_co2_total.div(distance_moyenne, axis=0) * 10

# Assurer que les 3 modes sont bien présents
df_co2_10km = df_co2_10km.reindex(["Vélo", "Vélo électrique", "Voiture"], fill_value=0)

# 🔹 Arrondir les valeurs à 2 chiffres après la virgule directement en Python
df_co2_10km = df_co2_10km.round(2)

# Extraire les valeurs pour le Tornado Chart
co2_emis_total = df_co2_10km["CO2_total_kg"].tolist()
co2_economisable_total = [-x for x in df_co2_10km["economie_CO2_velo"].tolist()]  # Valeurs négatives pour alignement

# 🔹 Tornado Chart - Comparaison des émissions actuelles vs économies ramenées à 10 km
tornado_chart_options = {
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {"type": "shadow"}
    },
    "legend": {
        "data": ["CO₂ Émis (kg/10 km)", "CO₂ Économisable (kg/10 km)"],
        "top": "5%",
        "left": "center"
    },
    "grid": {"left": "10%", "right": "10%", "bottom": "10%", "containLabel": True},
    "xAxis": {
        "type": "value",
        "splitLine": {"show": False},
        "name": "kg CO₂/10 km",
        "nameLocation": "middle",
        "nameGap": 25
    },
    "yAxis": {
        "type": "category",
        "data": ["Vélo", "Vélo électrique", "Voiture"],
        "axisLabel": {"fontWeight": "bold"}
    },
    "series": [
        {
            "name": "CO₂ Émis (kg/10 km)",
            "type": "bar",
            "stack": "total",
            "data": co2_emis_total,
            "itemStyle": {"color": "#E63946"}  # Rouge vif (danger)
        },
        {
            "name": "CO₂ Économisable (kg/10 km)",
            "type": "bar",
            "stack": "total",
            "data": co2_economisable_total,
            "itemStyle": {"color": "#2ECC71"}  # Vert profond (positif)
        }
    ]
}

# 📌 Affichage du titre et message de sensibilisation
st.markdown("""
## Impact du Mode de Transport sur le CO₂ 🌍

Chaque choix compte : **Émettez ou Économisez du CO₂ !**  
La voiture pollue bien plus qu'on ne le pense... 🚗💨

---
""")

# 📌 Affichage du Tornado Chart
st_echarts(options=tornado_chart_options, height="500px") # type: ignore

# 📌 Ajout d'un message final
st.markdown("""
### 🌱 Agissez dès aujourd’hui !  
🚲 **Opter pour le vélo, c’est économiser du CO₂ et protéger notre planète.**  
📉 **Moins de voitures = moins d’arbres détruits et moins de pollution.**  
🌍 **Un simple choix quotidien peut faire une énorme différence !**
""")


#######FIN KP2


















import streamlit as st # type: ignore

# Titre de la page
st.title("🌱 Votre impact environnemental avec le vélo")

# Constantes pour les calculs
CO2_PER_KM = 0.1  # Exemple : 0.1 kg de CO₂ économisé par km
DAILY_IMPACT = 0.5  # Impact quotidien supplémentaire (en kg de CO₂)
TREE_SMALL = 20   # 20 kg de CO₂ pour un petit arbre
TREE_LARGE = 100  # 100 kg de CO₂ pour un grand arbre

# Entrées utilisateur
st.subheader("🚴‍♂️ Entrez vos données")
km = st.number_input("Combien de kilomètres avez-vous parcourus ?", min_value=0, value=10)
days = st.number_input("Combien de jours avez-vous roulé ?", min_value=0, value=7)

# Calcul des réductions de CO₂
total_co2 = (km * CO2_PER_KM) + (days * DAILY_IMPACT)  # Total de CO₂ économisé
small_trees = total_co2 / TREE_SMALL  # Nombre de petits arbres
large_trees = total_co2 / TREE_LARGE  # Nombre de grands arbres

# Affichage des résultats
st.subheader("📊 Résultats")
st.write(f"Vous avez économisé **{total_co2:.2f} kg de CO₂** en {days} jours !")

# Sélection de l'image de l'arbre en fonction de la progression
if large_trees >= 1:
    tree_image = "images/tree_large.png"  # Grand arbre
    st.write("🌳 Vous avez fait pousser un grand arbre !")
elif small_trees >= 1:
    tree_image = "images/tree_medium.png"  # Arbre moyen
    st.write("🌿 Vous avez fait pousser un petit arbre !")
else:
    tree_image = "images/tree_small.png"  # Petit arbre
    st.write("🌱 Vous êtes sur la bonne voie pour faire pousser un arbre !")

# 创建一个空的占位符来模拟居中对齐
col1, col2, col3 = st.columns([1, 2, 1])  # 调整列的宽度，确保图片在中间

with col2:  # 把图片放在中间列
    st.image(tree_image, width=350, use_container_width=False, clamp=True)

# Barre de progression personnalisée
st.subheader("🌱 Progression de la croissance des arbres")

# Calcul de la progression
progress_small = min(small_trees, 1)  # Limite à 1 petit arbre
progress_large = large_trees  # Nombre de grands arbres

# Affichage de la progression avec des icônes et des couleurs
st.markdown("### Petit arbre 🌱")
st.markdown(
    f"""
    <div style="background-color: #f0f0f0; border-radius: 10px; padding: 10px;">
        <div style="background-color: #4CAF50; width: {progress_small * 100}%; border-radius: 10px; padding: 10px; text-align: center; color: white;">
            {progress_small * 100:.1f}%
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("### Grand arbre 🌳")
st.markdown(
    f"""
    <div style="background-color: #f0f0f0; border-radius: 10px; padding: 10px;">
        <div style="background-color: #27AE60; width: {progress_large * 100}%; border-radius: 10px; padding: 10px; text-align: center; color: white;">
            {progress_large * 100:.1f}%
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Message engageant
st.info("💡 Saviez-vous que chaque kilomètre parcouru à vélo contribue à réduire votre empreinte carbone ? Continuez comme ça ! 🌍")
# 🔜 Bouton pour continuer vers la page suivante
if st.button("Passer à l’action ✅"):
    st.switch_page("pages/5_Appel_Action.py")

