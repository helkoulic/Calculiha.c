# A cool calculator written in Python.
# Author: Helkoulic

# The Banner
print("""
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗     ██╗██╗  ██╗ █████╗    ██████╗ ██╗   ██╗
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██║██║  ██║██╔══██╗   ██╔══██╗╚██╗ ██╔╝
██║     ███████║██║     ██║     ██║   ██║██║     ██║███████║███████║   ██████╔╝ ╚████╔╝ 
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██║██╔══██║██╔══██║   ██╔═══╝   ╚██╔╝  
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║██║  ██║██║  ██║██╗██║        ██║   
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   """)
################ ########### ######### ####### ##### ### ## #


def calc(): 
    TYPE1 = input("|===(First Number)===> ")

    OPER =  input("|===(+|-|*|/)===> " )
    while OPER != "+" and OPER != "-" and OPER != "*" and OPER != "/" and OPER != "":
      print(f"ERROR!! '{OPER}' is not a valid operator.")
      calc()
      return

    TYPE2 = input("|===(Second Number)===> " )

    # RESULT = TYPE1 (+|-|*|/) TYPE2
    if OPER == "+":
        RESULT = float(TYPE1) + float(TYPE2)

    elif OPER == "-":
        RESULT = float(TYPE1) - float(TYPE2)

    elif OPER == "*":
        RESULT = float(TYPE1) * float(TYPE2)

    # Handle the ZeroDivisionError
    elif OPER == "/":
      try:
          RESULT = float(TYPE1) / float(TYPE2)
      except ZeroDivisionError:
        # Randomize the output each time this Error occurs
        RAN1= "GO TAKE A MATH COURSE!!"
        RAN2= "WHAT UNIVERSITY DO YOU LIVE IN??"
        RAN3= "OMG!! DID YOU EVEN STUDY?"
        if float(TYPE1) < 2:
          print(RAN3)
        elif float(TYPE1) == 2:
          print(RAN2)
        else:
          print(RAN1)
        return

    elif TYPE1 == "" or TYPE2 == "" or OPER == "":
      print()
      print("OW, YOU GONNA KILL ME RIGHT NOW :c")
      print("OKAY! TAKE CARE")
      exit()

    else:
        print("OooO My bad")


    # Print the result:
    print(f"|===> {TYPE1} {OPER} {TYPE2} = {'{0:g}'.format(RESULT)}")


# Run the calc fucntion and repeat it over and over again (exit when giving empty inputs)
REPEAT = True
while (REPEAT):
    calc()
