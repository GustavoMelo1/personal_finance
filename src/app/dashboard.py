import streamlit as st
import sys
import os
import plotly.express as px
import pandas as pd
import sqlite3
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.crud import balance_flow, select_investment, insert_flow
from core.table import create_db
from core.searcher import wishes

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

create_db()

st.title("Fluxo de Caixa")
st.caption("Controle Financeiro")

st.divider()
st.header("Visão Geral")

column1, column2, column3 = st.columns(3)

with column1:
    balance = balance_flow()
    st.metric(label="Saldo Livre", value=f"R$ {balance:.2f}")

with column2:
    st.metric(label="Saldo VA", value="R$ 0.00")

with column3:
    investments = select_investment()
    total_invested = sum([row[5] for row in investments])
    st.metric(label="Total Investido", value=f"R$ {total_invested:.2f}")

st.divider()
st.header("Mês")

column_form, column_chart = st.columns([1, 2])

with column_form:
    st.subheader("Adicionar")
    date = st.date_input("Data")
    description = st.text_input("Descrição")
    category = st.selectbox("Categoria", ["Alimentacao", "TI", "Cartao", "Conta", "Luxo", "Saude", "Transporte", "Outros"])
    type = st.selectbox("Tipo", ["Income", "Expense"])
    value = st.number_input("Valor", min_value=0.0)
    bank = st.selectbox("Conta", ["Santander", "Nubank", "Rico", "VA"])
    
    if st.button("Salvar"):
        insert_flow(str(date), description, category, type, value, bank)
        st.success("Salvo!")

with column_chart:
    st.subheader("Resumo")
    
    with sqlite3.connect(os.path.join(BASE_DIR, 'data', 'financas.db')) as conn:
        df = pd.read_sql_query("SELECT type, SUM(value) as total FROM flow GROUP BY type", conn)
    
    if not df.empty:
        fig = px.bar(df, x='type', y='total', color='type',
                    color_discrete_map={'Income': '#1D9E75', 'Expense': '#D85A30'},
                    labels={'type': '', 'total': 'R$'})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Nenhum lançamento ainda. Adiciona um gasto ou receita.")

st.divider()
st.header("Objetivos")

column_wish, column_add = st.columns([2, 1])

with column_wish:
    st.subheader("Meus Desejos")
    desejos = wishes()

    if not desejos:
        st.info("Nenhum desejo cadastrado ainda.")
    else:
        for desejo in desejos:
            nome = list(desejo.keys())[0]
            with st.container(border=True):
                st.markdown(f"**{nome}**")
                st.write(f"Busca: {desejo['search']}")
                st.write(f"Preço máximo: R$ {desejo['max_value']:.2f}")
                st.write(f"Lojas: {', '.join(desejo['store'])}")

with column_add:
    st.subheader("Adicionar Desejo")
    nome = st.text_input("Nome")
    busca = st.text_input("Termo de busca")
    preco = st.number_input("Preço máximo", min_value=0.0)
    
    if st.button("Adicionar"):
        novo = {
            nome: len(desejos) + 1,
            "search": busca,
            "ignore": [],
            "store": ["Amazon", "Magazine Luiza"],
            "max_value": preco
        }
        desejos.append(novo)
        with open(os.path.join(BASE_DIR, 'data', 'wishes.json'), 'w', encoding='utf-8') as f:
            json.dump({"wishes": desejos}, f, ensure_ascii=False, indent=4)
        st.success("Desejo adicionado!")
        st.rerun()

st.divider()
st.header("Extrato")

st.divider()
st.header("Investimentos")