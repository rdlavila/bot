import sqlite3
import streamlit as st

# Criar conexão com o banco de dados
def connect():
    conn = sqlite3.connect('dados.db')
    c = conn.cursor()

# Fechar conexão
def close():
    conn.close()