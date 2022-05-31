from hashlib import sha256
from RCube.cube import Cube
from RCube.cube import Block
from RCube.cube import Coordinate

def _check(parms):
    cubeError = _isValid(parms)
    if cubeError['status'] != 'valid':
        return cubeError
    if (_isFull(parms)):
        result = {'status' : 'full'}
        return result
    if (_isSpots(parms)):
        result = {'status' : 'spots'}
        return result
    if (_isCrosses(parms)):
        result = {'status' : 'crosses'}
        return result
    result = {'status': 'unknown'}
    return result

def _isValid(parms):
    if parms.get('cube') is None:
        result = {'status' : 'error: missing cube key'}
        return result
    if parms.get('integrity') is None:
        result = {'status' : 'error: missing integrity key'}
        return result
    if parms['cube'] == '':
        result = {'status' : 'error: missing cube value'}
        return result
    if parms['integrity'] == '':
        result = {'status' : 'error: missing integrity value'}
        return result
    if len(parms['cube']) != 54:
        result = {'status' : 'error: incorrect number of elements'}
        return result
    distinctValues = set(parms['cube'])
    if len(distinctValues) != 6:
        result = {'status' : 'error: incorrect number of distinct elements'}
        return result
    for color in distinctValues:
        if parms['cube'].count(color) != 9:
            result = {'status' : 'error: incorrect number of a element designator'}
            return result
    middleElements = parms['cube'][4:54:9]
    if len(set(middleElements)) != 6:
        result = {'status' : 'error: middle value are not distinct'}
        return result
    integrity = sha256(parms['cube'].encode('utf-8')).hexdigest().upper()
    if integrity != parms['integrity']:
        result = {'status' : 'error: cube does not match integrity value'}
        return result
    if _isImpossibleEdges(parms):
        result = {'status' : 'error: impossible edges'}
        return result
    if _isImpossibleCorners(parms):
        result = {'status' : 'error: impossible corners'}
        return result
    return {'status' : 'valid'}

def _isFull(parms):
    for element in range(1, 54):
        if (element % 9) != 0 and parms['cube'][element] != parms['cube'][element - 1]:
            return False
    return True

def _isSpots(parms):
    for element in range(1, 54):
        currElement = parms['cube'][element]
        prevElement = parms['cube'][element - 1]
        if (element % 9) != 0 and ((element - 4) % 9) != 0 and ((element - 5) % 9) != 0 and currElement != prevElement:
            return False
    return True

def _isCrosses(parms):
    cube = parms['cube']
    for i in range(6):
        firstElement = i * 9
        lastElement = (i + 1) * 9
        face = cube[firstElement : lastElement]
        if face[0] != face[2] or face[6] != face[8] or face[8] != face[0]:
            return False
        if len(set(face[3:6])) != 1 or face[1] != face[7] or face[1] != face[4]:
            return False
    return True

def _isImpossibleEdges(parms):
    cubeList = parms['cube']
    cube = Cube(cubeList)
    edges = cube.getEdges()
    for block in edges:
        if not (_isPossible(cubeList, block.getColors())):
            return True
    return False

def _isImpossibleCorners(parms):
    cubeList = parms['cube']
    cube = Cube(cubeList)
    corners = cube.getCorners()
    for block in corners:
        if not (_isPossible(cubeList, block.getColors())):
            return True
    return False

def _isPossible(cubeList, colors):
    opposites = {cubeList[4] : cubeList[22], cubeList[13] : cubeList[31], 
                cubeList[40] : cubeList[49]}
    if colors[0] == colors[1] or colors[1] == colors[2] or colors[0] == colors[2]:
        return False
    for i in range(3):
        op = opposites.get(colors[i])
        if op != None and (op == colors[i-1] or op == colors[(i+1)%3]):
            return False
    return True    
            
        