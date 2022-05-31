from hashlib import sha256
def _create(parms):
    if parms.get('faces') is None or parms['faces'] == '': 
        charid = _build('gybwro')
        hashedword = sha256(charid.encode('utf-8')).hexdigest()
        result = {'cube' : charid, 'integrity' : hashedword.upper(), 'status' : 'ok'}
        return result
    if len(parms['faces']) != 6:
        error01 = 'error: incorrect number of faces'
        result = {'status' : error01}
        return result
    for char in parms['faces']:
        if parms['faces'].count(char) > 1:
            error02 = 'error: Duplicate faces'
            result = {'status' : error02}
            return result
    charid = _build(parms['faces'])
    hashedword = sha256(charid.encode('utf-8')).hexdigest()
    result = {'cube' : charid, 'integrity' : hashedword.upper(), 'status' : 'ok'}
    return result

def _build(faces):
    charid = ''
    for char in faces:
        for i in range(9):
            charid += char
    return charid
