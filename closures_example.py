def value(x):
    def increment_by(y):
        return x+y
    return increment_by

increment10 = value(10)
print increment10(5)

increment45 = value(45)
print increment45(5)