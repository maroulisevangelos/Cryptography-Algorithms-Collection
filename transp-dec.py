#decrypts using transposition algorithm

enc_mes = "wl hlna otiw  ?wd0io0"

with open("output3.txt", "w") as f:
        # Write the value of the variable to the file
        f.write("")
        
for z in range(1,len(enc_mes)):
    key = z
    pr=[]
    print ("Key = " + str(key))

    t_plain_table = []
    help_table = []

    i=0
    while i<len(enc_mes):
        for y in range (len(enc_mes)//key):
            if (i>=len(enc_mes)):
                break
            plain_char = enc_mes[i]
            help_table.append(plain_char)
            i+=1
            
        t_plain_table.append(help_table)
        help_table = []

    plain_table = []
    

    
    for i in range (len(t_plain_table[0])):
        row = []
        for subtable in t_plain_table:
            if (i < len(subtable)):
                row.append(subtable[i])
        
        plain_table.append(row)
        

    pr = [element for subtable in plain_table for element in subtable] 
    plain_mes = "".join(map(str, pr))

    while (plain_mes[-1]== '0'):
        plain_mes = plain_mes[:-1]
        
    print("Plain message = " +plain_mes)
    
    with open("output3.txt", "a") as f:
        # Write the value of the variable to the file
        f.write(str(key) + "\n")
        f.write(str(plain_mes) + "\n")