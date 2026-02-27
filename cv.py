import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Mon CV", page_icon="", layout="wide")

# Sidebar pour Contacts et Logiciels
st.sidebar.image("marco.jpeg",width=150)
st.sidebar.header(" **Contacts**")
st.sidebar.markdown("""
**Adresse**  
Ross-Bethio,

**Téléphone**  
[+221 76 352 68 65]

**Email**  
[marmboup11@gmail.com]
""")

st.sidebar.header(" **Logiciels maîtrisés**")
logiciels = [
    "QGIS / ArcGIS",
    "AutoCAD", 
    "Python",
    "Pix4D",
    "Excel",
    "PowerPoint",
    "Erdas"
]
for logiciel in logiciels:
    st.sidebar.markdown(f"• **{logiciel}**")

st.sidebar.markdown("---")
st.sidebar.markdown("*Géomaticien - L2 en cours*")

# Main content
st.title(" **Curriculum Vitae**")
st.markdown("**mar mboup** - Géomaticien")

## Compétences
st.header(" **Compétences**")
competences = [
    "Maîtrise des techniques de levés topographiques",
    "Conception et mise en page de cartes thématiques de qualité professionnelle",
    "Utilisation des instruments : Niveau, Station totale(manuelle,rebotisée), Drone, GPS",
    "Géo-référencement",
    "Implanter une base de données",
    
]

    
for comp in competences:
    
    st.markdown(f"• **{comp}**")

## Expériences Professionnelles
st.header(" **Expériences Professionnelles**")

st.subheader("**Aout - Septembre 2025**")
st.markdown("**stage en entreprise à la DGPRE (Direction de la Gestion et de la Planification des Ressources en Eau) au Sénégal :**")


## Formation
st.header(" **Formation**")

st.markdown("""
**2025 - 2026**  
**Centre d'entrepreneuriat et de développement technique (CEDT) le G15**  
*Licence 2 en Géomatique (Formation en cours)*

**2024 - 2025**  
**Centre d'entrepreneuriat et de développement technique (CEDT) le G15**  
*Licence 1 en Géomatique*

**2019 - 2020**  
**lycée Ross-Bethio**  
*Baccalauréat*
""")

