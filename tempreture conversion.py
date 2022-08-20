option = int(input('for converting  °F to °C press 1:6'
  'for converting  °C to °F press 2:'
  'for converting  °C to °K press 3:' 
  'for converting  °K to °C press 4:'
  'for converting  °F to °K press 5:' 
  'and for converting  °K to °F press 6: '))
t = float(input('insert your tempreture = '))
if option == 1:
    C = 5/9*(t- 32)
    print('temperature=' , C , '°c')

elif option == 2:
    F = 9/5*t + 32
    print('temperature=' , F , '°F')

elif option == 3:
    K = t + 273
    print('temperature=' , K , '°K')

elif option == 4:
    C = t- 273
    print('temperature=' , C , '°c')

elif option == 5:
    K = 5/9*(t - 32) + 273
    print('temperature=' , K , '°K') 

elif option == 6:
    F = 9/5*(t - 273) + 32 
    print('temperature=' , F , '°F')


