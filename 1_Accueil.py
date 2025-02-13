import streamlit as st # type: ignore
import pandas as pd # type: ignore

# Configuration de la page
st.set_page_config(
    page_title="Mobilité Douce UGA",
    page_icon="🚲",
    layout="wide"
)
# 📌 Charger les données depuis Excel
df = pd.read_excel("data/DATA_UGA.xlsx")

# 🎯 Configuration de la page



# 📌 **Ajout des filtres dans la barre latérale**
st.sidebar.header("📌 Filtres")

# Filtre Type de personne (Affichage amélioré)
type_personne_mapping = {"ETU": "Etudiant", "PER": "Personnel"}
df["type_personne_affichage"] = df["type_personne"].map(type_personne_mapping)
type_personne_options = df["type_personne_affichage"].dropna().unique().tolist()
type_personne_selection = st.sidebar.multiselect("Vous êtes :", type_personne_options, default=type_personne_options)
type_personne_selected_values = [key for key, val in type_personne_mapping.items() if val in type_personne_selection]

# Filtre Mode de transport (Gardé uniquement dans la sidebar)
mode_transport_options = df["mode_transport"].dropna().unique().tolist()
mode_transport_selection = st.sidebar.multiselect("Vous utilisez :", mode_transport_options, default=mode_transport_options)

# Filtre Année
annee_options = df["année_saisie"].dropna().unique().tolist()
annee_selection = st.sidebar.multiselect("Année :", annee_options, default=annee_options)

# Appliquer les filtres globaux
df_filtered = df[
    (df["type_personne"].isin(type_personne_selected_values)) &
    (df["mode_transport"].isin(mode_transport_selection)) &
    (df["année_saisie"].isin(annee_selection))
]



