import streamlit as st
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="DevFuture Reddit", page_icon="🚀", layout="wide")

# --- ESTILIZAÇÃO FUTURISTA (CSS) ---
st.markdown("""
    <style>
    /* Fundo e texto geral */
    .stApp {
        background-color: #0e1117;
        color: #00ffc3;
    }
    /* Estilização dos cards de posts */
    .post-card {
        background: rgba(255, 255, 255, 0.05);
        border-left: 5px solid #00ffc3;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .post-card:hover {
        border-left: 5px solid #ff00ff;
        background: rgba(255, 255, 255, 0.08);
    }
    /* Títulos */
    h1, h2, h3 {
        color: #ff00ff ! loosening;
        text-shadow: 2px 2px 10px rgba(255, 0, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- BANCO DE DADOS SIMULADO ---
if 'posts' not in st.session_state:
    st.session_state.posts = [
        {
            "autor": "Admin_Bot",
            "titulo": "Bem-vinda meu amor, minha namorada ninda",
            "conteúdo": "Este é o espaço para compartilhar seus projetos e ideias mais ambiciosas.",
            "data": "2026-04-03 00:00",
            "votos": 10
        }
    ]

# --- SIDEBAR (POSTAR NOVO CONTEÚDO) ---
with st.sidebar:
    st.header("⚡ Terminal de Upload")
    novo_autor = st.text_input("Seu Nickname", placeholder="Ex: CyberDev")
    novo_titulo = st.text_input("Título do Trabalho")
    novo_conteudo = st.text_area("Descrição/Código", placeholder="O que você desenvolveu?")
    
    if st.button("PUBLICAR NA REDE"):
        if novo_autor and novo_titulo and novo_conteudo:
            novo_post = {
                "autor": novo_autor,
                "titulo": novo_titulo,
                "conteúdo": novo_conteudo,
                "data": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "votos": 0
            }
            # Insere no topo como um Reddit
            st.session_state.posts.insert(0, novo_post)
            st.success("Post enviado para a Matrix!")
        else:
            st.error("Preencha todos os campos, programador.")

# --- CORPO PRINCIPAL ---
st.title("🌐 NEOLINKED // THE FUTURE")
st.markdown("---")

# Exibição dos Posts
for i, post in enumerate(st.session_state.posts):
    with st.container():
        st.markdown(f"""
            <div class="post-card">
                <small style='color: #888;'>Postado por u/{post['autor']} em {post['data']}</small>
                <h2 style='margin-top: 0;'>{post['titulo']}</h2>
                <p style='font-family: monospace; font-size: 1.1rem;'>{post['conteúdo']}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Sistema de Votos Simples
        col1, col2 = st.columns([1, 10])
        with col1:
            if st.button(f"▲", key=f"up_{i}"):
                st.session_state.posts[i]['votos'] += 1
        with col2:
            st.write(f"**{post['votos']}** pontos de reputação")
        
        st.markdown("<br>", unsafe_allow_html=True)
