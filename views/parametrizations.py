import webbrowser
import sys
sys.path.insert(1, './backend')
import disparo
from PySimpleGUI import PySimpleGUI as sg

def showParametrizations(isLogged):
    site="www.wpdisparoantiblock.com"

    # Variaveis de sistema
    padding = ((0,0))

    # webbrowser.open(site)
    sg.theme('Reddit')


    layoutParametrizacoes =[
        [sg.Image(filename='imgs/logowp-disparoO.png', size=(300,50), enable_events=True, key='-IMAGEM-')],

        [sg.Text('\nParametrizações:\n')],

        [sg.Text('Defina o intervalo de tempo entre o envio de\ncada mensagem:')],
        [sg.Text('Min: '), sg.Spin([i for i in range(1,120)], initial_value=10, size=(4,1), pad=padding, key='tempMinEnvMsg'),  sg.Text('sec.'),
        sg.Text('Max: '), sg.Spin([i for i in range(1,120)], initial_value=20, size=(4,1), pad=padding, key='tempMaxEnvMsg'), sg.Text('sec. ') ],
        
        [sg.Text('\nDefina o intervalo de quantidadede envio de\nmensagens:')],
        [sg.Text('Min: '), sg.Spin([i for i in range(1,120)], initial_value=10, size=(4,1), pad=padding, key='qtdMinMsg'),  sg.Text('sec.'),
        sg.Text('Max: '), sg.Spin([i for i in range(1,120)], initial_value=20, size=(4,1), pad=padding, key='qtdMaxMsg'), sg.Text('sec. ') ],

        
        [sg.Text('\nDefina o intervalo de tempo para o descanso\ndo seu chip:')],
        [sg.Text('Min: '), sg.Spin([i for i in range(120,380)], initial_value=120, size=(4,1), pad=padding, key='restMinChip'),  sg.Text('sec.'),
        sg.Text('Max: '), sg.Spin([i for i in range(380,1000)], initial_value=380, size=(4,1), pad=padding, key='restMaxChip'), sg.Text('sec. ') ],

        [sg.Text('Selecione a sua lista\npara o envio das mensagens: ', key=('-uploadText-')),
        sg.FileBrowse('Upload', key='upload')],
        [sg.Button('Baixe o modelo do arquivo',key='-template-')],
        
        [sg.Button('Executar', key='-EXECUTAR-')]    
    ]

    janela = sg.Window('Dispara WP-AntiBlock', layoutParametrizacoes, element_justification='center')

    janela.set_icon('imgs/logowp-disparod.png')

    while True:
        evento, valores = janela.read()
        if evento == sg.WINDOW_CLOSED:
            break
        elif evento == '-IMAGEM-':
            # Abre o link no navegador ao clicar na imagem
                webbrowser.open(site)
        elif evento == '-template-':
            webbrowser.open(site+"/downloads")
        elif evento == '-EXECUTAR-':
            
            # recebe as parametrizações
            tempMinEnvMsg = valores['tempMinEnvMsg']
            tempMaxEnvMsg = valores['tempMaxEnvMsg']

            qtdMinMsg = valores['qtdMinMsg']
            qtdMaxMsg = valores['qtdMaxMsg']

            restMinChip = valores['restMinChip']
            restMaxChip = valores['restMaxChip']

            upload = valores['upload']

            if upload:
                disparo.sendMsg(tempMinEnvMsg, tempMaxEnvMsg, qtdMinMsg, qtdMaxMsg, restMinChip, restMaxChip, upload)
            else:
                janela['-uploadText-'].update(text_color='red', font=('helvetica',10,'bold')) 
        

    janela.close()
