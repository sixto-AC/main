import streamlit as st
import os
from datetime import datetime, timedelta
import jwt

# Configuración inicial de la página
st.set_page_config(page_title="SafeHealthAI", layout="centered")

# Configuración para cumplir con HIPAA y GDPR
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Función para mostrar el login
def login():

    st.image("SafeHealthAI-app/assets/SafeHealthAI-logo.jpg", width=100)  
    st.subheader("Inicio de sesión")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == "admin" and password == "password":  # Cambia por tu lógica de autenticación
            st.session_state.logged_in = True
        else:
            st.error("Usuario o contraseña incorrectos")

# Función para mostrar disclaimers de compliance
def compliance_disclaimers():
    st.warning("Esta aplicación cumple con HIPAA y GDPR para la protección de datos sensibles.")
    st.write("Al continuar, aceptas que los datos ingresados serán tratados conforme a estas normativas.")
    
    if st.checkbox("Acepto y comprendo las políticas de protección de datos"):
        st.session_state.accepted = True
    else:
        st.stop()

# Mostrar contenido solo si el usuario está logueado
if not st.session_state.logged_in:
    login()
else:
    # Si está logueado, mostrar contenido principal
    st.sidebar.title("SafeHealthAI")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update(logged_in=False))

    st.sidebar.markdown("""
    - **Inicio**
    - **Dashboard**
    - **Recomendaciones**
    - **Asistente**
    - **Historias médicas**
    """)

    st.title("SafeHealthAI - Asistente Virtual Médico")
    st.markdown("---")
    st.subheader("Descripción del Proyecto")
    st.write("""
    **SafeHealthAI** es un asistente virtual médico diseñado para proporcionar análisis predictivo y protección dinámica de datos sensibles.
    Este proyecto está alineado con las normativas HIPAA y GDPR para asegurar la confidencialidad y protección de la información del usuario.
    """)
     # Enlace al repositorio de GitHub
    repo_url = "https://github.com/InnovationChallengeGrupo5/SafeHealthAI"  # Reemplaza con la URL de tu repositorio
    st.markdown(f"[![GitHub](https://img.shields.io/badge/GitHub-Proyecto-100000?style=for-the-badge&logo=github&logoColor=white)]({repo_url})", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("[Política de Privacidad](/SafeHealthAI-app/pages/privacy_policy.md)")
    compliance_disclaimers()
  

    # Consentimiento para procesamiento de datos de salud
    consentimiento = st.checkbox("Doy mi consentimiento para el tratamiento de mis datos de salud de acuerdo con HIPAA y GDPR.")
    if not consentimiento:
        st.warning("Necesitas dar tu consentimiento para continuar.")
        st.stop()
    
    # Botones para derechos de acceso
    if st.button("Solicitar acceso a mis datos"):
        st.success("Recibirás un enlace para acceder a tus datos registrados.")
    if st.button("Ejercer mi derecho al olvido"):
        st.warning("Al ejercer este derecho, se eliminarán todos tus datos almacenados en la aplicación.")

    # Integración de Copilot
    copilot_url = "https://copilotstudio.microsoft.com/.../canvas"
    st.subheader("Copilot de SafeHealthAI")
    st.components.v1.iframe(copilot_url, width=800, height=600)


# Insertar avisos de compliance en todo el contenido principal.
st.subheader("Aviso de Compliance")
st.write("**Nota**: Esta aplicación cumple con todas las normativas vigentes sobre el manejo de datos sensibles y está en conformidad con HIPAA.")
