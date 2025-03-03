#firstly decrypts ciphertext using transposition algorithm and then decrypts using caesar algorithm with 1 key
#code for puzzle 4

enc_mes_first = "jye,---nexjnxoummxw,eoqxx,0ejrjnrrwcnl,wy-qlevmqe,eafxehwle-uno.q.,um n xxeejqexn .,rexmnye,lke-nnnjeeunux-enwewav,wnnwlx q,lknm.-qtnrn blamumvweg eeyge.qevjn..rnqqkvek,n-ewewy.-nxeenlex0r ejlj,h w p,eej-x,ujfeye,-x e-lvv  qpnwxjuqwniu,rqcuj gwxr,jlr xe-rrrtjxjrn. eow eejice,eexuue-eln xlne,r,wp-t kvenc,nmnvaliexcxalona,,ef,.t-lqwcewennur--eq-ejxnqixoekjt -q qqxeunyxjpe,eleenwjetn-tm eei"

alphabet = "abcdefghijklmnopqrstuvwxyz -,.0"


enc_mes = enc_mes_first
with open("output4.txt", "w") as f:
        # Write the value of the variable to the file
        f.write("")

for k in range (1,len(enc_mes)):
    step = len(enc_mes) // k
    plain_mes = ""
     
    for i in range (0,step):
        plain_mes += enc_mes[i]
        pos=i
        while (pos + step <len(enc_mes)):
            pos += step
            plain_mes += enc_mes[pos]
        
    print("--- First Key = "+ str(k) )
   
    enc_mes = plain_mes  
        
        
    for y in range (len(alphabet)):
        key = y
        
        print ("Second Key = " + str(key))
        
        plain_mes = ""
        for i in range (len(enc_mes)):
            plain_char = enc_mes[i]
            plain_mes += alphabet[alphabet.index(plain_char)-key% len(alphabet)]
        
        while (plain_mes[-1]== '0'):
            plain_mes = plain_mes[:-1]
        
        with open("output4.txt", "a") as f:
            # Write the value of the variable to the file
            f.write(str(k) + "\n")
            f.write(str(key) + "\n")
            f.write(str(plain_mes) + "\n")
            
        print ("Plain message is = "+ plain_mes)
        
    enc_mes = enc_mes_first
    
    
#puzzle4 
#enc_mes =  "jye,---nexjnxoummxw,eoqxx,0ejrjnrrwcnl,wy-qlevmqe,eafxehwle-uno.q.,um n xxeejqexn .,rexmnye,lke-nnnjeeunux-enwewav,wnnwlx q,lknm.-qtnrn blamumvweg eeyge.qevjn..rnqqkvek,n-ewewy.-nxeenlex0r ejlj,h w p,eej-x,ujfeye,-x e-lvv  qpnwxjuqwniu,rqcuj gwxr,jlr xe-rrrtjxjrn. eow eejice,eexuue-eln xlne,r,wp-t kvenc,nmnvaliexcxalona,,ef,.t-lqwcewennur--eq-ejxnqixoekjt -q qqxeunyxjpe,eleenwjetn-tm eei"
#plain_mes = "an early opponent of security through obscurity was the locksmith alfred charles hobbs, who demonstrated to the public how state-of-the-art locks could be picked. in response to concerns that exposing security flaws in the design of locks could make them more vulnerable to criminals, he said rogues are very keen in their profession, and know already much more than we can teach them."
#key-transposition = 10
#key-caesar = 9
#Transposition and Caesar algorithm
#alphabet = "abcdefghijklmnopqrstuvwxyz -,.0"