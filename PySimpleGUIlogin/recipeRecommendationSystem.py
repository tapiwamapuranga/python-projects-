#importing the main and login classes
from loginForm import LOGIN
from main import Main

#creating objects of the classes(instentiating)
main=Main()
log=LOGIN()

if log.login()==True:
    main.main()
else: print("Application failed to load")

