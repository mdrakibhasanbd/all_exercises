filename = input("Input the Filename: ")
filename = "abc.py"

print(type(filename))

f_extns = filename.split(".")

print("The extesion of the file is : " + repr(f_extns[-1]))