import tkinter as tk
import subprocess
import sys

def criar_header(janela, pagina_atual):
    """
    Cria o header padrão com botões de navegação.
    pagina_atual: 'aboutus', 'menu' ou 'order'
    """
    frame_header = tk.Frame(janela, bg="#905700")
    frame_header.pack(side="top", fill="x")

    titulo = tk.Label(frame_header, text="STEAM INC", font=("Bahnschrift Light", 25, "bold"), bg="#905700")
    titulo.pack(side="left", padx=20, pady=10)

    # Função para abrir página e fechar a atual
    def abrir_arquivo(caminho):
        janela.destroy()  # fecha a janela atual
        subprocess.Popen([sys.executable, caminho])

    # Botão SOBRE NÓS
    state_aboutus = "disabled" if pagina_atual == "aboutus" else "normal"
    botao_aboutus = tk.Button(frame_header, text="SOBRE NÓS", bg="#ffdc6a", fg="black",
                              relief="flat", padx=15, pady=5, state=state_aboutus,
                              command=lambda: abrir_arquivo(r"C:\Users\gamew\OneDrive\Área de Trabalho\VSCode Projetos\marcos\projetoCafeteriaSteamInc\aboutus.py"))
    botao_aboutus.pack(side="right", padx=5)

    # Botão PEDIDOS
    state_order = "disabled" if pagina_atual == "order" else "normal"
    botao_order = tk.Button(frame_header, text="PEDIDOS", bg="#ffdc6a", fg="black",
                            relief="flat", padx=15, pady=5, state=state_order,
                            command=lambda: abrir_arquivo(r"C:\Users\gamew\OneDrive\Área de Trabalho\VSCode Projetos\marcos\projetoCafeteriaSteamInc\order.py"))
    botao_order.pack(side="right", padx=5)

    # Botão CARDÁPIO
    state_menu = "disabled" if pagina_atual == "menu" else "normal"
    botao_menu = tk.Button(frame_header, text="CARDÁPIO", bg="#ffdc6a", fg="black",
                           relief="flat", padx=15, pady=5, state=state_menu,
                           command=lambda: abrir_arquivo(r"C:\Users\gamew\OneDrive\Área de Trabalho\VSCode Projetos\marcos\projetoCafeteriaSteamInc\menu.py"))
    botao_menu.pack(side="right", padx=5)