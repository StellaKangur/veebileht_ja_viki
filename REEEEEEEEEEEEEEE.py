mehu = 90
koda = 20
aeg = 0

while mehu>=20.1:
    jahemehu = (mehu - koda) * 0.19
    mehu = mehu-jahemehu
    aeg+=1
    print("Supi temperatuur",aeg,". minutil on",round(mehu,2),"kraadi.")
