def square(x):
    """Return the square of a number.
    """
    return x**2.

def annotated_square(x: float) -> float:
    """Return the square of a number.
    """
    return x**2.

print(square(2.))
print(annotated_square(2.))
