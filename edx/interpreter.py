exp = input("Type Expression: ")

x, y, z = exp.split(" ")

new_x = float(x)
new_z = float(z)

if y == "+":
    output = new_x + new_z
    
if y == "-":
    output = new_x - new_z
    
if y == "*":
    output = new_x * new_z
    
if y == "/":
    output = new_x / new_z
    
print(round(output, 1))
