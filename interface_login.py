import customtkinter as ctk 

janela = ctk.CTk()
janela.geometry("1000x800")
janela.title("Tarefas")
janela.maxsize(width=1000, height=800)
janela.minsize(width=1000, height=800)
janela._set_appearance_mode("black")
ctk.set_appearance_mode('black')


frame1 = ctk.CTkFrame(master=janela , width=400, height=400,border_width=2,corner_radius=30, border_color="purple").place(x=300, y=170)

#funções
def validar_login():
    usuario = campo_usuario.get()
    senha = campo_senha.get()
    usuario_correto = 'adm@gmail.com'
    senha_correta = 'foda'
        
    if usuario == "teste@gmail.com" and senha == "foda":
        resultado_login.configure(text = 'Bem vindo', text_color = 'green',)

        if campo_usuario.get() == usuario_correto and campo_senha.get() == senha_correta:
            janela.destroy()
            abrir_pagina_principal()


    else: resultado_login.configure(text = 'Incorreto', text_color = 'red')

"""def trocar_aparencia():
    modo_atual = ctk.get_appearance_mode()
    if modo_atual == "dark":
        ctk.set_appearance_mode("light")
    else: ctk.set_appearance_mode("system")"""


def alterar_tema(escolha):
    ctk.set_appearance_mode(escolha.lower())

#-----------
#button1
#def color (escolha):
#   print(f'Tema: {escolha} ')

btn = ctk.CTkOptionMenu(janela, values =['Dark', 'Light', 'Sytem'],command=alterar_tema , fg_color= "purple",
                    dropdown_hover_color = "gray",
                     button_color="gray")
btn.pack(pady=40)
btn.set("Temas")



if btn:
    comand = ctk.set_appearance_mode("black") 

#login
ctk.CTkLabel(janela, text="Login", font=("arial bold",20)).pack(pady=30, padx=10)

ctk.CTkLabel(janela, text="Gmail", font=("arial bold",20)).pack(pady=20, padx=10)


#campo de usuario
campo_usuario = ctk.CTkEntry(janela,placeholder_text='Digite seu Gmail')
campo_usuario.pack(pady=10)


#campo senha 
ctk.CTkLabel(janela, text="Senha", font=("arial bold",20)).pack(pady=30, padx=10)

campo_senha = ctk.CTkEntry(janela,placeholder_text='Digite sua senha', show = '*')
campo_senha.pack(pady=20)

btn_login = ctk.CTkButton(janela, text = "Login", command= validar_login, fg_color="purple" )
btn_login.pack(pady=40)



#resultado login
resultado_login = ctk.CTkLabel(janela, text='')
resultado_login.pack(pady=20)

def abrir_pagina_principal():
    janela_secundaria = ctk.CTk()
    janela_secundaria = ctk.geometry("1000x800")

    label_bem_vindo = ctk.CTkLabel(janela_secundaria, text= "Bem vindo!", font=("Arial",20))
    label_bem_vindo.pack(pady = 20)




janela.mainloop()