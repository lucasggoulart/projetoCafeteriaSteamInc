import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk
from tkinter import font
import webbrowser

def abrir_site():
    webbrowser.open("https://github.com/lucasggoulart/projetoCafeteriaSteamInc")

def aboutus_screen():
    janela = tk.Tk()
    janela.title("Steam Inc - Sobre Nós")
    janela.geometry("1000x600")
    janela.configure(bg="#ffffff")

    
    def arredondar_bordas(imagem, raio):
        largura, altura = imagem.size
        mask = Image.new("L", (largura, altura), 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle((0, 0, largura, altura), raio, fill=255)
        imagem_rounded = imagem.copy()
        imagem_rounded.putalpha(mask)
        return imagem_rounded

    imagem_fundo = Image.open("img/background.png").resize((1000, 600), Image.LANCZOS).convert("RGBA")
    imagem_fundo = arredondar_bordas(imagem_fundo, 30)
    imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

    frame_header = tk.Frame(janela, bg="#ffffff")
    frame_header.pack(side="top", padx=20, pady=20)

    frame_principal = tk.Frame(janela, bg="#ffffff")
    frame_principal.pack(fill="both", expand=True, padx=20, pady=20)

    fundo_label = tk.Label(frame_principal, image=imagem_fundo_tk, bg="#ffebdb")
    fundo_label.place(x=0, y=0, relwidth=1, relheight=1)

    frame_esquerda = tk.Frame(frame_principal, bg="#ffffff")
    frame_esquerda.pack(side="left", expand=True, padx=20, pady=20)

    #label_emoji = tk.Label(frame_esquerda, text="☕", font=("Helvetica", 100), bg="#ffffff")
    #label_emoji.pack()

    frame_direita = tk.Frame(frame_principal, bg="#ffffff")
    frame_direita.pack(side="right", expand=True, padx=20, pady=20)

    titulo = tk.Label(frame_header, text="steam inc - カフェ", font=("Bahnschrift SemiBold", 20, "bold"), bg="#ffffff")
    titulo.pack(anchor="w")

    #fonts = list(font.families())
    #fonts.sort()

    #for f in fonts:
        #print(f)

    subtitulo = tk.Label(frame_direita, text="Quem somos?", font=("Segoe UI Semibold", 24, "bold"), bg="#ffffff")
    subtitulo.pack(anchor="w", pady=(10, 5))

    sobre_label = tk.Label(frame_direita, text="SOBRE NÓS:", font=("Segoe UI Semibold", 13, "bold"), bg="#ffffff", fg="#6b4f4f")
    sobre_label.pack(anchor="w", pady=(5, 0))

    descricao = (
        "A Steam Inc é uma solução online desenvolvida para modernizar o processo de pedidos em cafeterias. "
        "O sistema simula "
        "um totem de autoatendimento que facilita e agiliza a experiência do cliente.\n\n"
        "Nosso objetivo é oferecer uma plataforma intuitiva, com navegação simples, para que os clientes possam "
        "conhecer nossos produtos, realizar pedidos e finalizar compras com praticidade."
    )

    texto = tk.Label(frame_direita, text=descricao, wraplength=400, justify="left", font=("Segoe UI Light", 13, "bold"), bg="#ffffff")
    texto.pack(anchor="w", pady=(5, 15))

    botao_fechar = tk.Button(frame_direita, text="FECHAR", bg="#c26d2d", fg="white", relief="flat",
                             padx=15, pady=5, command=janela.destroy)
    botao_fechar.pack(anchor="w")

    separador = ttk.Separator(janela, orient='horizontal')
    separador.pack(fill='x')

    rodape = tk.Frame(janela, bg="#000000")
    rodape.pack(fill="x")

    texto_rodape = tk.Label(
        rodape,
        text="© 2025 Steam Inc. Todos os direitos reservados.\n"
             "Cliente: Felipe Cesare | Desenvolvedor: Lucas Goulart",
        font=("Arial", 9),
        fg="white",
        bg="#000000"
    )
    texto_rodape.pack()

    link_contato = tk.Label(
        rodape,
        text="→ Repositório Oficial do GitHub",
        font=("Arial", 9, "underline"),
        fg="white",
        cursor="hand2",
        bg="#000000"
    )
    link_contato.pack()
    link_contato.bind("<Button-1>", lambda e: abrir_site())

    janela.mainloop()

if __name__ == "__main__":
    aboutus_screen()
