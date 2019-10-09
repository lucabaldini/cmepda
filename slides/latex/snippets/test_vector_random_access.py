from vector_random_access import Vector

v = Vector([5., 3., -1, 8.])

print(len(v))

print(v[0], v[1])

v[1] = 10.
print(v)

print (v[9]) # This will generate an error!
