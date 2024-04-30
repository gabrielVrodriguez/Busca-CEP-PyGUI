from interface import *
from consult import *


screen()

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Consultar':
         if event == 'Consultar':
            try:
                cep_value = values['cep']
                response_json = consult(cep_value)

                window['logradouro'].update(response_json['logradouro'])
                window['bairro'].update(response_json['bairro'])
                window['localidade'].update(response_json['localidade'])
                window['uf'].update(response_json['uf'])
                window['ddd'].update(response_json['ddd'])
            
            except Exception as e:
                sg.Popup('Verifique se o CEP foi preenchido corretamente')