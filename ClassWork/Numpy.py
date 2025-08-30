# Numpy.py

import numpy as np

arr1 = np.array([1,2,3])
print(f'"1 - Dim Array" :\n{arr1}\n')

arr2 = np.array([[1,2,3],[4,5,6]])
print(f'"2 - Dim Array" :\n{arr2}\n')

arr3 = np.array([[[1,2],[3,4],[5,6]]])
print(f'"3 - Dim Array" :\n{arr3}\n')

zeroes = np.zeros((2,4,5))                                          # (2,4,5) = (array, row, col)
print(f"Zeroes: \n{zeroes}\n")

one = np.ones((2,5))                                                # (2,5) = (row, col)
print(f"Ones: \n{one}\n")

id = np.eye(4,4)                                                    # (4,4) = (row, col)
print(f"Identical matrix: \n{id}\n")

full_array = np.full((2,4),"Booked")                                # ((2,4),"Booked") = (row, col), "anyValue"
print(f"FullArray: \n{full_array}\n")

range_arr = np.arange(10,-1,-1)                                     # (10,-1,-1) = (start, end, step_value)
print(f"Range using Numpy: \n{range_arr}\n")

line_space = np.linspace(0,100,5)                                   # (0,100,5) = (start, end, how_many_parts_u_want)
print(f"Line Spaces: \n{line_space}\n")

rand_int = np.random.randint(1,7)                                   # 1=st_value, 7=end-val
print(f"It can give one number from given range: \n{rand_int}\n")

rand_ints = np.random.randint(1,7,2)                                # 1=st_value, 7=end-val, 2=step_value
print(f"It can give numbers (which are based on step value) from given range: \n{rand_ints}\n")

rand_int_arr = np.random.randint(1,7,(3,3))                          # 1=st_value, 7=end-val, (3,3)=(row,col)
print(f"It can give numbers (which are based on dimen array) from given range: \n{rand_int_arr}\n")

rand_float = np.random.rand(2,3)
print(f"Float Values: \n{rand_float}\n")
