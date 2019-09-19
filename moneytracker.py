import sys
from function import process_file

weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


#Starting Balance
try:
    start_bal = float(input("Starting balance: $"))
except ValueError:
    print("Error: Cannot convert to float!")
    sys.exit()

    if start_bal < 0:
        print("Error: Must start with positive balance!")
        sys.exit()
    else:
        while True:
            print("")
            day = 0
            cmd = input("Enter command: ")
            #TRANSACTION COMMAND
            if cmd == "transaction":
                try:
                    trans = float(input("Enter amount: $"))
                except ValueError:
                    print("Error: Cannot convert to float!")
                    continue
                    if trans < 0:
                        trans = abs(trans)
                        start_bal = start_bal - trans
                    else:
                        start_bal = start_bal + trans
                
            # NEXT COMMAND    
            elif cmd == "next":
                if start_bal < 0:
                    print("Oh no! You're in debt!")
                    sys.exit()
                else:
                    print("Going to the next day...")
                    day += 1
                    
            #STATUS COMMAND
            elif:
                
            #REGULAR COMMAND
            elif:
            
            #HELP COMMAND
            elif:
            
            #QUIT COMMAND
            elif cmd == 'quit':
                print("Bye!")
                sys.exit()
            
            #ANYTHING ELSE
            else:
                print("Command not found.")
                print("Use the "help" command for a list of available commands")
                
                