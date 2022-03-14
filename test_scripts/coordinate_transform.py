
def tranform(value, min_old, max_old, min_new, max_new):
    range_old = max_old - min_old
    range_new = max_new - min_new

    return (value - min_old) / range_old * range_new + min_new

def transformX(value):
    return tranform(value, -114886.44, 61582.69, 14.83, 17.17)

def transformY(value):
    return tranform(value, 158944.80, 431704.35, 46.56, 49.02)
    
def transformXY(x, y):
    return (transformX(x), transformY(y))

x, y = (-96250.5, 319999.5)
x,y = (-97500.5, 319999.5)
print(transformXY(x,y))
