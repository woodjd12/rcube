from hashlib import sha256
integrity = '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'
cube = 'gggggggggrrrrrrrrrbbbbbbbybooooooooowwwwwwwwwybyyyyyyy'
expectedIntegrity = sha256(cube.encode('utf-8')).hexdigest().upper()
print(expectedIntegrity)
print(len(cube))
if integrity != expectedIntegrity:
    print('false')
else:
    print('true')
        