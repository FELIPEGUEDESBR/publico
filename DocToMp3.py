# Script para converter texto de um arquivo .docx para um arquivo .mp3
# Primeiro instale os pacotes: pyttsx3, python-docx, tkinter com apt install 
import pyttsx3
from docx import Document
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Função para converter texto de um arquivo .docx para um arquivo .mp3
def doc_to_mp3(input_file, output_file, rate=150):
    document = Document(input_file)
    text = ''
    for paragraph in document.paragraphs:
        text += paragraph.text + '\n'
    text_to_speech(text, output_file, rate)

# Esta função converte o texto em fala sintetizada, fornecendo a flexibilidade da taxa de fala e salvando-o
def text_to_speech(text, output_file, rate=150):
    audio_interface = pyttsx3.init()
    audio_interface.setProperty('rate', rate)   
    audio_interface.save_to_file(text, output_file)
    audio_interface.runAndWait()

# Navega pelo sistema de arquivos para selecionar um arquivo .docx
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

# processa um arquivo de documento selecionado, convertendo seu conteúdo de texto em formato de audiobook MP3 e notifica o usuário ao criar com sucesso, exibindo o nome do audiobook
def create_audio():
    doc_file = entry_path.get()
    if not doc_file:
        messagebox.showerror("Error", "Please select a document file")
        return
    output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if output_file:
        doc_text = extract_text_from_doc(doc_file)
        text_to_speech(doc_text, output_file)
        messagebox.showinfo("Success", f"Audiobook '{output_file}' created successfully!")

# Cria uma janela com o título “AudioBook at Flood”.

root = tk.Tk()
root.title("AudioBook at Flood")

#Cria uma janela para mostrar o caminho do arquivo selecionado
entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=0, padx=10, pady=10)

#Cria um botão para selecionar um arquivo .docx
btn_browse = tk.Button(root, text="Browse File", command=browse_file)
btn_browse.grid(row=0, column=1, padx=10, pady=10)

# Criar um botão para criar um audiobook
btn_create = tk.Button(root, text="Create Audiobook", command=create_audio)
btn_create.grid(row=1, columnspan=2, padx=10, pady=10)

# Inicia a janela principal
root.mainloop()