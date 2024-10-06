class Demo:
    a = 4


o = Demo()
print(o.a)

o.a = 0
print(o.a)
print(Demo.a)  # class atrribute has not changed
