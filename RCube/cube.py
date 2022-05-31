class Cube:
    def __init__(self, cubeList):
        self.cubeList = cubeList
        self.corners = (Block(Coordinate(-1,1,1), [cubeList[29], cubeList[42], cubeList[0]]),
                     Block(Coordinate(1,1,1), [cubeList[9], cubeList[44], cubeList[2]]),
                     Block(Coordinate(-1,-1,1), [cubeList[35], cubeList[45], cubeList[6]]),
                     Block(Coordinate(1,-1,1), [cubeList[15], cubeList[47], cubeList[8]]),
                     Block(Coordinate(-1,1,-1), [cubeList[27], cubeList[36], cubeList[20]]),
                     Block(Coordinate(1,1,-1), [cubeList[11], cubeList[38], cubeList[18]]),
                     Block(Coordinate(-1,-1,-1), [cubeList[33], cubeList[51], cubeList[26]]),
                     Block(Coordinate(1,-1,-1), [cubeList[17], cubeList[53], cubeList[24]]))
        self.edges = (Block(Coordinate(0,1,1), [None, cubeList[43], cubeList[1]]),
                   Block(Coordinate(-1,0,1), [cubeList[32], None, cubeList[3]]),
                   Block(Coordinate(1,0,1), [cubeList[12], None, cubeList[5]]),
                   Block(Coordinate(0,-1,1), [None, cubeList[46], cubeList[7]]),
                   Block(Coordinate(0,1,-1), [None, cubeList[37], cubeList[19]]),
                   Block(Coordinate(-1,0,-1), [cubeList[30], None, cubeList[23]]),
                   Block(Coordinate(1,0,-1), [cubeList[14], None, cubeList[21]]),
                   Block(Coordinate(0,-1,-1), [None, cubeList[52], cubeList[25]]),
                   Block(Coordinate(-1,1,0), [cubeList[28], cubeList[39], None]),
                   Block(Coordinate(-1,-1,0), [cubeList[34], cubeList[48], None]),
                   Block(Coordinate(1,1,0), [cubeList[10], cubeList[41], None]),
                   Block(Coordinate(1,-1,0), [cubeList[16], cubeList[50], None]))
        self.middle = (Block(Coordinate(0,0,1), [None, None, cubeList[4]]),
                   Block(Coordinate(1,0,0), [cubeList[13], None, None]),
                   Block(Coordinate(0,0,-1), [None, None, cubeList[22]]),
                   Block(Coordinate(-1,0,0), [cubeList[31], None, None]),
                   Block(Coordinate(0,1,0), [None, cubeList[40], None]),
                   Block(Coordinate(0,-1,0), [None, cubeList[49], None]))
        self.blocks = self.corners + self.edges + self.middle
        
    def getCorners(self):
        return self.corners
        
    def getEdges(self):
        return self.edges
        
    def getMiddle(self):
        return self.middle
        
    def getBlocks(self):
        return self.blocks
    
class Block:
    def __init__(self, position, colors):
        self.position = position
        self.colors = colors
        self._setType()
        
    def _setType(self):
        if self.colors.count(None) == 0:
            self.type = 'corner'
        elif self.colors.count(None) == 1:
            self.type = 'edge'
        elif self.colors.count(None) == 2:
            self.type = 'middle'
    def getPosition(self):
        return self.position
    
    def getColors(self):
        return self.colors
    
    def getType(self):
        return self.type

class Coordinate:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def getCoordinates(self):
        return [self.x, self.y, self.z]