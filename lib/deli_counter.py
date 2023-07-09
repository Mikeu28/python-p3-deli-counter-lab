katz_deli = ["Logan", "Avi", "Spencer"]

def line(katz_deli):
    if katz_deli == []:
        print( "The line is currently empty." )
    else:
        message = "The line is currently:" 
        for index in range(len(katz_deli)):
            message += f' {index + 1}. {katz_deli[index]}'
        print(message)

def take_a_number( katz_deli, customer_name ):
    katz_deli.append(customer_name)
    number_in_line = len(katz_deli)
    print( f"Welcome, {customer_name}. You are number {number_in_line} in line." )

def now_serving(katz_deli):
    if katz_deli == []:
        print( "There is nobody waiting to be served!" )
    else:
        print( f"Currently serving {katz_deli[0]}." )
        del katz_deli[0]