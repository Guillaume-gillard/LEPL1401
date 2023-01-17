### Code to complete [START] ###

try :
    command = input ( "Enter your command: " )

except :
    print("There was an error")

parameters = command.split ()

if parameters[0] == "divide":
    try :
        print ( "The value of your division is: " + str (float(parameters[1])/float(parameters[2])))
    except :
        print("There was an error")
elif parameters[0] == "showfile":
    try :
        file = open ( parameters[1] )
        print ( file.read () )
        file.close ()
    except :
        print("There was an error")
else:
    print ( "Command not recognized")