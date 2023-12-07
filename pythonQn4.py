#qn4i)
list=(1,12,123,1234,12345)
for x in list:
 print(x)
    
    #qn4iii)
a=3
b=4
c=(3+4)
def sum(a,b):
  print(f"The sum of {a} and {b} is {c}")
sum(3,4)
    
    
    
    
    #iv)
class car:
  def __init__(modal, brand, year):
       modal.brand = brand
       modal.year = year
#create a car class with properties ie brand,year.
class car:
  def __init__(modal, brand, year):
    modal.brand= brand
    modal.year = year
    
b1 = car("toyota", 2023)

print(b1.brand)
print(b1.year)
#v)
# creating an object
b1=car("toyota",2023,) 

# printing the car brand and year
print(f'brand is {b1.brand} and year is {b1.year}')