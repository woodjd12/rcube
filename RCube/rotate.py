import RCube.check as check
from RCube.cube import Cube
from RCube.cube import Block
from RCube.cube import Coordinate
from hashlib import sha256

def _rotate(parms):
    rotations = {'f':_f,'F':_F,'r':_r,'R':_R,'b':_b,'B':_B,'l':_l,'L':_L,'t':_t,'T':_T,'u':_u,'U':_U}
    cubeError = check._isValid(parms)
    if cubeError['status'] != 'valid':
        return cubeError
    result = {'rotate': 'rotate stub'}
    if parms.get('side') is None:
        result = {'status' : 'error: missing side key'}
        return result
    if parms['side'] == '':
        result = {'status' : 'error: missing side value'}
        return result
    if rotations[parms['side']] is None:
        result = {'status' : 'error: invalis rotation'}
    cubeList = parms['cube']
    newCube = rotations[parms['side']](cubeList)
    integrity = sha256(newCube.encode('utf-8')).hexdigest().upper()
    result = {'status':'rotated', 'cube': newCube, 'integrity': integrity}
    return result

def _f(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.z == 1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(-y, x, z, blocks)
            if block.colors[0] is not None and block.colors[1] is None:
                block.colors[0] += newBlock.colors[1][0]
            elif block.colors[0] is None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[0] += newBlock.colors[1][0]
                block.colors[1] += newBlock.colors[0][0]
    return _writeList(blocks)

def _F(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.z == 1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(y, -x, z, blocks)
            if block.colors[0] is not None and block.colors[1] is None:
                block.colors[0] += newBlock.colors[1][0]
            elif block.colors[0] is None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[0] += newBlock.colors[1][0]
                block.colors[1] += newBlock.colors[0][0]
    return _writeList(blocks)

def _r(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.x == 1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(x, -z, y, blocks)
            if block.colors[1] is not None and block.colors[2] is None:
                block.colors[1] += newBlock.colors[2][0]
            elif block.colors[1] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[1][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[1][0]
    return _writeList(blocks)    

def _R(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.x == 1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(x, z, -y, blocks)
            if block.colors[1] is not None and block.colors[2] is None:
                block.colors[1] += newBlock.colors[2][0]
            elif block.colors[1] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[1][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[1][0]
    return _writeList(blocks)    


def _b(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.z == -1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(y, -x, z, blocks)
            if block.colors[0] is not None and block.colors[1] is None:
                block.colors[0] += newBlock.colors[1][0]
            elif block.colors[0] is None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[0] += newBlock.colors[1][0]
                block.colors[1] += newBlock.colors[0][0]
    return _writeList(blocks)

def _B(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.z == -1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(-y, x, z, blocks)
            if block.colors[0] is not None and block.colors[1] is None:
                block.colors[0] += newBlock.colors[1][0]
            elif block.colors[0] is None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[0] += newBlock.colors[1][0]
                block.colors[1] += newBlock.colors[0][0]
    return _writeList(blocks)

def _l(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.x == -1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(x, z, -y, blocks)
            if block.colors[1] is not None and block.colors[2] is None:
                block.colors[1] += newBlock.colors[2][0]
            elif block.colors[1] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[1][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[1][0]
    return _writeList(blocks)   

def _L(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.x == -1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(x, -z, y, blocks)
            if block.colors[1] is not None and block.colors[2] is None:
                block.colors[1] += newBlock.colors[2][0]
            elif block.colors[1] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[1][0]
            elif block.colors[0] is not None and block.colors[1] is not None:
                block.colors[1] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[1][0]
    return _writeList(blocks)

def _t(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.y == 1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(z, y, -x, blocks)
            if block.colors[0] is not None and block.colors[2] is None:
                block.colors[0] += newBlock.colors[2][0]
            elif block.colors[0] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[2] is not None:
                block.colors[0] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[0][0]
    return _writeList(blocks)

def _T(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.y == 1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(-z, y, x, blocks)
            if block.colors[0] is not None and block.colors[2] is None:
                block.colors[0] += newBlock.colors[2][0]
            elif block.colors[0] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[2] is not None:
                block.colors[0] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[0][0]
    return _writeList(blocks)

def _u(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.y == -1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(-z, y, x, blocks)
            if block.colors[0] is not None and block.colors[2] is None:
                block.colors[0] += newBlock.colors[2][0]
            elif block.colors[0] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[2] is not None:
                block.colors[0] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[0][0]
    return _writeList(blocks)

def _U(cubeList):
    cube = Cube(cubeList)
    blocks = cube.getBlocks()
    for block in blocks:
        if block.position.y == -1:
            x = block.position.x
            y = block.position.y
            z = block.position.z
            newBlock = _search(z, y, -x, blocks)
            if block.colors[0] is not None and block.colors[2] is None:
                block.colors[0] += newBlock.colors[2][0]
            elif block.colors[0] is None and block.colors[2] is not None:
                block.colors[2] += newBlock.colors[0][0]
            elif block.colors[0] is not None and block.colors[2] is not None:
                block.colors[0] += newBlock.colors[2][0]
                block.colors[2] += newBlock.colors[0][0]
    return _writeList(blocks)

def _writeList(blocks):
    cubeList = [None] * 54
    cubeList[29] = blocks[0].colors[0][-1]
    cubeList[42] = blocks[0].colors[1][-1]
    cubeList[0] = blocks[0].colors[2][-1]
    cubeList[9] = blocks[1].colors[0][-1]
    cubeList[44] = blocks[1].colors[1][-1]
    cubeList[2] = blocks[1].colors[2][-1]
    cubeList[35] = blocks[2].colors[0][-1]
    cubeList[45] = blocks[2].colors[1][-1]
    cubeList[6] = blocks[2].colors[2][-1]
    cubeList[15] = blocks[3].colors[0][-1]
    cubeList[47] = blocks[3].colors[1][-1]
    cubeList[8] = blocks[3].colors[2][-1]
    cubeList[27] = blocks[4].colors[0][-1]
    cubeList[36] = blocks[4].colors[1][-1]
    cubeList[20] = blocks[4].colors[2][-1]
    cubeList[11] = blocks[5].colors[0][-1]
    cubeList[38] = blocks[5].colors[1][-1]
    cubeList[18] = blocks[5].colors[2][-1]
    cubeList[33] = blocks[6].colors[0][-1]
    cubeList[51] = blocks[6].colors[1][-1]
    cubeList[26] = blocks[6].colors[2][-1]
    cubeList[17] = blocks[7].colors[0][-1]
    cubeList[53] = blocks[7].colors[1][-1]
    cubeList[24] = blocks[7].colors[2][-1]
    cubeList[43] = blocks[8].colors[1][-1]
    cubeList[1] = blocks[8].colors[2][-1]
    cubeList[32] = blocks[9].colors[0][-1]
    cubeList[3] = blocks[9].colors[2][-1]
    cubeList[12] = blocks[10].colors[0][-1]
    cubeList[5] = blocks[10].colors[2][-1]
    cubeList[46] = blocks[11].colors[1][-1]
    cubeList[7] = blocks[11].colors[2][-1]
    cubeList[37] = blocks[12].colors[1][-1]
    cubeList[19] = blocks[12].colors[2][-1]
    cubeList[30] = blocks[13].colors[0][-1]
    cubeList[23] = blocks[13].colors[2][-1]
    cubeList[14] = blocks[14].colors[0][-1]
    cubeList[21] = blocks[14].colors[2][-1]
    cubeList[52] = blocks[15].colors[1][-1]
    cubeList[25] = blocks[15].colors[2][-1]
    cubeList[28] = blocks[16].colors[0][-1]
    cubeList[39] = blocks[16].colors[1][-1]
    cubeList[34] = blocks[17].colors[0][-1]
    cubeList[48] = blocks[17].colors[1][-1]
    cubeList[10] = blocks[18].colors[0][-1]
    cubeList[41] = blocks[18].colors[1][-1]
    cubeList[16] = blocks[19].colors[0][-1]
    cubeList[50] = blocks[19].colors[1][-1]
    cubeList[4] = blocks[20].colors[2][-1]
    cubeList[13] = blocks[21].colors[0][-1]
    cubeList[22] = blocks[22].colors[2][-1]
    cubeList[31] = blocks[23].colors[0][-1]
    cubeList[40] = blocks[24].colors[1][-1]
    cubeList[49] = blocks[25].colors[1][-1]
    cubeString = ''
    for i in cubeList:
        cubeString += i
    return cubeString
def _search(targetx, targety, targetz, blocks):
    for block in blocks:
        x = block.position.x
        y = block.position.y
        z = block.position.z
        if x == targetx and y == targety and z == targetz:
            return block
    return None