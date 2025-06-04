import streamlit as st
import random

st.set_page_config(page_title="Desafio da Fazenda 🐗", page_icon="🌽")

def play_sound(sound_url):
    st.markdown(
        f"""
        <audio autoplay>
            <source src="{sound_url}" type="audio/mpeg">
        </audio>
        """,
        unsafe_allow_html=True,
    )

if "vidas" not in st.session_state:
    st.session_state.vidas = 3
    st.session_state.rodada = 1
    st.session_state.pontos = 0
    st.session_state.resultado = ""
    st.session_state.fase = 1

st.title("🐗 Desafio da Fazenda – Fuga dos Javalis")
st.markdown(f"🌾 **Fase {st.session_state.fase}** — Rodada {st.session_state.rodada}")
st.markdown(f"❤️ Vidas restantes: {st.session_state.vidas}")
st.markdown(f"🏆 Pontuação: {st.session_state.pontos}")

acoes = ["Fugir pra esquerda", "Parar e se esconder", "Fugir pra direita"]
escolha = st.radio("Escolha sua ação:", acoes)

if st.button("👉 Confirmar ação"):
    direcao_javali = random.choice(["esquerda", "direita", "nenhum"])
    sorte = random.random()
    sucesso = False
    humor = ""

    if escolha == "Fugir pra esquerda" and direcao_javali == "direita":
        sucesso = True
        humor = "🐄 Você correu feito galinha em dia de festa. Escapou bonito!"
    elif escolha == "Fugir pra direita" and direcao_javali == "esquerda":
        sucesso = True
        humor = "🐓 Quase que o bicho te pega! Mas você foi ligeiro!"
    elif escolha == "Parar e se esconder" and sorte > 0.6:
        sucesso = True
        humor = "🌿 Você ficou parado que nem cerca quebrada... e deu certo!"
    else:
        st.session_state.vidas -= 1
        humor = "💥 Trombou com o javali! Levou uma chifrada no orgulho."

    if sucesso:
        st.session_state.pontos += 1
        if st.session_state.pontos % 5 == 0:
            st.session_state.fase += 1
            humor += " 🌟 Avançou pra próxima fase!"
        play_sound("https://www.soundjay.com/button/beep-07.mp3")
    else:
        play_sound("https://www.soundjay.com/button/beep-10.mp3")

    st.session_state.rodada += 1
    st.session_state.resultado = humor
    st.experimental_rerun()

if st.session_state.resultado:
    st.markdown(f"### Resultado da última rodada:\n{st.session_state.resultado}")

if st.session_state.vidas <= 0:
    st.error("☠️ Fim de jogo! O javali levou a melhor dessa vez...")
    st.markdown(f"**Você chegou até a fase {st.session_state.fase} com {st.session_state.pontos} pontos.**")
    if st.button("🔁 Jogar novamente"):
        st.session_state.vidas = 3
        st.session_state.rodada = 1
        st.session_state.pontos = 0
        st.session_state.resultado = ""
        st.session_state.fase = 1
        st.experimental_rerun()
