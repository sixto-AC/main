 # Subir recetas médicas
import streamlit as st
from azure.storage.blob import BlobServiceClient
import os

# Configuración de la conexión a Azure Storage
#CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
#CONTAINER_NAME = "nombre-del-contenedor"

if 'logged_in' not in st.session_state or not st.session_state.logged_in:
    st.warning("Por favor, inicia sesión para acceder al dashboard.")
    st.stop()  # Detener la ejecución si no está autenticado

# Configurar el cliente de Blob Storage
#blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
#container_client = blob_service_client.get_container_client(CONTAINER_NAME)

st.title("Subir Historias Médicas")

# Subida de archivo
uploaded_file = st.file_uploader("Selecciona una historia médica para subir", type=["pdf", "jpg", "png"])

if uploaded_file is not None:
    # Leer el archivo
    file_contents = uploaded_file.read()
    blob_name = uploaded_file.name

    # Subir el archivo al contenedor de Azure Blob Storage
    try:
        #blob_client = container_client.get_blob_client(blob_name)
        #blob_client.upload_blob(file_contents, overwrite=True)
        st.success(f"Archivo '{blob_name}' subido exitosamente.")
    except Exception as e:
        st.error(f"Error al subir el archivo: {e}")    
    