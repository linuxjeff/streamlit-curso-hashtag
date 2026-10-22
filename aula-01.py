# Importar as bibliotecas necessárias
import streamlit as st
import pandas as pd
import yfinance as yf

# Criar as funções de carregamento de dados

    # Cotações do Itau - ITUB4 - 2010 a 2024
@st.cache_data
def carregar_dados(empresa):
    dados_acao = yf.Ticker(empresa)
    cotacoes_acao = dados_acao.history(start="2010-01-01", end="2024-07-01")
    cotacoes_acao = cotacoes_acao[["Close"]]
    return cotacoes_acao

dados = carregar_dados("ITUB4.SA")
print(dados)

# Preparar a vizualizações

# Criar a interface do streamlit
st.write("""
    # App Preço de Ações
    O gráfico abaixo representa a evolução do preçodas ações do Itau (ITUB4) ao logo dos anos.
""")

# Criar grafico
st.line_chart(dados)
