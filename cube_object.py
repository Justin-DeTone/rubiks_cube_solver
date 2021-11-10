#Possible rubik's cube colors are as follows:
#Red, Blue, Green, Orange, Whie, Yellow

class Face:
    def __init__(self, color):
        #color takes the first letter of one of the above colors and initializes a cube face to that color
        self.face = [[color * 3], [color * 3], [color * 3]]

    def display(self):
        print(self.face[0])
        print(self.face[1])
        print(self.face[2])

test_face = Face("G")
test_face.display()
