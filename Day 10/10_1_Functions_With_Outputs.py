# Functions with outputs

def format_name(f_name,l_name):
    
    '''What i thought before i get to know about 
       string_name.title() 
       function'''
    
    # list_f_name = list(f_name)
    # list_l_name = list(l_name)
    # list_correct_f_name = []
    # list_correct_l_name = []
    
    # for i in range (len(f_name)):
    #     if i==0:
    '''       the below is incorrect
              i.e.
              list_correct_f_name[i] = f_name[i].upper()
              is incorrect
    '''       
    #         list_correct_f_name.append(f_name[i].upper()) 
    '''       The above is correct'''
    #     else:
    #         list_correct_f_name.append(f_name[i].lower())
    
    # final_f_name = ''.join(list_correct_f_name)
    
    # for i in range (len(l_name)):
    #     if i==0:
    #         list_correct_l_name.append(l_name[i].upper())
    #     else:
    #         list_correct_l_name.append(l_name[i].lower())
    
    # final_l_name = ''.join(list_correct_l_name)
    
    # return f'{final_f_name} {final_l_name}'
    
    
    
    '''After i get to know about
       string_name.title() function'''
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f'{formated_f_name} {formated_l_name}'
    
    
    



# How to call the function?
formated_name = format_name("aBhIsHeK","gohEL")

print(formated_name)

# OR YOU CAN DIRECTLY PRINT:     print(format_name("aBhIsHeK","gohEL"))
# And the output will be the same