import streamlit as st
import pandas as pd
import urllib.parse

# Configuración de la página web
st.set_page_config(page_title="Catálogo de Sublimados", page_icon="📱", layout="wide")

# Función corregida usando el endpoint de miniaturas de Google Drive
def obtener_url_imagen_drive(url_drive):
    try:
        if "file/d/" in url_drive:
            id_archivo = url_drive.split("file/d/")[1].split("/")[0]
            return f"https://drive.google.com/thumbnail?id={id_archivo}&sz=w600"
    except Exception:
        pass
    return url_drive

# 1. Base de datos con la información exacta de tu enlace
@st.cache_data
def cargar_datos():
    datos = [
        # Animal nocturno
        {"Colección": "Animal nocturno", "Modelo": "Oso", "URL": "https://drive.google.com/file/d/1BZCRfRa1hrJvFdh_al0wnpOACBZHWQuo/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Aguila", "URL": "https://drive.google.com/file/d/195Xdr1J3-EZe_ARYQA-KRVhh8gPozoHZ/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "León", "URL": "https://drive.google.com/file/d/18jWpnDPiU3WsDga3-5MDMCILvrG_lU7g/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Buho", "URL": "https://drive.google.com/file/d/1wG6dwNlQB1nW8nq6vmn5v-MXqx7_SYfm/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Serpiente", "URL": "https://drive.google.com/file/d/1mQG5akzWGS4Pwwe_lJ3VIu1BEVZIt0W-/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Puma", "URL": "https://drive.google.com/file/d/17d7VGoPzU-VBmqxB8CXQjnT8GKcsropI/view?usp=drivesdk"},
        {"Colección": "Animal nocturno", "Modelo": "Elefante", "URL": "https://drive.google.com/file/d/1n1QpDz6J6PNgcdVVAJldfZ3xA7SuZmle/view?usp=drivesdk"},
        # Angel Armado
        {"Colección": "Angel Armado", "Modelo": "Venado", "URL": "https://drive.google.com/file/d/1rnyExjeEGQmoaHT6Noo_6ZTeMuS88F1H/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado IIII", "URL": "https://drive.google.com/file/d/1hG4i-2fq539uY5CwHVNC9EO9X-ECnpVp/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VIIII", "URL": "https://drive.google.com/file/d/1BLm6Dtb5XJsqVbYL2P_JPQQ7Q9VII_oC/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VIII", "URL": "https://drive.google.com/file/d/1JwICILHiG6OLb8WNqajhYhwpianfZuhA/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VII", "URL": "https://drive.google.com/file/d/1FNPf8xcL0xVyLXSlR7rgBCO6ph2s28V7/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado VI", "URL": "https://drive.google.com/file/d/10bU3Uyr5Wm6hi-zRwsqxlHvOVJn8MAgD/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado V", "URL": "https://drive.google.com/file/d/1CJB2gZ9inD23jNJI9_EldfijA5wDKTtc/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado III", "URL": "https://drive.google.com/file/d/1DfpEVIGhuKnpPiuvfkIlHLDPHZXMdLzK/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado II", "URL": "https://drive.google.com/file/d/1HXv4R9Zb8V96XwJKD-x4qGkkiBfcgA5Q/view?usp=drivesdk"},
        {"Colección": "Angel Armado", "Modelo": "Armado I", "URL": "https://drive.google.com/file/d/12irI1nOr37XgYRWjbt-oXPq01t-1IgYV/view?usp=drivesdk"},
        # Animal
        {"Colección": "Animal", "Modelo": "Animal XIIII", "URL": "https://drive.google.com/file/d/1FGqbTtYZutDDqp9sDV0hKqBkJKOVxrDy/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal XIII", "URL": "https://drive.google.com/file/d/1c1gLcwG9qOAGUb9SfVjxInW6asxVBzMi/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal XII", "URL": "https://drive.google.com/file/d/1jEXB2_87uqj8FebKoQrdauknF6W2SLp8/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal XI", "URL": "https://drive.google.com/file/d/1iPKySoH_HDW-zGqlkb8ojqjQfMu81t8T/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal X", "URL": "https://drive.google.com/file/d/1SOSbtDXAW3jDJGpRDWesy4ISmYL3KXGq/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VIIII", "URL": "https://drive.google.com/file/d/1bFVja4a6eh6lHzEljdGU0nA_ffkWYWcz/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VIII", "URL": "https://drive.google.com/file/d/1YsVM6CGYpg7GfmoZuCwW995xRUB8YYqv/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VII", "URL": "https://drive.google.com/file/d/1yEi3o6_F2WjCEX-VHy3zKjsY73FUYyt9/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal VI", "URL": "https://drive.google.com/file/d/1IcFRfv2R8wGKkQZkM6CvQwbZKIMoZWmk/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal V", "URL": "https://drive.google.com/file/d/1EuB64sR_nt2wke-RBXjbLsN1BLBikg_1/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal IIII", "URL": "https://drive.google.com/file/d/1W2YURhKfbdHn9Omfv9de-s6hFMtgQeaG/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal III", "URL": "https://drive.google.com/file/d/1aVibEqqODWd1wT1nhFH4Hmxf7YWqhMDx/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal II", "URL": "https://drive.google.com/file/d/1OSGV9RMzBawEEAiMR9C2rblquQ8BSPjz/view?usp=drivesdk"},
        {"Colección": "Animal", "Modelo": "Animal I", "URL": "https://drive.google.com/file/d/1_wtreCfVsDf7M6ECCn7-CtdNRZsQTfAQ/view?usp=drivesdk"},
        # Magic
        {"Colección": "Magic", "Modelo": "Magic 12", "URL": "https://drive.google.com/file/d/1FVnzuujx9NHqy2R8hmlIylonYZ3sf8FN/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 11", "URL": "https://drive.google.com/file/d/12CiaMVD0wbptPNXh1lkuG-OhYEAp42jA/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 10", "URL": "https://drive.google.com/file/d/1Pf1mwYEFF2POB-jN7Mv4LoptrYoJwNDM/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 09", "URL": "https://drive.google.com/file/d/10FSWfmVs1bwl5v-FRc-_OqbgFeKjrPUc/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 08", "URL": "https://drive.google.com/file/d/1f9A72TJAelagydaxYRoQzpjXgbrLASZ8/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 07", "URL": "https://drive.google.com/file/d/18xuTEXCvRo_eTRp6diOUsyjwGT60lvZD/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 06", "URL": "https://drive.google.com/file/d/18Pg0NlTpn2GoXrdFp4uFe9NhdXIy-Atm/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 05", "URL": "https://drive.google.com/file/d/1Nlq3e5NkBPYnL0Y-qdsgYF0fZ2Y-5pHZ/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 04", "URL": "https://drive.google.com/file/d/1gHPn-xeEw13Tn1X2tGHKRkBPxwk5Z6Fa/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 03", "URL": "https://drive.google.com/file/d/1ojcDZvWWUvDjgVsktvB2ewrOOCAoc18X/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 02", "URL": "https://drive.google.com/file/d/156kpRWHII4Z1qf6iAd1vo26nG3pQqL9Z/view?usp=drivesdk"},
        {"Colección": "Magic", "Modelo": "Magic 01", "URL": "https://drive.google.com/file/d/137qwFVsBDfZgCHUsQz6xOjRg2rsdbdrr/view?usp=drivesdk"},
        # Mago de oz
        {"Colección": "Mago de oz", "Modelo": "Espantapajaro", "URL": "https://drive.google.com/file/d/1-1IBqhlAfnvE8R5yNQ7zJkC11-mTZddV/view?usp=drivesdk"},
        {"Colección": "Mago de oz", "Modelo": "Bruja", "URL": "https://drive.google.com/file/d/14ROBQC-Iu7OhxyIIS-bm4hHaVnemEVvC/view?usp=drivesdk"},
        # Warzone
        {"Colección": "Warzone", "Modelo": "Nevermore", "URL": "https://drive.google.com/file/d/1GNSV2cJJYMGMg8SbbOMlm8GoO3lUGVoc/view?usp=drivesdk"},
        # Bob
        {"Colección": "Bob", "Modelo": "Piña", "URL": "https://drive.google.com/file/d/13XrFrcsQSvS9cK7k4r9eEfCbiBdK6-A3/view?usp=drivesdk"},
        {"Colección": "Bob", "Modelo": "Patricio", "URL": "https://drive.google.com/file/d/1b61hUhjfCxPAYHl8NCc1_p2bTtQo_tvF/view?usp=drivesdk"}
    ]
    return pd.DataFrame(datos)

df_catalogo = cargar_datos()

# Número corregido incluyendo el código de país de México (+52) y sin espacios ni símbolos
TELEFONO_WHATSAPP = "525629088870"

if "carrito" not in st.session_state:
    st.session_state.carrito = {}

st.title("📱 Catálogo de Sublimados Interactivos")
st.write("Selecciona tus modelos de la lista, define los metros que necesitas y envía tu pedido directo por WhatsApp.")

# --- DISEÑO EN COLUMNAS ---
col_izquierda, col_derecha = st.columns([2, 1])

with col_izquierda:
    st.header("✨ Modelos Disponibles")
    
    colecciones = ["Todas"] + list(df_catalogo["Colección"].unique())
    coleccion_seleccionada = st.selectbox("Filtrar por Colección:", colecciones)
    
    if coleccion_seleccionada != "Todas":
        df_filtrado = df_catalogo[df_catalogo["Colección"] == coleccion_seleccionada]
    else:
        df_filtrado = df_catalogo

    for index, fila in df_filtrado.iterrows():
        key_id = f"{fila['Colección']}_{fila['Modelo']}"
        
        with st.container(border=True):
            col_img, col_info, col_accion = st.columns([1.2, 1.8, 1])
            
            with col_img:
                url_directa = obtener_url_imagen_drive(fila['URL'])
                st.image(url_directa, use_container_width=True)
                
            with col_info:
                st.subheader(f"{fila['Modelo']}")
                st.caption(f"Colección: {fila['Colección']}")
                
            with col_accion:
                registro_actual = st.session_state.carrito.get(key_id, 0.0)
                if isinstance(registro_actual, dict):
                    valor_actual = float(registro_actual.get("Metros", 0.0))
                else:
                    valor_actual = float(registro_actual)
                
                metros = st.number_input(
                    "Metros:", 
                    min_value=0.0, 
                    max_value=500.0, 
                    value=valor_actual, 
                    step=0.5, 
                    key=f"input_{key_id}"
                )
                
                if metros > 0:
                    st.session_state.carrito[key_id] = {
                        "Colección": fila["Colección"],
                        "Modelo": fila["Modelo"],
                        "Metros": metros
                    }
                elif key_id in st.session_state.carrito and metros == 0:
                    del st.session_state.carrito[key_id]

with col_derecha:
    st.header("🛒 Tu Pedido")
    
    if not st.session_state.carrito:
        st.info("Sin modelos seleccionados. Ajusta los metros en el panel izquierdo.")
    else:
        resumen_datos = []
        texto_whatsapp = "¡Hola! Quisiera realizar un pedido con el siguiente detalle:\n\n"
        total_metros = 0
        
        for k, v in st.session_state.carrito.items():
            resumen_datos.append({
                "Modelo": v["Modelo"],
                "Colección": v["Colección"],
                "Metros": f"{v['Metros']} m"
            })
            texto_whatsapp += f"• *{v['Colección']} - {v['Modelo']}*: {v['Metros']} metros\n"
            total_metros += v["Metros"]
            
        df_resumen = pd.DataFrame(resumen_datos)
        st.table(df_resumen)
        
        st.metric(label="Total Metros Seleccionados", value=f"{total_metros} m")
        
        if st.button("Limpiar todo el Pedido"):
            st.session_state.carrito = {}
            st.rerun()
            
        st.write("---")
        
        # Codificación correcta del texto para la URL
        texto_codificado = urllib.parse.quote(texto_whatsapp)
        enlace_wa = f"https://wa.me/{TELEFONO_WHATSAPP}?text={texto_codificado}"
        
        # Implementación nativa de Streamlit para evitar que los navegadores bloqueen la ventana emergente
        st.link_button(
            "🚀 Solicitar pedido por WhatsApp", 
            enlace_wa, 
            use_container_width=True
        )