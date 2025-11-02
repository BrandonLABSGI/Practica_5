import streamlit as st
from modulos.venta import mostrar_venta
from modulos.login import login

# Si NO hay sesión, pedir login
if not st.session_state.get("sesion_iniciada"):
    login()
    st.stop()  # Evita que el resto del código se ejecute sin login

# ✅ Si hay sesión, mostrar menú lateral
opciones = ["Ventas", "Otra opción"]
seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

# ✅ Contenido según selección
if seleccion == "Ventas":
    mostrar_venta()
elif seleccion == "Otra opción":
    st.write("Has seleccionado otra opción.")
