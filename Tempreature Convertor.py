User_Input = input('What is the unit of tempretature you want to measure in? (F) for Farenheit, (C) for Celcius: and (K) for Kelvin: ' )
User_Input_Degree = int(input('What is the degree of your unit of tempreature?: '))
User_Input2 = input('What is the unit of tempretature you want to Convert in? (F) for Farenheit, (C) for Celcius: and (K) for Kelvin: ' )


if User_Input == 'C' and User_Input2 == 'F':
    answer = User_Input_Degree - 32 * 5/9

'''if User_Input == 'C':
    answer = User_Input_Degree * 1.8 + 32 

if User_Input == 'K':
    answer = User_Input_Degree - 273.15 * 9/5 + 32
'''
print(f'Your degree in the opposite unit of Tempretature is {answer} degrees.')