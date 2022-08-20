height = float (input('enter your hight in meter = ')) 
weight = float (input('enter your weight in kg= ')) 
bmi = weight / (height ** 2) 
if 16 > bmi: 
    print ('you are slim')

elif 16 < bmi <= 18.5: 
    print ('body weight deficit') 

elif 18.5 < bmi <= 24: 
    print ('norm') 
    
elif 24 < bmi <= 30:
     print ('weight over') 

elif 30 < bmi <= 35: 
    print('obesity first degree') 

elif 35 < bmi <= 40: 
    print ('obesity second degree.') 

elif 40 < bmi: 
    print ('obesity third degree')