import PySimpleGUI as sg
from docx import Document
from datetime import datetime
import json

# Função para salvar o Número de Registro
def salvar_num_registro(num):
    with open('config.json', 'w') as file:
        json.dump({'num': num}, file)

# Função para carregar o Número de Registro
def carregar_num_registro():
    try:
        with open('config.json', 'r') as file:
            dado = json.load(file)
            if 'num' in dado:
                return int(dado['num'])
    except FileNotFoundError:
        print(f"Arquivo 'config.json' não encontrado.")
        return None

sg.theme('LightBlue')

layout = [
    [sg.HSep(color='black', pad=(10, 10))],
    [sg.Text('Número da Venda', expand_x=4), sg.Input(size=(30), justification='center', key='num_venda')],
    [sg.Text('Empreedimento', expand_x=4), sg.Input(size=(30), justification='center', key='empreed')],
    [sg.Text('Quadra', expand_x=4), sg.Input(size=(30), justification='center', key='quadra')],
    [sg.Text('Lote', expand_x=4), sg.Input(size=(30), justification='center', key='lote')],
    [sg.Text('Cliente', expand_x=4), sg.Input(size=(30), justification='center', key='cliente')],
    [sg.Text('Observação(s)', expand_x=4)],
    [sg.Input(size=(30), key='obs')],
    [sg.Button('Limpar')],
    [sg.HSep(color='black', pad=(10, 10))],
    [sg.Button('Gerar Contrato', key='gerar')]
]

janela = sg.Window("Gerador de Contratos", layout, size=(400,400), element_justification='center')
 
while True:
    event, values = janela.read()

    if event == sg.WIN_CLOSED:
        break
    
    doc = Document("contratos.docx")

    if event == 'gerar':

        ## Pegando data
        data = datetime.now()
        dia = data.day
        mes = data.month
        ano = data.year

        n_registro = carregar_num_registro()
        
        num_venda = values['num_venda']
        empreed = values['empreed']
        quadra = values['quadra']
        lote = values['lote']
        cliente = values['cliente']
        obs = values['obs']

        doc.add_paragraph(f"Número da Venda: {num_venda}")
        doc.add_paragraph(f"Número de Registro: {n_registro}")
        doc.add_paragraph(f"Data: {dia}/{mes}/{ano}")
        doc.add_paragraph(f"Empreendimento: {empreed}")
        doc.add_paragraph(f"Quadra: {quadra}")
        doc.add_paragraph(f"Lote: {lote}")
        doc.add_paragraph(f"Cliente: {cliente}")
        doc.add_paragraph(f"Obs: {obs}")
        doc.add_paragraph('')
        sg.popup(f'Contrato nº {n_registro} gerado com sucesso!')
        salvar_num_registro(n_registro + 1)

    doc.save("contratos.docx")

    if event == 'Limpar':
        janela['num_contrato'].update('')
        janela['local'].update('')
        janela['quadra'].update('')
        janela['lote'].update('')
        janela['cliente'].update('')
        janela['obs'].update('')
    
janela.close()