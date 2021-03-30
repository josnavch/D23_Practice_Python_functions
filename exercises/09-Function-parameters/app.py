# Your code goes here:
def render_person(nombre, bornday, eyes, age, gender):
   
    param = nombre + " is a " + str(age) + " years old "+ gender + " born in " + str(bornday) + " with " + eyes + " eyes" 
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))