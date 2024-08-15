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
if __name__ == '__main__':
   formated_name = format_name("aBhIsHeK","gohEL")
   print(formated_name)


''' If we print the formated_name outside the scope of if statement
    then whenever we import this module in any other file, 
    it will give an error, such as:-
    
      Traceback (most recent call last):
          File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 10\10_2_Multiple_Return_values.py", line 1, in <module>
              from _10_1_Functions_With_Outputs import format_name
          File "c:\Users\Abhishek Gohel\Desktop\Python 100 Days\Day 10\_10_1_Functions_With_Outputs.py", line 57, in <module>
              print(formated_name)
                    ^^^^^^^^^^^^^
      NameError: name 'formated_name' is not defined. Did you mean: 'format_name'?

'''



'''The comments below are for this file only'''
# OR YOU CAN DIRECTLY PRINT:     print(format_name("aBhIsHeK","gohEL"))
# And the output will be the same