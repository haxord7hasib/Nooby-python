#----------no matter------------#
name1 = "Hasib" 
height1_foot = 5.7 
weight1_kg = 90 
age1= 24
name2 = "Ruzbelt"
height2_foot = 5.7
weight2_kg = 55
age2 = 23
name3 = "Nahid"
height3_foot=5.5
weight3_kg=65.5
age3 = 23 
def power(name,weight_kg,height_foot,age):
  individual_power = weight_kg*height_foot/(age**2)
  print("Power:")
  print(individual_power)
  if individual_power>0.80:
   print(name + " is Powerfull")
  elif individual_power<0.60:
   print(name + " is too much weak")
  else:
   print(name + " is weak")

power(name1,weight1_kg,height1_foot,age1)
power(name2,weight2_kg,height2_foot,age2)
power(name3,weight3_kg,height3_foot,age3)
