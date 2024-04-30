import PySimpleGUI as sg

def screen():
    sg.theme('LightGrey')

    cep = [
        [sg.Text('Informe o seu CEP: ', font='arial 12', pad=(0,0))],
        [sg.Input(size=(20, 0), font="arial 12", pad=(0, 0), key="cep")]
    ]

    column1 = [
        [sg.Text('LOGRADOURO: ', font="arial 12")],
        [sg.Text('BAIRRO: ', font="arial 12")],
        [sg.Text('LOCALIDADE: ', font="arial 12")],
        [sg.Text('UF: ', font="arial 12")],
        [sg.Text('DDD: ', font="arial 12")]
    ]

    column2 = [
        [sg.Input(font='arial 12 bold', key='logradouro', size=(35,1))],
        [sg.Input(font='arial 12 bold', key='bairro', size=(30,1))],
        [sg.Input(font='arial 12 bold', key='localidade', size=(30,1))],
        [sg.Input(font='arial 12 bold', key='uf', size=(4,1))],
        [sg.Input(font='arial 12 bold', key='ddd', size=(4,1))]
    ]

    button = [
        [sg.Button('Consultar', font='arial 12', size=(10,1), pad=((0,15), 0)),
         sg.CButton('Sair', font='arial 12', size=(8,1))
         ]
    ]

    layout = [
        [sg.Text('ConsultaCEP', font='arial 18 bold', pad=(10, 0))],
        [sg.Column(cep, justification='center', element_justification='center')],
        [sg.Column(column1, pad=((0, 20), 0)), sg.Column(column2)],
        [sg.Column(button, justification='center')]
    ]

    telaCep = sg.Window('ConsultaCEP', element_padding=(0, 10), layout=layout, size=(600, 500), finalize=True)

