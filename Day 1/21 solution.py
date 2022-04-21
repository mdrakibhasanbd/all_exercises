d = {"a":1, "b":2, "c":3}
print(d)
d = dict((key, b ) 
for key,b in d.items()
if b >=2)
print(d)