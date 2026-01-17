import requests
import streamlit as st

st.set_page_config(
    page_title="Buscador de Países",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Buscador de Países")
st.caption("Consulte informações de países usando uma API pública")

pais = st.text_input("Digite o nome de um país:")

if pais:
    url = f"https://restcountries.com/v3.1/name/{pais}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()[0]

        nome_pt = dados.get("translations", {}).get("por", {}).get("common")
        nome = nome_pt if nome_pt else dados["name"]["common"]

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader(nome)

            continentes_pt = {
                "Africa": "África",
                "Americas": "Américas",
                "Asia": "Ásia",
                "Europe": "Europa",
                "Oceania": "Oceania",
                "Antarctic": "Antártida"
            }

            continente = continentes_pt.get(
                dados.get("continents", [""])[0],
                dados.get("continents", [""])[0]
            )

            capital = dados.get("capital", ["Não informado"])[0]
            populacao = f"{dados.get('population', 0):,}".replace(",", ".")
            moeda = list(dados.get("currencies", {}).values())[0]["name"] if dados.get("currencies") else "Não informado"
            idioma = list(dados.get("languages", {}).values())[0] if dados.get("languages") else "Não informado"

            st.write(f"🌎 **Continente:** {continente}")
            st.write(f"🏳️ **Capital:** {capital}")
            st.write(f"👥 **População:** {populacao}")
            st.write(f"💰 **Moeda:** {moeda}")
            st.write(f"🗣️ **Idioma:** {idioma}")

        with col2:
            bandeira = dados.get("flags", {}).get("png")
            if bandeira:
                st.image(bandeira)

    else:
        st.error("País não encontrado 😢")
