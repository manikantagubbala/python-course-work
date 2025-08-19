import sys
import math
import platform
import random

print(sys.argv)
print(sys.path)
#sys.exit()



print(math.sqrt(25))
print(round(math.sqrt(25)))
print("Round: ",round(32.1),round(32.5),round(32.6),round(32.9))
print("Ceil: ", math.ceil(12.0), math.ceil(12.1), math.ceil(12.5), math.ceil(12.9))
print(math.pi)
print(math.e)
print("Floor: ", math.floor(23.0), math.floor(23.1), math.floor(23.5), math.floor(23.9))
print("We use floor in sqrt: ",math.floor(math.sqrt(5)))
print("Fabs Neg to Pos: ",math.fabs(-34),math.fabs(23))
print("neg to Pos: ",abs(-90), abs(643))
print("Factorial: ", math.factorial(6))
print("GCD of two numbers: ",math.gcd(24,18))
print("Cos : ", math.cos(45))
print("Tan:", math.tan(45))
print("Sin: ", math.sin(0))
print("Degree: ", math.degrees(math.pi))
print("Radians: ", math.radians(180))


print("\nAbout your system: ", platform.system())
print("About sys version: ", platform.release())
print("System Processor: ", platform.processor())

print("Random(): ")
print("It gives random value from 0 to 1: ", random.random())
print("It gives random values btwen a and b: ", random.randint(1,100))
print("It gives random float values btwen a and b: ", random.uniform(1,9))
names=['Manikanta', "Aditya", "Eswar", "Venky"]
print("It gives random value from names: ", random.choice(names))
print("It gives random values from names,but :", random.choices(names, k=2))
random.shuffle(names)
print("It gives shuffle: ", names)
