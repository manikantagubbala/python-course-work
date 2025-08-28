#

#try:
#    file = open('mani.txt','r')
#except Exception:
#    print("File Not Present")
#else:
#    read = file.read()
#
#    print(read)

with open('mani.txt','r+') as file:
    print(file.read())