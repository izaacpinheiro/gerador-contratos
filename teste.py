import PySimpleGUI as sg

# Layout
layout = [
    [sg.Text('Nome:'), sg.Input(key='-NOME-')],
    [sg.Text('Idade:'), sg.Input(key='-IDADE-')],
    [sg.Button('Enviar', key='-ENVIAR-', disabled=True), sg.Button('Sair')]
]

# Janela
janela = sg.Window('Exemplo de Habilitar Botão').Layout(layout)

while True:
    event, values = janela.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break

    nome = values['-NOME-']
    idade = values['-IDADE-']

    # Verifica se ambos os campos estão preenchidos
    if nome.strip() and idade.strip():
        janela['-ENVIAR-'].update(disabled=False)  # Ativa o botão Enviar se os campos estiverem preenchidos
    else:
        janela['-ENVIAR-'].update(disabled=True)  # Desativa o botão Enviar se algum campo estiver vazio

    if event == '-ENVIAR-':
        sg.popup(f'Nome: {nome}\nIdade: {idade}')

janela.close()
