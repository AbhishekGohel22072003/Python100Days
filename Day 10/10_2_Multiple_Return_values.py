'''If we do not return anything and we just type
   return
   and then whenever we try to print that function,
   it will print:-
   None

e.g.

def format_name(f_name,l_name):
    return

print(format_name('aBhishek','gOHel'))    
# This wiil print 
# None

'''


def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return formated_f_name,formated_l_name
    # This will return the 
    # TUPLE
    
    print('''This will not be printed
          as it is written 
          after returning the function...''')

print(format_name("aBhIshek",'gOHEL'))
# OUTPUT: ('Abhishek', 'Gohel') 
# as multiple returns will return
# a TUPLE