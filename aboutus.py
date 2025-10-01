import tkinter as tk
from tkinter import ttk
import webbrowser

def abrir_site():
    webbrowser.open("https://github.com/lucasggoulart/projetoCafeteriaSteamInc")

def criar_tela_sobre_nos():
    janela = tk.Tk()
    janela.title("Steam Inc - Sobre Nós")
    janela.geometry("600x500")
    janela.configure(bg="#f5f5f5")

    titulo = ttk.Label(janela, text="☕ Steam Inc", font=("Helvetica", 24, "bold"))
    titulo.pack(pady=10)

    subtitulo = ttk.Label(janela, text="Quem somos?", font=("Helvetica", 18))
    subtitulo.pack(pady=5)

    descricao = (
        "A Steam Inc é uma solução online desenvolvida para modernizar o processo de pedidos "
        "em cafeterias. Criado como um projeto do curso de Desenvolvimento de Sistemas da ETEC Jaraguá, "
        "o sistema simula um totem de autoatendimento que facilita e agiliza a experiência do cliente.\n\n"
        "Nosso objetivo é oferecer uma plataforma intuitiva, com navegação simples, para que os clientes "
        "possam conhecer nossos produtos, realizar pedidos e finalizar compras com praticidade."
    )

    texto_descricao = tk.Text(janela, wrap=tk.WORD, height=10, width=70, font=("Arial", 12))
    texto_descricao.insert(tk.END, descricao)
    texto_descricao.configure(state="disabled", bg="#ffffff")
    texto_descricao.pack(pady=10)

    botao_fechar = ttk.Button(janela, text="Fechar", command=janela.destroy)
    botao_fechar.pack(pady=10)

    separador = ttk.Separator(janela, orient='horizontal')
    separador.pack(fill='x', padx=20, pady=10)

    # Rodapé
    rodape_frame = tk.Frame(janela, bg="#f5f5f5")
    rodape_frame.pack(fill='x', pady=(5, 10))

    texto_rodape = tk.Label(
        rodape_frame,
        text="© 2025 Steam Inc. Todos os direitos reservados.\n"
             "Cliente: Felipe Cesare | Desenvolvedor: Lucas Goulart",
        font=("Arial", 9),
        bg="#f5f5f5"
    )
    texto_rodape.pack()

    link_contato = tk.Label(
        rodape_frame,
        text="🔗 Repositório Oficial do GitHub",
        font=("Arial", 9, "underline"),
        fg="blue",
        cursor="hand2",
        bg="#f5f5f5"
    )
    link_contato.pack()
    link_contato.bind("<Button-1>", lambda e: abrir_site())


    janela.mainloop()

# Executa a tela se o script for rodado diretamente
if __name__ == "__main__":
    criar_tela_sobre_nos()
