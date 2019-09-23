import sys
from function import process_file

weekdays = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

try:
    if len(sys.argv) < 1:
        pass
        
    filestring = sys.argv[1]
    regtrans = process_file(filestring)
except IndexError:
    print("Error: Not enough command line arguments!")
    sys.exit()
except ValueError:
    print("Error: File not found!")
    sys.exit()
    
#Starting Balance
try:
    start_bal = float(input("Starting balance: $"))
    cur_bal = start_bal
except ValueError:
    print("Error: Cannot convert to float!")
    sys.exit()
except EOFError:
    print("Error: File not found!")
    sys.exit()

if start_bal <= 0:
    print("Error: Must start with positive balance!")
    
else:
    day = 0
    if day == 0 or day % 7 == 0:
        cur_bal = cur_bal + regtrans[0][0] - regtrans[1][0]
    while True:
        
        print("")
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
                cur_bal = cur_bal - trans
            else:
                cur_bal = cur_bal + trans

        #NEXT COMMAND    
        elif cmd == "next":
            if cur_bal < 0:
                print("Oh no! You're in debt!")
                break
            else:
                print("Going to the next day...")
                day += 1
                start_bal = cur_bal
                
            if day == 0 or day % 7 == 0:
                cur_bal = cur_bal + regtrans[0][0] - regtrans[1][0]
            elif day == 1 or day % 7 == 1:
                cur_bal = cur_bal + regtrans[0][1] - regtrans[1][1]
            elif day == 2 or day % 7 == 2:
                cur_bal = cur_bal + regtrans[0][2] - regtrans[1][2]
            elif day == 3 or day % 7 == 3:
                cur_bal = cur_bal + regtrans[0][3] - regtrans[1][3]
            elif day == 4 or day % 7 == 4:
                cur_bal = cur_bal + regtrans[0][4] - regtrans[1][4]
            elif day == 5 or day % 7 == 5:
                cur_bal = cur_bal + regtrans[0][5] - regtrans[1][5]
            elif day == 6 or day % 7 == 6:
                cur_bal = cur_bal + regtrans[0][6] - regtrans[1][6]

        #STATUS COMMAND
        elif cmd == "status":
            if day == 0 or day % 7 == 0:
                print("Day",str(day),"("+weekdays[0]+")")
            elif day == 1 or day % 7 == 1:
                print("Day",str(day),"("+weekdays[1]+")")
            elif day == 2 or day % 7 == 2:
                print("Day",str(day),"("+weekdays[2]+")")
            elif day == 3 or day % 7 == 3:
                print("Day",str(day),"("+weekdays[3]+")")
            elif day == 4 or day % 7 == 4:
                print("Day",str(day),"("+weekdays[4]+")")
            elif day == 5 or day % 7 == 5:
                print("Day",str(day),"("+weekdays[5]+")")
            elif day == 6 or day % 7 == 6:
                print("Day",str(day),"("+weekdays[6]+")")

            print("Starting balance: ${:.2f}".format(start_bal))
            print("Current balance: ${:.2f}".format(cur_bal))

            if start_bal < cur_bal:
                print("Nice work! You're in the black.")
            elif start_bal > cur_bal:
                print("Be careful! You're in the red.")
            else:
                pass

        #REGULAR COMMAND
        elif cmd == "regular":
            print("Regular Transactions:")
            print("Sun: +${:.2f} -${:.2f}".format(regtrans[0][0],regtrans[1][0]))
            print("Mon: +${:.2f} -${:.2f}".format(regtrans[0][1],regtrans[1][1]))
            print("Tue: +${:.2f} -${:.2f}".format(regtrans[0][2],regtrans[1][2]))
            print("Wed: +${:.2f} -${:.2f}".format(regtrans[0][3],regtrans[1][3]))
            print("Thu: +${:.2f} -${:.2f}".format(regtrans[0][4],regtrans[1][4]))
            print("Fri: +${:.2f} -${:.2f}".format(regtrans[0][5],regtrans[1][5]))
            print("Sat: +${:.2f} -${:.2f}".format(regtrans[0][6],regtrans[1][6]))

        #HELP COMMAND
        elif cmd == "help":
            print("The available commands are:")
            print('"transaction": Record a new income or expense')
            print('"next": Move on to the next day')
            print('"status": Show a summary of how you\'re doing today')
            print('"regular": Show a summary of your regular transactions')
            print('"help": Show this help message')
            print('"quit": Quit the program')

        #QUIT COMMAND
        elif cmd == 'quit':
            print("Bye!")
            break

        #ANYTHING ELSE
        else:
            print("Command not found.")
            print('Use the "help" command for a list of available commands')

