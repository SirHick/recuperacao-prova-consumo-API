
import streamlit as st
from consumidor_api import obter_dados_meteorologicos

st.set_page_config(
    page_title="Dashboard Meteorológico",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Meteorológico")
st.write("Painel de monitoramento — Jaraguá do Sul/SC")

if st.button("🔄 Consultar novamente"):
    st.rerun()

try:
    with st.spinner("Atualizando painel..."):
        dados = obter_dados_meteorologicos()

    st.success("Painel atualizado.")

    st.subheader("Indicadores principais")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🌡️ Temperatura",
        f"{dados['temperatura']:.1f} °C"
    )

    col2.metric(
        "💧 Umidade relativa",
        f"{dados['umidade_relativa']:.0f} %"
    )

    col3.metric(
        "🌡️ Sensação térmica",
        f"{dados['sensacao_termica']:.1f} °C"
    )

    st.divider()

    st.subheader("Condições ambientais")

    esquerda, direita = st.columns(2)

    with esquerda:
        st.markdown("**Precipitação**")

        st.metric(
            "🌧️ Volume registrado",
            f"{dados['precipitacao']:.1f} mm"
        )

    with direita:
        st.markdown("**Velocidade do vento**")

        st.metric(
            "🍃 Velocidade registrada",
            f"{dados['velocidade_vento']:.1f} km/h"
        )

    st.divider()

    st.subheader("Indicador de umidade relativa")

    umidade = max(0, min(100, dados["umidade_relativa"]))

    st.progress(umidade / 100)
    st.caption(f"Umidade relativa: {umidade:.0f}%")

except Exception as erro:
    st.error(f"Erro ao atualizar o dashboard: {erro}")