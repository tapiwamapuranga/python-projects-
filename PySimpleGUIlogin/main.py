import PySimpleGUI as sg

#This is a class with all the contents of the main window
class Main:
    
    #the main window method
    def main(self):
        # Define the recipe or ingridient layout of the maain window
        layout1 = [
            [sg.Text("Select What you wanna do:")],
            [sg.Combo(['Recipe', 'Ingridient','Customized Recipe'], key='-COMBO-')],
            [sg.Button('Ok')]
        ]


        #defining the main window layout
        layout=[
            [sg.Text('Welcome to sevcor Recipe Recommendation'),sg.Button('MENU')],
            [layout1]
        ]

        # Creating the main  window
        window = sg.Window('Sevcor Recipe Recommendation', layout)

        # main Event selection loop
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Ok':
                selected_option = values['-COMBO-']
                sg.popup(f'You selected: {selected_option}')
                
            if event=='MENU':
                main1.menuDropdown()
                break
        pass
    
        # Closing the main window
        window.close()
    pass

    def menuDropdown(self):
        
        # Defining the layout of menu drop window
        layout = [
            [sg.Text("Menu Select:")],
            [sg.Listbox(['User Details', 'Change Password', 'Option 3'], size=(15, 3), key='-LISTBOX-')],
            [sg.Button('Submit')]
        ]

        # Creating the drop down window
        window = sg.Window('Drop-down List Example', layout)

        # menu drop down Event selection loop
        while True:
            event, values = window.read()

            if event == sg.WINDOW_CLOSED:
                break

            if event == 'Submit':
                selected_options = values['-LISTBOX-']
                sg.popup(f'You selected: {selected_options}')
        pass
    
        # Closing the drop down menu window
        window.close()
    pass
pass

main1=Main()