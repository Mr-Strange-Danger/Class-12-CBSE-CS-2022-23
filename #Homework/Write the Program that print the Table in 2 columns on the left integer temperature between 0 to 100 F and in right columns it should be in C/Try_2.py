#Using Visual Studio Code
#Main User using Git Service with GitHub
#Made on apr 12 13:42:42 2022


print(' For Converting Temperature into Celsius , Fahrenheit and Kelvin .')
print(' For Converting Celsius to Fahrenheit and Kelvin   -=-  Type "009"')
print(' For Converting Fahrenheit to Celsius and Kelvin   -=-  Type "008"')
print(' For Converting Kelvin to Celsius and Fahrenheit   -=-  Type "007"')
in1=int(input(' Enter Your Result.  >>>  '))
if in1==9:
    ct1=int(input(' Enter Temperature in Celsius  -=-  '))
    ft1=(ct1*1.8)+32
    kt1=float(ct1)+273.15
    print(' Temperature in Celsius      :  ',ct1,' °C')
    print(' Temperature in Fahrenheit   :  ',ft1,' °F')
    print(' Temperature in Kelvin       :  ',kt1,' K')
elif in1==8:
    ft2=int(input(' Enter Temperature in Fahrenheit  -=-  '))
    ct2=((ft2-32)/1.8)
    kt2=float(ct2)+273.15
    print(' Temperature in Fahrenheit   :  ',ft2,' °F')
    print(' Temperature in Celsius      :  ',ct2,' °C')
    print(' Temperature in Kelvin       :  ',kt2,' K')
elif in1==7:
    kt3=float(input(' Enter Temperature in Kelvin  -=-  '))
    ct3=kt3-273.15
    ft3=(ct3*1.8)+32
    print(' Temperature in Kelvin       :  ',kt3,' K')
    print(' Temperature in Celsius      :  ',ct3,' °C')
    print(' Temperature in Fahrenheit   :  ',ft3,' °F')
else:
    print(' # Please Try Again #\n # Enter Information Properly #')


#Project Completed at apr 12 14:00:58 2022
#Project Completed with Visual Studio Code
#Support Visual Studio Code
