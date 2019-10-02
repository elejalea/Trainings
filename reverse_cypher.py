AZ = []
for X in range(int(ord('A')), int(ord('Z'))+1):
    AZ.append(chr(X))
ZA = list(reversed(AZ))
az = [i.lower() for i in AZ]
za = list(reversed(az))
keys = AZ+az
values = ZA+za
cypher = dict(zip(keys, values))


# CAESAR CYPHER
# AZ = []
# for X in range(int(ord('A')), int(ord('Z'))+1):
#     AZ.append(chr(X))
# az = [i.lower() for i in AZ]
# keys = AZ+az
# values = keys[3:]+list(keys[:3])
# cypher = dict(zip(keys, values))


txt = input()
cyphered = ''
for i in txt:
    if i in cypher.keys():
        cyphered += cypher[i]
    else:
        cyphered += i
print(cyphered)

decypher = ''
for i in cyphered:
    if i in cypher.values():
        decypher += cypher[i]
    else:
        decypher += i
print(decypher)