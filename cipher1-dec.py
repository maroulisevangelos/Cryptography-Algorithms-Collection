#decrypts using caesar algorithm with 1 key
#code for puzzle 1


alphabet = "abcdefghijklmnopqrstuvwxyz "

enc_mes="ymnxerjxxfljenxejshwcuyjieanymefe jwcexnruqjehnumjw"

with open("output1.txt", "w") as f:
        # Write the value of the variable to the file
        f.write("")

for y in range (len(alphabet)):
    key = y
    print ("Key = " + str(key))
    plain_mes = ""
    for i in range (len(enc_mes)):
        plain_char = enc_mes[i]
        plain_mes += alphabet[alphabet.index(plain_char)-key% len(alphabet)]
    
    with open("output1.txt", "a") as f:
        # Write the value of the variable to the file
        f.write(str(key) + "\n")
        f.write(str(plain_mes) + "\n")
    print ("Plain message is = "+ plain_mes)
    




#puzzle1 
#enc_mes = "ymnxerjxxfljenxejshwcuyjieanymefe jwcexnruqjehnumjw"
#plain_mes = "this message is encrypted with a very simple cipher"
#key = 5
#Caesar algorithm using 1 key
#alphabet = "abcdefghijklmnopqrstuvwxyz "