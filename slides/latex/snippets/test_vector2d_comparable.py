from vector2d_comparable import Vector2d

v, z = Vector2d(3., -1.), Vector2d(3., 1.)
print(v >= z, v == z, v < z)
# This works even if we don't define the __gt__ method explicitly
print(v > z)

vector_list = [Vector2d(3., -1.), Vector2d(-5., 1.), Vector2d(3., 0.)]
print(vector_list)
# Tho make the following line work we need to implement either __ge__ and __lt__
# or __gt__ and __le__ (we need a complementary pair of operator)
vector_list.sort()
print(vector_list)
# Note: we got the full power of timsort for free! Nice :)
