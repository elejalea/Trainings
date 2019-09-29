while True:
    PRS = input()
    if PRS.endswith('o'):
        print('PRS1SG')
    elif PRS.endswith('as') or PRS.endswith('es'):
        print('PRS2SG')
    elif PRS.endswith('a') or PRS.endswith('e'):
        print('PRS3SG')
    elif PRS.endswith('amos') or PRS.endswith('emos') or PRS.endswith ('imos'):
        print('PRS1Pl')
    elif PRS.endswith('áis') or PRS.endswith('éis') or PRS.endswith('ís'):
        print('PRS2Pl')
    elif PRS.endswith('an') or PRS.endswith('en') or PRS.endswith('en'):
        print('PRS3Pl')
    elif PRS == '':
        break
    else:
        print('invalid form')