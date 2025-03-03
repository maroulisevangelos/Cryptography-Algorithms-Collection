#decrypts using caesar algorithm with 2 keys
#code for puzzle 2


alphabet = "abcdefghijklmnopqrstuvwxyz ,."

enc_mes = "lbldicljs,aeyqbk.,yzimliityqpdrbtisqxtb pcljtvttyrivzc kbx.qavtxyjtibribzztvttyriv.o jldlbgibrifs,weae  phjqldoqb pe.xb,ntwqm,zbzztibsijchtdrqetaqs,r woi,yywkpdb,lbi,yqb pqoxdxwe cpdbqzyijsxzhpjtvlbivzc kbx.qavtxyvprif.ed,o,yzitiyzhxtw,atb,zdieqqb pqneyvpfbiieqqlbre.,b xqldoqnexfcjljteyqe,b ijsxijchtdrqxtn tdprims,n ivldiupqneyitwphpwiticzwpbieqqlqrxyx.twq k.fzipqnexfcjphkqsxi,aqe,oxwoivzda,ox.xoqbeiupqb pqqtb phieqqb pe.xb,ntwqnexfcjphiin,pdnxitywit.jtytvttwqtdbxwbtzpdnxk"

with open("output2.txt", "w") as f:
        # Write the value of the variable to the file
        f.write("")

for k in range (len(alphabet)):
    key1 = k

    for z in range (len(alphabet)):
        key2 = z
        print("Key1 = ", key1);
        print("Key2 = ", key2);
        plain_mes = ""

        for i in range (len(enc_mes)):
            plain_char = enc_mes[i]
            if (i % 2 == 0):
                plain_mes += alphabet[(alphabet.index(plain_char)-key1)%len(alphabet)]
            else :
                plain_mes += alphabet[(alphabet.index(plain_char)-key2)%len(alphabet)]
                
        with open("output2.txt", "a") as f:
            # Write the value of the variable to the file
            f.write(str(key1) + "\n")
            f.write(str(key2) + "\n")
            f.write(str(plain_mes) + "\n")
        
        print ("Plain message = " + plain_mes)
        

#puzzle2
#enc_mes = "lbldicljs,aeyqbk.,yzimliityqpdrbtisqxtb pcljtvttyrivzc kbx.qavtxyjtibribzztvttyriv.o jldlbgibrifs,weae  phjqldoqb pe.xb,ntwqm,zbzztibsijchtdrqetaqs,r woi,yywkpdb,lbi,yqb pqoxdxwe cpdbqzyijsxzhpjtvlbivzc kbx.qavtxyvprif.ed,o,yzitiyzhxtw,atb,zdieqqb pqneyvpfbiieqqlbre.,b xqldoqnexfcjljteyqe,b ijsxijchtdrqxtn tdprims,n ivldiupqneyitwphpwiticzwpbieqqlqrxyx.twq k.fzipqnexfcjphkqsxi,aqe,oxwoivzda,ox.xoqbeiupqb pqqtb phieqqb pe.xb,ntwqnexfcjphiin,pdnxitywit.jtytvttwqtdbxwbtzpdnxk"
#Plain message = alan mathison turing was an english mathematician, computer scientist, logician, cryptanalyst, philosopher, and theoretical biologist. turing was highly influential in the development of theoretical computer science, providing a formalisation of the concepts of algorithm and computation with the turing machine, which can be considered a model of a general purpose computer. he is widely considered to be the father of theoretical computer science and artificial intelligence.
#Key1 =  11
#Key2 =  19
#Caesar Algorithm using 2 keys
#alphabet = "abcdefghijklmnopqrstuvwxyz ,."