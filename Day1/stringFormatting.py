a=42
b=13.14256935
c="hello"
e=56314552145562

r = "a is %d"%a
print(r)
r="%10d%f"%(a,b)
print(r)
r="%+010d%E"%(a,b)
print(r)