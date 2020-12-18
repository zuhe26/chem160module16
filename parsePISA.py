import xmltodict
import sys
#fd=open("interface-0.xml","r")
d=xmltodict.parse(sys.stdin.read())
residues=['RESIDUE1','RESIDUE2']
d1=d['INTERFACE']
d2=d1['RESIDUES']
for res in residues:
    d3=d2[res]
    d4=d3['RESIDUE']
    chain="A"
    chainid=[]
    aa=[]
    num=[]
    ASA=[]
    BSA=[]
    Gsolv=[]
    for i in d4:
        struct=i["STRUCTURE"]
        d5=struct.split()
        num.append(int(d5[1]))
        d6=d5[0].split(":")
        chainid.append(d6[0])
        aa.append(d6[1])
        d7=i["SOLVENTACCESSIBLEAREA"]
        ASA.append(float(d7))
        d8=i["BURIEDSURFACEAREA"]
        BSA.append(float(d8))
        d9=i["SOLVATIONENERGY"]
        Gsolv.append(float(d9))

    for i in range(len(num)):
        print("%3d %3s %1s %7.3f %7.3f %7.3f"%(num[i],aa[i],chainid[i],
                                               ASA[i],BSA[i],Gsolv[i]))