# Appliquer un style CSS
st.markdown("""
    <style>
        /* Garder la couleur de fond actuelle */
        .stApp {
            background-color: #fff0d1 !important; /* Beige clair */
        }
        
        /* Changer uniquement le texte blanc en vert foncé */
        h1, h2, h3, h4, h5, h6 {
            color: #215E21 !important;  /* Vert foncé */
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



# Appliquer le style CSS directement dans Streamlit avec markdown
st.markdown("""
    <style>
        /* Fond général clair */
        body {
            background-color: #F5F5F5; /* Fond gris très clair pour toute la page */
            font-family: 'Roboto', sans-serif; /* Police élégante et moderne */
            color: #333; /* Texte sombre pour un bon contraste */
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }

        /* Titre principal */
        .main-title {
            font-size: 36px;
            color: #2C3E50; /* Couleur bleu foncé pour le titre */
            font-weight: 700;
            text-align: center;
            padding-top: 30px;
            margin-bottom: 40px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
        }

        /* Titre des sections */
        .section-title {
            font-size: 28px;
            color: #2C3E50;
            font-weight: 600;
            padding: 20px;
            text-align: center;
            margin-bottom: 25px;
            border-radius: 12px;
            background: linear-gradient(145deg, #FFFFFF, #F0F0F0);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Couleurs pour les sections spécifiques */
        .bike-section {
            background-color: #96ceb4; /* Vert clair pour le vélo */
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .bike-section:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .electric-bike-section {
            background-color: #ffeead; /* Vert foncé pour le vélo électrique */
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .electric-bike-section:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        .car-section {
            background-color: #ffad60; /* Rouge vif pour la voiture */
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .car-section:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }

        /* Texte de chaque section */
        .text {
            font-size: 18px;
            color: #555;  /* Gris foncé pour un contraste agréable */
            text-align: center;
            padding: 0 20px;
            line-height: 1.8;
        }

        

        /* Icônes des modes de transport */
        .icon-box {
            text-align: center;
            margin-top: 30px;
        }

        .icon {
            width: 100px;
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }

        .icon:hover {
            transform: scale(1.1);
        }

        /* Séparateurs et autres éléments */
        .separator {
            margin: 50px 0;
            border-bottom: 2px solid #BDC3C7; /* Séparateur léger */
        }

        .section-wrapper {
            padding: 25px 15px;
            margin-bottom: 40px;
            border-radius: 12px;
            background-color: #FFFFFF;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Ajouter l'image au début de la page
st.image("https://attraxcdnprod1-freshed3dgayb7c3.z01.azurefd.net/1481103/43cc2251-abc6-42a6-bf07-36e410f33bf7/2025.2.11.26450/img/67b4c57c-223c-4d2e-8335-08d9f10ce754", 
         use_container_width=True, 
         caption="UGA mobilité douce")

# Titre principal
st.markdown('<h1 class="main-title"> Objectif & Choix des Moyens de Transport</h1>', unsafe_allow_html=True)

# Introduction
st.markdown("""
Cette étude analyse les trajets domicile-campus des étudiants et personnels de l’UGA en comparant le **vélo, le vélo électrique** et la **voiture** selon leur impact environnemental.
""")

# Sections différenciées par des couleurs et icônes
col1, col2, col3 = st.columns(3)

# Vélo
with col1:
    st.markdown('<div class="bike-section">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios/452/bicycle.png", width=100)
    st.markdown('<p class="section-title" style="color:#2C3E50">🚴‍♂️ Vélo</p>', unsafe_allow_html=True)
    st.markdown('<p class="text">-Zéro émission- Écologique et économique</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Vélo Électrique
with col2:
    st.markdown('<div class="electric-bike-section">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios/452/electric-bicycle.png", width=100)
    st.markdown('<p class="section-title" style="color:#2C3E50">⚡ Vélo Électrique</p>', unsafe_allow_html=True)
    st.markdown('<p class="text">-Faible empreinte CO₂- Plus d’autonomie</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Voiture
with col3:
    st.markdown('<div class="car-section">', unsafe_allow_html=True)
    st.image("https://img.icons8.com/ios/452/car.png", width=100)
    st.markdown('<p class="section-title" style="color:#2C3E50">🚗 Voiture</p>', unsafe_allow_html=True)
    st.markdown('<p class="text">-Émet CO₂- Confort et flexibilité</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Pourquoi pas le bus ou le tram ?
st.subheader(" Pourquoi pas le bus ou le tram ?")
st.markdown("""
L'empreinte carbone des transports en commun dépend du taux d’occupation, rendant la comparaison difficile.
""")

# Pourquoi pas la marche ?
st.subheader(" Pourquoi pas la marche ?")
st.markdown("""
La marche est peu utilisée au-delà de **3-5 km**, ce qui la rend moins pertinente pour cette étude.
""")

# Conclusion
st.markdown("""
👉 **L’objectif est d’identifier des alternatives durables et réalistes pour réduire l’empreinte carbone des étudiants.**  
🌍♻️
""")

# Séparation
st.markdown('<div class="separator"></div>', unsafe_allow_html=True)


# Chemin de l'image locale (utilisez un chemin relatif ou absolu correct)
image_path = "images/1.png"  # Chemin absolu


# Afficher l'image en haut de la page
st.image(image_path, use_container_width=True)


# Introduction percutante
st.markdown("""
### 🌍 **Saviez-vous que…**  
🔹 Une voiture consomme en moyenne **65 kWh** pour 100 km, contre **seulement 0,8 kWh** pour un vélo électrique ?  
🔹 En passant au vélo, vous pouvez économiser **l’équivalent de 200 arbres plantés par an** ! 🌱  
🔹 Les voitures thermiques émettent **jusqu’à 80 fois plus de CO₂** qu’un vélo électrique ! 💨  
""")

# Bouton pour passer à l'analyse
if st.button("Passer à l’analyse 🌍"):
    st.switch_page("pages/2_Impact_Environnemental.py")  # Redirige vers la page suivante