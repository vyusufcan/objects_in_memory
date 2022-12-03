# EVERYTHING IS OBJECT


print(object) # < class 'object' >

print(isinstance(5, object)) # True


print(isinstance([1,5,6],object)) # True

print(isinstance((1,5,6),object)) # True

print(isinstance("Hello World",object)) # True


def f(x):
    return x

print(isinstance(f, object))


class Movie:

    def __init__(self, title) -> None:
        self.title = title


print(isinstance(Movie, object))