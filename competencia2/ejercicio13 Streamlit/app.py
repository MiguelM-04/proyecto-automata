import streamlit as st
from archivo import Archivo
from analizador_lexico import AnalizadorLexico


class App:

    def __init__(self):
        st.set_page_config(page_title="Analizador Lexico", layout="wide")
        self.analizador = AnalizadorLexico()

    def ejecutar(self):
        st.title("Analizador Lexico con ANTLR y Streamlit")
        st.write("Sube un archivo `.sql` para ver tokens y errores lexicos.")        
        # Configuramos el cargador para que solo acepte extensiones .sql
        archivo_subido = st.file_uploader("Selecciona tu archivo", type=["sql"])

        if archivo_subido is None:
            st.info("Primero sube un archivo .py")
            return

        archivo = Archivo(archivo_subido)

        codigo = archivo.leer()
        info = archivo.obtener_info()

        st.subheader("Informacion del archivo")
        st.write("Nombre:", info["nombre"])
        st.write("Extension:", info["extension"])

        # Cambiamos el lenguaje de visualización del bloque de código a python
        st.subheader("Codigo original")
        st.code(codigo, language="sql")

        self.analizador.analizar(codigo)

        tokens = self.analizador.obtener_tokens()
        errores = self.analizador.obtener_errores()

        st.subheader("Tokens")

        if len(tokens) == 0:
            st.warning("No se encontraron tokens")
        else:
            st.dataframe(tokens, use_container_width=True)

        st.subheader("Errores lexicos")

        if len(errores) == 0:
            st.success("No hay errores lexicos")
        else:
            st.dataframe(errores, use_container_width=True)


if __name__ == "__main__":
    app = App()
    app.ejecutar()