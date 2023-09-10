import PySimpleGUI as sg

layout=[
    [
        sg.Input(key='-INPUT-'),sg.Spin(['Km to mile',
        'mile to Km','KG to pound','sec to Min'],key='-UNITS-'),
        sg.Button('Convert',key='-CONVERT-')
    ],
    [sg.Text('Output', key='-OUTPUT-')]
    
]


window=sg.Window('Converter',layout)

while True:
    event,values=window.read()
    
    if event ==sg.WIN_CLOSED:
        break
    
    if event=='-CONVERT-':
        input_value=float(values['-INPUT-'])
        match values['-UNITS-']:
            case 'Km to mile':
                output=round(input_value*0.6214)
                output_string=f'{input_value}km are {output}miles.'
            case 'mile to Km':
                    output=round(input_value/0.6214)
                    output_string=f'{input_value}miles are {output}Km.'
            case 'KG to pound':
                    output=round(input_value*2.20462)
                    output_string=f'{input_value}KG are {output}pounds.'
            case 'sec to Min':
                    output=round(input_value/60)
                    output_string=f'{input_value}seconds are {output}minutes.'
        window['-OUTPUT-'].update(output_string)
                    
            
        


window.close()