from rect import PyRectangle
from random import randint, seed

MAXINT = 100

seed()

passed = True
iteration = 0
while passed:
    x0, y0 = randint(-MAXINT, MAXINT), randint(-MAXINT, MAXINT)
    x1, y1 = x0 + randint(0, MAXINT), y0 + randint(0, MAXINT)
    pyRect = PyRectangle(x0, y0, x1, y1)
    dx, dy = 0, 0
    for i in range(2):
        if pyRect.getLength() != x1-x0:
            passed = False
        if pyRect.getHeight() != y1-y0:
            passed = False
        if pyRect.getArea() != (x1-x0)*(y1-y0):
            passed = False
        if not passed:
            print "x0=%u y0=%u x1=%u y1=%u dx=%u dy=%u" % (x0, y0, x1, y1, dx, dy)
        dx, dy = randint(-MAXINT, MAXINT), randint(-MAXINT, MAXINT)
        pyRect.move(dx, dy)
    print iteration
    iteration = iteration + 1
