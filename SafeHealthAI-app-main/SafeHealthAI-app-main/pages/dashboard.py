import streamlit as st

# Verificar si el usuario está autenticado
if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Por favor, inicia sesión para acceder al dashboard.")
    st.stop()  # Detener la ejecución si no está autenticado

# Configuración de la página
st.set_page_config(page_title="Dashboard - SafeHealthAI", layout="wide")

# Título de la página
st.title("Dashboard de SafeHealthAI")
st.write("Esta sección muestra las visualizaciones de datos en Power BI.")

# URL de Power BI
# Reemplaza `power_bi_url` con el enlace embed de tu informe de Power BI
power_bi_url = "https://app.powerbi.com/view?r=TU_ENLACE_EMBED"

# Incrustar Power BI con iframe
st.components.v1.iframe(power_bi_url, width=800, height=600)
