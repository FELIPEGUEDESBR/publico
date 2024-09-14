# # Script para converter texto de um arquivo .docx para um arquivo .mp3

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# Função para abrir a janela de diálogo para escolher o arquivo
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

#Função para converter o arquivo
def convert_file():
    import pyttsx3
    import docx
    import os
    import re

    # Carrega o arquivo
    file_path = entry_path.get()
    if not file_path:
        return

    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"

    # Remove caracteres especiais
    text = re.sub(r'[^\w\s]', '', text)

    # Converte o texto em áudio
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if "Microsoft Daniel - Portuguese (Brazil)" in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.save_to_file(text, 'audio.mp3')
    engine.runAndWait()

    # Abre o arquivo de áudio
    os.system("audio.mp3")

# Criação da janela
janela = tk.Tk()
janela.title(" Aplicação GUI para conversão de texto em áudio") 
tk.Label(janela,text="Converter Word para mp3:").grid(row=0)


# Campos de entrada
entry_path = tk.Entry(janela, width=50)
entry_path.grid(row=3,column=1,sticky=tk.W,pady=4)

# Botão para localizar o arquivo
btnLocalizar = tk.Button(janela, text='Localizar Word', command=browse_file).grid(row=3,column=0,sticky=tk.W,pady=4)

# Botão para converter o arquivo
btnConverter = tk.Button(janela, text='Converter', command=convert_file).grid(row=4,column=0,sticky=tk.W,pady=4)


# Botão para sair
btnSair = tk.Button(janela, text='Sair', command=janela.quit).grid(row=4,column=1,sticky=tk.W,pady=4)

tk.mainloop()   