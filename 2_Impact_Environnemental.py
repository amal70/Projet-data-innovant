import streamlit as st # type: ignore
import pandas as pd # type: ignore
from streamlit_echarts import st_echarts # type: ignore
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

color_mapping = {
    "Vélo": "#96ceb4",  # 绿色
    "Vélo Électrique": "#ffeead",  # 黄色
    "Voiture": "#ffad60"  # 橙色
}


# 📌 **Ajout des filtres dans la barre latérale**
st.sidebar.header("📌 Filtres")
# CSS pour personnaliser la couleur des filtres (multiselect)
st.markdown(
    """
    <style>
        /* Changer la couleur des options sélectionnées */
        div[data-baseweb="tag"] {
            background-color: #A2CCB6 !important; /* Vert pastel */
            color: black !important;
            border-radius: 10px;
            padding: 5px 10px;
        }

        /* Modifier la couleur du texte à l'intérieur des filtres */
        div[data-baseweb="tag"] span {
            color: black !important;
            font-weight: bold;
        }

        /* Modifier la couleur de l'icône de fermeture (croix X) */
        div[data-baseweb="tag"] svg {
            fill: #132F20 !important; /* Vert foncé */
        }

        /* Modifier la couleur de fond de la liste déroulante */
        ul[data-testid="stMultiSelect"] {
            background-color: #FCEEB5 !important; /* Jaune pastel */
            border-radius: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


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


# Appliquer un fond de couleur avec du CSS
st.markdown("""
    <style>
        /* Modifier la couleur de fond de la page entière */
        .stApp {
            background-color: #fff0d1 !important; /* Vert foncé */
        }
        
        /* Optionnel : Changer la couleur du texte pour améliorer la visibilité */
        .stMarkdown, .stTextInput, .stButton {
            color: white !important; /* Texte blanc */
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

# Chemin de l'image locale (utilisez un chemin relatif ou absolu correct)
image_path = "images/3.png"  # Chemin absolu

# Afficher l'image en haut de la page
st.image(image_path, use_container_width=True)

# Appliquer le style CSS
st.markdown("""
    <style>
        /* Style général pour la page */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f8f9fa;
        }

        /* Style pour les indicateurs KPI */
        .kpi-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin: 10px;
            border: 1px solid #e0e0e0;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .kpi-box:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        }
        .kpi-box h3 {
            font-size: 18px;
            color: #2c3e50;
            margin-bottom: 10px;
            font-weight: 600;
        }
        .kpi-box p {
            font-size: 24px;
            font-weight: bold;
            color: #FFFFFF;
            margin: 0;
        }

        /* Style pour les graphiques */
        .chart-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            border: 1px solid #e0e0e0;
        }

        /* Style pour le message engageant */
        .info-box {
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            border: 1px solid #90caf9;
        }

        /* Style pour les titres */
        h1, h2, h3 {
            color: #2c3e50;
        }
    </style>
""", unsafe_allow_html=True)

# 🔹 **KPI dynamiques**

# 📌 Appliquer les filtres aux KPI
df_filtered_kpi = df_filtered  # On applique les filtres définis précédemment

# Recalculer les KPI après filtrage
kpi_consommation = df_filtered_kpi["consommation_kWh"].sum()
kpi_co2_total = df_filtered_kpi["CO2_total_tonnes"].sum()
kpi_arbres_compenses = df_filtered_kpi["arbres_equivalents"].sum()

# 🔹 **KPI dynamiques**
st.markdown("## 🔹 **KPI dynamiques**")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class="kpi-box" style="background-color: #7FC97F;">
            <h3>🔋 Consommation d’énergie (kWh)</h3>
            <p>{kpi_consommation:,.0f} kWh</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-box" style="background-color: #27AE60;">
            <h3>💨 CO₂ total émis</h3>
            <p>{kpi_co2_total:,.2f} tonnes</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-box" style="background-color: #E74C3C;">
            <h3>🌱 Arbres compensés</h3>
            <p>{kpi_arbres_compenses:,.0f} arbres</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")



#######KPI CONSOMMATION
###############COPIER 


# Calculer la distance moyenne parcourue par mode de transport
distance_moyenne_energy = df.groupby("mode_transport")[["vélo_km", "VAE_km", "voiture_km"]].sum().sum(axis=1)

# Regrouper la consommation d’énergie totale
df_energy_total = df.groupby("mode_transport")["consommation_kWh"].sum()

# Ramener toutes les valeurs à **une échelle de 5 km** et arrondir à 2 décimales
df_energy_5km = (df_energy_total.div(distance_moyenne_energy, axis=0) * 5).round(2)

# Assurer que les 3 modes sont bien présents
df_energy_5km = df_energy_5km.reindex(["Vélo", "Vélo électrique", "Voiture"], fill_value=0)

# 🔹 Correction : Forcer le vélo à 0 et éviter notation scientifique
df_energy_5km[df_energy_5km < 0.01] = 0  # Le vélo est bien à 0 kWh

# Définir un `max` correct pour éviter que le graphique soit écrasé
y_max = max(df_energy_5km) * 1.2 if max(df_energy_5km) > 1 else 1

# 📌 Options mises à jour avec texte en haut
bar_chart_options_5km = {
    "tooltip": {"trigger": "item", "formatter": "{b}: {c} kWh"},
    "xAxis": {"type": "category", "data": df_energy_5km.index.tolist()},
    "yAxis": {
        "type": "value",
        "name": "Consommation (kWh) pour 5 km",
        "nameLocation": "end",  # Texte en haut
        "nameGap": 10,  # Moins d’espace pour un meilleur rendu
        "axisLabel": {"formatter": "{value} kWh"},  # Évite notation scientifique
        "min": 0,
        "max": y_max  
    },
    "series": [
        {
            "data": df_energy_5km.tolist(),
            "type": "bar",
            "color": "#4CAF50",
            "label": {
                "show": True,
                "position": "top",
                "formatter": "{c} kWh"
            }
        }
    ],
}

# 📌 Affichage du graphique corrigé
st.subheader("🔋 Consommation énergétique par mode de transport (kWh/5 km)")
st_echarts(options=bar_chart_options_5km, height="400px")
st.markdown(
    """
    <div style="text-align: right; font-size: 0.8em; color: black;">
        <i><a href="https://www.2raventure.com/fr/blog/la-consommation-electrique-d-un-vae-n108?srsltid=AfmBOoqopSOeTlk36KbvfrTCefElWVfHK7TrLn2tbLqSQ1JnWdknxI3x" target="_blank" style="color: black; text-decoration: none;">
        https://www.2raventure.com/fr/blog/la-consommation-electrique-d-un-vae-n108?srsltid=AfmBOoqopSOeTlk36KbvfrTCefElWVfHK7TrLn2tbLqSQ1JnWdknxI3x
        </a></i>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")
##############COLLER













# 📌 **Disposition des filtres Cycle de Vie + Donut Chart**
st.subheader(" Répartition des émissions de CO₂ par mode de transport")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader(" Étape du Cycle de Vie")
    
    # Options de cycle de vie
    cycle_vie_mapping = {
        "Fabrication": "CO2_fabrication_kg",
        "Utilisation": "CO2_utilisation_kg"
    }
    
    # Checkbox pour chaque étape du cycle de vie (cochées par défaut)
    fabrication_checked = st.checkbox("Fabrication", value=True)
    utilisation_checked = st.checkbox("Utilisation", value=True)
    
    # Déterminer les colonnes sélectionnées en fonction des cases cochées
    selected_columns = []
    if fabrication_checked:
        selected_columns.append(cycle_vie_mapping["Fabrication"])
    if utilisation_checked:
        selected_columns.append(cycle_vie_mapping["Utilisation"])

# Vérifier si au moins une étape du cycle de vie est sélectionnée
if not selected_columns:
    st.warning("Veuillez sélectionner au moins une étape du cycle de vie.")
else:
    with col2:
        # Filtrer les données selon les sélections
        df_filtered["CO2_filtré"] = df_filtered[selected_columns].sum(axis=1)
        df_final = df_filtered.groupby("mode_transport")["CO2_filtré"].sum().reset_index()

        # 🔥 Donut Chart interactif avec ECharts
        donut_chart_options = {
            "tooltip": {"trigger": "item"},
            "legend": {"top": "5%", "left": "center"},
            "series": [
                {
                    "name": "Émissions de CO₂",
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
                        "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
                    },
                    "labelLine": {"show": False},
                    "data": [{"value": row["CO2_filtré"], "name": row["mode_transport"]} for _, row in df_final.iterrows()],
                }
            ],
        }

        st_echarts(options=donut_chart_options, height="500px")

st.markdown("---")

# 📢 **Message engageant**
st.info("🌍 L’impact environnemental dépend du mode de transport. Découvrez combien d’énergie et de CO₂ vous pouvez économiser en changeant vos habitudes !")

