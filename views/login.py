import PySimpleGUI as sg
import sys
sys.path.insert(1, './backend')
import controller
import validacoes
def showLogin():
    isLogged = False

    sg.theme('Reddit')

    layout = [[sg.Image(filename='imgs/logowp-disparod.png', enable_events=True, key='-IMAGEM-')],
            [sg.Text('Usuário:'), sg.InputText(size=(20,40),key='user')],
            [sg.Text('Senha:  '), sg.InputText(size=(20,40),key='password',password_char='*')],
            [sg.Button('Login', key='-LOGIN-')]]

    window = sg.Window('Faça o Login', layout,element_justification='center')

    # Ler os dados do banco de dados
    #username, password = window.read()

    while True:
        evento, valores = window.read()

        if evento == sg.WINDOW_CLOSED:
            break
        elif evento == '-LOGIN-':
            isLogged = validacoes.login(valores['user'],valores['password'])
            if isLogged:    
                isLogged=True
                window.close()
                controller.main(isLogged)
            else:
                sg.PopupError("Verfique suas credenciais!")
                

