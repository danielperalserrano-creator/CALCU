import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de Rebajas", page_icon="🛍️")

# Título y descripción
st.title(" Calculadora de Rebajas")
st.markdown("Introduce el precio original y el porcentaje de descuento.")
st.write("---")

# 2. Entrada de datos (barra lateral)
st.sidebar.header("Datos del Producto")

precio_original = st.sidebar.number_input(
    "Precio original (€)", 
    min_value=0.0, 
    max_value=1000.0, 
    value=50.0
)

descuento = st.sidebar.slider(
    "Porcentaje de descuento (%)", 
    0, 
    100, 
    20
)

# 3. Botón y lógica
if st.button("Calcular precio final"):

    # Cálculo del descuento
    cantidad_descuento = precio_original * (descuento / 100)
    precio_final = precio_original - cantidad_descuento

    # 4. Mostrar resultados
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Precio original", f"{precio_original:.2f} €")
        st.metric("Descuento aplicado", f"-{cantidad_descuento:.2f} €")

    with col2:
        st.metric("Precio final", f"{precio_final:.2f} €")
        st.success("¡Has ahorrado dinero! ")

    # Mostrar fórmula matemática
    st.write("---")
    st.info("Fórmula utilizada:")
    st.latex(r''' Precio\ Final = Precio\ Original - (Precio\ Original \times \frac{Descuento}{100}) ''')

