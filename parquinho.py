def distance_between_points(a, b):
    Ax = a[0] #1
    Ay = a[1] #6
    Bx = b[0] #4
    By = b[1] #2
    x = ((Ax-Bx)**2)+((Ay-By)**2)
    r = x **(1/2)
    return r

print(distance_between_points((-10.2,12.5), (0.3,14.7)))