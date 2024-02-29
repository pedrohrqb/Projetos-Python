import customtkinter as ctk

janela = ctk.CTk() # Cria a janela

#configuração da janela principal

janela.title('Multi-tarefas') # Dando titulo a janela principal
janela.geometry('1000x750') # Definindo a largura e altura da janela principal
janela.resizable(width=False, height=False) # Tirando a permissão do usuário de aumentar ou diminuir a janela!

#Criando uma função de uma nova janela integrada a um botão.
def calculadora():
    calculadora = ctk.CTkToplevel(janela, fg_color='white')
    calculadora.geometry('300x400')
    calculadora.resizable(width=False, height=False)
    calculadora.title('Calculadora')
    calculadora.iconbitmap('imagens/calculator.png') # ARRUMAR ICONE DA CALCULADORA
    
       
#Botão que irá abrir uma nova janela ao clique    
btn_calc_1 = ctk.CTkButton(master=janela, text='Calculadora', command=calculadora).place(x=300, y=100)



janela.mainloop() #Executa a janela mantendo em um loop infinito.