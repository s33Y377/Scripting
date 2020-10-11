from collections import namedtuple
Point = namedtuple('Test', ['x', 'y'])
print("Point", Point)
p = Point(11, 22)
t = ["11", "22"]
print("p", p)
print(p.x, "||", p.y)
print("p.make", Point._make(t))
print("p asdict", p._asdict())
print("p replace", p._replace(x=33))
print(p.x)
