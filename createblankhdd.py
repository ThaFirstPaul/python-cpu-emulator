f = open("/Users/paulvonlutzow/Desktop/MyContent/Programming/Python/16bit-singlebus-computer/hdd.txt","w")
for i in range(0,1024):
    if i== 1023:
        f.write("0000000000000000")
    else:
        f.write("0000000000000000\n")
f.close()
