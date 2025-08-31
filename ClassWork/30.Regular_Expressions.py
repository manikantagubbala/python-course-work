# 30.Regular_Expressions.py
import re

#pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
#result = re.fullmatch(pattern,"Gubbala Bhuvana Manikanta")
#print(result.group() if result else "No Pattern")

password = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'
res = re.fullmatch(password,"M@ni1234")
print(res.group() if res else "No Pattern")