# This function estimates the pi value by creating square grid points centered at the origin (0,0) with a given step-size value
# Pi=3.141592653589793

def Calculate_Pi(StepeSize):
    # For a 2-unit square we set:
    Ymin, Ymax, Xmin, Xmax = -1, 1, -1, 1
    X, Y = [], []
    # Creating grid points inside the 2-unit square  including the square perimeter
    while Ymin <= Ymax:
        while Xmin <= Xmax:
            X.append(Xmin)
            Y.append(Ymin)
            Xmin += StepeSize
        Xmin = -1
        Ymin += StepeSize
    Nc = 0  # Nc is the number of grid points inside the unit circle

    for i in range(len(X)):
        if ((X[i]) ** 2 + (Y[i]) ** 2) <= 1:
            Nc += 1
    # (area of a square/area of a circle)=4/pi=Total grid points/Nc => pi=4*Nc/Total grid points
    Pi = 4 * Nc / len(X)
    return ("The value of Pi with the given step-size is: ", Pi)


# Example with step-size=0.001 pi=3.141529

print(Calculate_Pi(0.001))

