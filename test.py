def produce(rOff, cOff):
    ## Row constraints 
    exI = ""
    exJ = ""
    exL = ""
    for i in range((1+rOff),(10+rOff)):
        for j in range((1+cOff),(10+cOff)):
            for k in range(1,10):
                for l in range((1+cOff),(10+cOff)):
                    if j is not l:
                       if i < 10:
                           exI = "0"
                       if j < 10:
                           exJ = "0"
                       if l < 10:
                           exL = "0"
                       print("-",exI,i,exJ,j,k, sep="", end="")
                       print(" ", end="")
                       print("-",exI,i,exL,l,k, sep="")
                       exI = ""
                       exJ = ""
                       exL = ""

produce(0,0)
