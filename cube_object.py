#Possible rubik's cube colors are as follows:
#Red, Blue, Green, Orange, Whie, Yellow

class Face:
    def __init__(self, color):
        #color takes the first letter of one of the above colors and initializes a cube face to that color
        self.face = [[color * 3], [color * 3], [color * 3]]

        #references to adjacent faces
        self.up = None
        self.down = None
        self.left = None
        self.right = None

    def setUp(self, reference):
        self.up = reference
    def setDown(self, reference):
        self.down = reference
    def setLeft(self, reference):
        self.left = reference
    def setRight(self, reference):
        self.right = reference

    def display(self):
        print(self.face[0])
        print(self.face[1])
        print(self.face[2])

class Cube(Face):
    def __init__(self):
        self.orange_face = Face("O")
        self.green_face = Face("G")
        self.red_face = Face("R")
        self.blue_face = Face("B")
        self.white_face = Face("W")
        self.yellow_face = Face("Y")


test_face = Face("G")
test_face.display()
