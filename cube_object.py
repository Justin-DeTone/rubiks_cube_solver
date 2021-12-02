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


        #MUST FIX REFERENCES
        self.orange_face.setUp(self.white_face)
        self.orange_face.setDown(self.blue_face)
        self.orange_face.setLeft(self.yellow_face)
        self.orange_face.setRight(self.green_face)

        self.green_face.setUp(self.white_face)
        self.green_face.setDown(self.blue_face)
        self.green_face.setLeft(self.orange_face)
        self.green_face.setRight(self.red_face)

        self.red_face.setUp(self.white_face)
        self.red_face.setDown(self.blue_face)
        self.red_face.setLeft(self.green_face)
        self.red_face.setRight(self.yellow_face)

        self.yellow_face.setUp(self.white_face)
        self.yellow_face.setDown(self.blue_face)
        self.yellow_face.setLeft(self.red_face)
        self.yellow_face.setRight(self.orange_face)

        self.white_face.setUp(self.orange_face)
        self.white_face.setDown(self.red_face)
        self.white_face.setLeft(self.green_face)
        self.white_face.setRight(self.yellow_face)

        self.blue_face.setUp(self.red_face)
        self.blue_face.setDown(self.orange_face)
        self.blue_face.setLeft(self.green_face)
        self.blue_face.setRight(self.yellow_face)

test_face = Face("G")
test_face.display()
