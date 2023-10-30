"""
Papildināt programmu ar ciklu, kurā sarakstā esošiem uzvārdiem tiktu 
pievienots klāt doktora nosaukums - Dr.
"""
"""

saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
sarakts2=[]

for uzvards in saraksts1:
    doktors="Dr. "+uzvards
    saraksts2. append(doktors)

print(saraksts2)


"""


#2.variants
saraksts1=["Kalniņš", "Opmanis", "Vēzis", "Almane"]
saraksts2=[]
def pievienot_dok(uzvards):
    return "Dr.  "+uzvards

saraksts2=list(map(pievienot_dok, saraksts1))
print(saraksts2)
