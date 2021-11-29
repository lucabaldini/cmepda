from vector_ducked import Vector
       
v = Vector([1., 2., 3.])
t = Vector([1., 2., 3., 4.])
z = Vector([1., 2., 5.])
u = Vector([1., 2., 3.])

print(v)
print(abs(v))
print(sum(v))
print(v == t, v == z, v == u)
print(v+z)
print(v+t) # Note the result: this is due to the behaviour of zip()!
