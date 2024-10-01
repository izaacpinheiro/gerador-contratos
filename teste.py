import PySimpleGUI as sg

# Layout da janela
layout = [
    [sg.Text('Informe seu nome:'), sg.InputText(key='-NOME-')],
    [sg.Text('Informe sua idade:'), sg.InputText(key='-IDADE-')],
    [sg.Button('Clique-me', key='-BOTAO-', disabled=True)],
    [sg.Button('Sair')]
]

# Criando a janela
window = sg.Window('Exemplo de Desabilitar Botão', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    elif event == '-NOME-' and values['-NOME-'] and values['-IDADE-']:
        # Ativa o botão se ambos os campos estiverem preenchidos
        window['-BOTAO-'].update(disabled=False)
    elif event == '-IDADE-' and values['-NOME-'] and values['-IDADE-']:
        # Ativa o botão se ambos os campos estiverem preenchidos
        window['-BOTAO-'].update(disabled=False)
    elif event == '-BOTAO-':
        sg.popup(f"Nome: {values['-NOME-']}\nIdade: {values['-IDADE-']}")

# Fechando a janela
window.close()
