# FileOperations.py

'''
# 'r' --> read
try:
    file = open('Sample.txt','r')
    read = file.read()
    file.seek(0)                                    # seek means again starts with first
    readlines = file.readlines()
    file.seek(0)
    readline = file.readline()
    print(f"\nRead the File: \n{read}")
    print(f"Readlines in the File: {readlines}\n")
    print(f"ReadLine in the File: {readline}\n")
except Exception as e:
    print(f"File is not in Your Folder {e}")

'''

# 'a' --> append

try:
    file = open("Sample.txt",'a')
except Exception as e:
    print(f"File not found {e}")
else:
    file.write("I am good at Python Developer.")
    file.close()
finally:
    print("Reset the Code.")

