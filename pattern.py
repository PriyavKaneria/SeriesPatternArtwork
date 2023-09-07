# Best configs
# fibonacci: n = 325
# prime: n = 25,50,75,100
# square: n = 150,250,300
# cube: n = ?
# power: n = 12,20,22,24,27,42 ; seqLength = 500
# recaman: n = 125,250,725 ; seqLength = 2000

# Config
r = 300
n = 100
delta = 25
seqLength = 2000
sequence = "prime"
logging = False
changeNMenu = True
savePostScript = False # Requires PIL
# Available sequences = ["fibonacci", "prime", "square", "cube", "power", "recaman"]

# Libraries and initial settings
import turtle as t
t.speed("fastest")
t.tracer(0, 0)

if savePostScript:
    t.setup(r*2 + 204, r*2 + 208)

if changeNMenu:
    inc_button = t.Turtle(shape="triangle")
    inc_button.up()
    inc_button.goto(400, -300)
    inc_button.left(90)
    dec_button = t.Turtle(shape="triangle")
    dec_button.up()
    dec_button.goto(400, -340)
    dec_button.right(90)
    writer = t.Turtle()
    writer.ht()
    writer.up()
    writer.goto(400, -335)
    writer.down()
    writer.write(n, font=("Courier New", 20), align='center')

# Memory
coords = [t.position()]
curr_pos = -1
originalGeneratedSequence = []
moddedGeneratedSequence = []

# Sequences

# Fibonacci
class Fibonacci:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.b

# Prime
class Prime:
    def __init__(self):
        self.primes = [2]
        self.curr = 2

    def isPrime(self, num):
        for i in self.primes:
            if num % i == 0:
                return False
        return True

    def next(self):
        self.curr += 1
        while not self.isPrime(self.curr):
            self.curr += 1
        self.primes.append(self.curr)
        return self.curr

# Square
class Square:
    def __init__(self):
        self.curr = 0

    def next(self):
        self.curr += 1
        return self.curr ** 2

# Cube
class Cube:
    def __init__(self):
        self.curr = 0

    def next(self):
        self.curr += 1
        return self.curr ** 3

# Power
class Power:
    def __init__(self):
        self.curr = 0

    def next(self):
        self.curr += 1
        return self.curr ** self.curr

# Recaman
class Recaman:
    def __init__(self):
        self.curr = 0
        self.prev = 0
        self.n = 0
        self.nums = [0]

    def next(self):
        self.n += 1
        if self.curr - self.n > 0 and self.curr - self.n not in self.nums:
            self.curr -= self.n
        else:
            self.curr += self.n
        self.nums.append(self.curr)
        return self.curr

class Sequence:
    def __init__(self, sequence):
        self.sequence = sequence
        self.sequenceClass = None
        if self.sequence == "fibonacci":
            self.sequenceClass = Fibonacci(0, 1)
        elif self.sequence == "prime":
            self.sequenceClass = Prime()
        elif self.sequence == "square":
            self.sequenceClass = Square()
        elif self.sequence == "cube":
            self.sequenceClass = Cube()
        elif self.sequence == "power":
            self.sequenceClass = Power()
        elif self.sequence == "factorial":
            self.sequenceClass = Factorial()
        elif self.sequence == "recaman":
            self.sequenceClass = Recaman()

    def next(self):
        return self.sequenceClass.next()

# Helper functions
def resetMemory():
    global coords, curr_pos
    coords = []
    curr_pos = -1


def draw_circle():
    t.up()
    t.home()
    t.right(90)
    t.forward(r)
    t.left(90)
    t.down()
    t.circle(radius=r, steps=n)
    return


def draw_points():
    t.up()
    for i in range(n):
        t.circle(radius=r, steps=1, extent=360/n)
        coords.append(t.position())
        # t.down()
        # t.dot(3, "red")
        # t.up()
    return


def tgo(curr_pos):
    t.down()
    t.goto(coords[curr_pos])
    t.up()
    return

def calculate():
    global n, curr_pos
    _sequence = Sequence(sequence)
    for i in range(seqLength):
        nextNum = _sequence.next()
        mod = nextNum % n
        if logging:
            originalGeneratedSequence.append(nextNum)
            moddedGeneratedSequence.append(mod)
        curr_pos += mod
        curr_pos %= n
        tgo(curr_pos)


def redraw():
    global n, curr_pos
    tgo(-1)
    resetMemory()
    t.clear()
    draw_circle()
    draw_points()
    calculate()
    if logging:
        print("----------------------------------------")
        print("n = ", n)
        print(originalGeneratedSequence)
        print(moddedGeneratedSequence)


def increase_n(_x, _y):
    global n
    n += delta
    writer.clear()
    writer.write(n, font=("Courier New", 20), align='center')
    redraw()


def decrease_n(_x, _y):
    global n
    n -= delta
    if n <= 0:
        return
    if changeNMenu:
        writer.clear()
        writer.write(n, font=("Courier New", 20), align='center')
    redraw()


# Main pattern code
redraw()
if changeNMenu:
    inc_button.onclick(increase_n)
    dec_button.onclick(decrease_n)


# End
t.hideturtle()
t.update()

# PostScript
if savePostScript:
    from PIL import Image, EpsImagePlugin
    from os import path, mkdir, walk, remove
    import re
    from time import sleep
    if not path.exists("saves"):
        mkdir("saves")
    _, _, dirFiles = walk("saves").__next__()
    dirFiles.sort(key=lambda f: int(re.sub('\D', '', f)))
    if len(dirFiles) > 0:
        lastFile = dirFiles[-1]
        lastFile = int(re.sub('\D', '', lastFile))
        lastFile += 1
    else:
        lastFile = 1
    print("Saving image...")
    t.getscreen().getcanvas().postscript(file=f"./saves/pattern_{lastFile}.ps")
    sleep(1)
    img = Image.open(f"./saves/pattern_{lastFile}.ps")
    img.save(f"./saves/pattern_{lastFile}.png", "png")
    img.close()
    remove(f"./saves/pattern_{lastFile}.ps")
    print("Done!")

t.done()