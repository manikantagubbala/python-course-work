import numpy as np

# 1.Array Creation 
# Write a NumPy program to create a 1D array of numbers from 10 to 50 (inclusive).
arr = np.arange(10,50,1)
print(f'{arr}\n')

# 2.Zeros and Ones 
# Create a 3×3 matrix with all elements equal to 0, and another with all elements equal to 1.

zero_one = np.zeros((3,3)), np.ones((3,3))
print(f'{zero_one}\n')

# 3.Identity Matrix 
# Generate a 5×5 identity matrix using NumPy.

id = np.eye(5,5)
print(f'{id}\n')

# 4.Reshape Array 
# Convert a 1D array of numbers from 1 to 12 into a 3×4 matrix.
arr = np.arange(1,13,1)
reshape_arr = arr.reshape(3,4)
print(f'{reshape_arr}\n')

# 5.Element-wise Operations 
# Create two NumPy arrays [1,2,3] and [4,5,6]. Perform element-wise addition, subtraction, multiplication, and division.
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
add, sub, mul, div = arr1 + arr2, arr1 - arr2, arr1 * arr2, arr1 / arr2
print(f"{add}\n{sub}\n{mul}\n{div}\n")

# 6.Array Slicing 
# Given an array from 1 to 20, extract elements from index 5 to 10.
arr = np.arange(1,21,1)
index_val = arr[5:11]
print(f"{index_val}\n")

# 7.Statistical Functions 
# Create an array of random numbers and find the mean, median, variance, and standard deviation.
arr  = np.arange(1,21,1)
mean = np.mean(arr)
median = np.median(arr)
print(f"Mean: {mean}\n{median}\n")


# 8. Index of Maximum and Minimum
# Create a NumPy array and find the indices of the maximum and minimum values.
arr = np.arange(1,11,1)
mx = np.argmax(arr)             # amx index
mn = np.argmin(arr)             # Min index
print(f"{mx}\n{mn}")







# 9.Sorting
# Generate a random array of size 10 and sort it in ascending order.

# 10.Broadcasting
# Add a 1D array [1, 2, 3] to each row of a 3×3 matrix of all 5’s using broadcasting.