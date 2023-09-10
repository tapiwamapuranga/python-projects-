import PySimpleGUI as sg


class LOGIN():
    
    password=""
    
    #this function is used to create new user in the system
    def userRegistration(self):
        
        #defining The layout and contents of the registration window
        layout = [
            [sg.Text('\t\t\tUser registration')],
            [sg.Text('Email\t\t', enable_events=True), sg.Input(key='-EMAIL-')],
            [sg.Text('User Name\t',enable_events=True), sg.Input(key='-USERNAME-')],
            [sg.Text('New Passord\t', enable_events=True), sg.Input(key='-NEWPASSWORD-',password_char='*')],
            [sg.Text('Confirm Password  ', enable_events=True), sg.Input(key='-CONFIRMPASSWORD-',password_char='*')],
            [sg.Button('Register', key='-REGISTERBTN-')]
        ]
        
        # creating the registration window
        window= sg.Window('Sevcor Kitchen cook',layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            
            if event == '-REGISTERBTN-':
                
                if values['-EMAIL-']!="" and values['-USERNAME-']!="":
                    if values['-NEWPASSWORD-']!="" and values['-CONFIRMPASSWORD-']!="":
                        if values['-NEWPASSWORD-']==values['-CONFIRMPASSWORD-']:
                            
                            p.password=values['-NEWPASSWORD-']
                            sg.popup_notify('New Password Created Success fully')
                        else: sg.popup_auto_close('passowrd dont match')
                    else: sg.popup_auto_close('ENTER NEW PASSWORD')
                else: sg.popup_auto_close('Please fill in  all details!!')
        pass
        window.Close()
    pass
            
        
    #This function is used to recover passwords
    def passwordRecovery(self):
        
        #defining The layout and contents of the password receovery window
        layout = [
            [sg.Text('\t\t\tPassword Recovery')],
            [sg.Text('Username'), sg.Input(key='-USERNAME-')],
            [sg.Text('Email\t'), sg.Input(key='-EMAIL-')],
            [sg.Button('Recover', key='-RECOVERBTN-'),sg.Exit()]
        ]

        # creating the set password window
        window= sg.Window('Sevcor Recipe Recommendation',layout)
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED,'Exit'):
                break        
            elif event=='-RECOVERBTN-':
                validation_result= LOGIN.validate(self,values)
                if validation_result[0]:
                    sg.popup('EMAIL SENT!')
                else:
                    error_message=LOGIN.generate_error_message(self,validation_result[1])
                    sg.popup(error_message)
        pass
        window.Close()
    pass
                
                
        
    #This function is used to reset new passwords
    def setPassword(self):
        
        #defining The layout and contents of the window
        layout = [
            [sg.Text('\t\t\tReset Password')],
            [sg.Text('OLD Passord\t', enable_events=True), sg.Input(key='-OLDPASSWORD-',password_char='*')],
            [sg.Text('New Passord\t', enable_events=True), sg.Input(key='-NEWPASSWORD-',password_char='*')],
            [sg.Text('Confirm Password  ', enable_events=True), sg.Input(key='-CONFIRMPASSWORD-',password_char='*')],
            [sg.Button('Create', key='-CREATEBTN-')]
        ]

        # creating the set password window
        window= sg.Window('Servcor Recipe Recommendation',layout)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            
            if event == '-CREATEBTN-':
                if values['-OLDPASSWORD-']==p.password:
                    if values['-NEWPASSWORD-']==values['-CONFIRMPASSWORD-']:
                        p.password=values['-NEWPASSWORD-']
                        sg.popup_notify('New Password Created Success fully')
                    else: sg.popup_auto_close('passowrd dont match')
                else: sg.popup_auto_close('INVALID OLD PASSWORD')
        pass
        window.Close()        
    pass

    #this function validates before sends a confirmation message
    def validate(self,values):
        is_valid =True
        values_invalid=[]
        
        if len(values['-USERNAME-'])==0:
            values_invalid.append('Name')
            is_valid=False
        
        if len(values['-EMAIL-'])==0:
            values_invalid.append('Email Address')
            is_valid=False
            
        if  '@' not in values['-EMAIL-']:
            values_invalid.append('Email missing @')
            is_valid=False
            
        result=[is_valid,values_invalid]
        return result
    pass

    def generate_error_message(self,values_invalid):
        error_message=''
        for value_invalid in values_invalid:
            error_message+=('\nInvalid :'+value_invalid)
        return error_message
    pass


    def login(self):
        
        check=False
        
        # creating layout of the window using lists
        layout = [
            [sg.Text('\t\tLogin Form', key='-HEADING-')],
            [sg.Text('Username', key='-USERNAME-'), sg.Input(key='-USERNAMEINPUT-')],
            [sg.Text('Password', key='-PASSWORD-'), sg.Input(key='-PASSWORDINPUT-',password_char='*')],
            [sg.Button('Login', key='-LOGINBTN-'), sg.Text('Forgot Password' ,text_color='red', enable_events=True, key='-PASSWORDRECOVERY-')],
            [sg.Text('Not yet registered',text_color='blue', enable_events=True, key='-REGISTER-')]
        ]

        # creating the window
        window = sg.Window('Servcor Recipe recommendation ',layout)

        # a looop that keeps the window open even if we press a button
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            
        #testing if username and password is correct
            if event == '-LOGINBTN-':
                if(values['-USERNAMEINPUT-'] == 'tapiwa'):
                    if(values['-PASSWORDINPUT-'] == 'MAPURANGA'):
                        sg.popup_notify('Login succcess full',location=(500,20))
                        check=True
                        break
                    else: sg.popup_error("Invalid Password!!")
                else: sg.popup_error("Invalid Username!!")
                
            if event=='-REGISTER-':
                log1.userRegistration()
                break
            
            if event=='-PASSWORDRECOVERY-':
                log1.passwordRecovery()
        pass
        window.Close()
        return check
    pass
pass

log1=LOGIN()
p=LOGIN()
