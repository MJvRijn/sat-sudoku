def produce(rOff, cOff):    
    ## At least 1 number in a cell: 
    exI = ""
    exJ = ""
    exK = ""
    exL = ""
    exM = ""
    for i in range((1+rOff),(10+rOff)): 
        for j in range((1+cOff),(10+cOff)): 
            for k in range(1,10): 
                if i < 10:
                    exI = "0"
                if j < 10:
                    exJ = "0"
                print(exI,i,exJ,j,k, sep="", end="")         
                print(" ", end="") 
                exI = ""
                exJ = ""
            print("\n", end="") 
 
    ## No duplicates: 
    for i in range((1+rOff),(10+rOff)): 
        for j in range((1+cOff),(10+cOff)): 
            for k in range(1,10): 
                for l in range(1,10): 
                    if l is not k: 
                        if i < 10:
                            exI = "0"
                        if j < 10:
                            exJ = "0"
                        print("-",exI,i,exJ,j,k, sep="", end="") 
                        print(" ", end="") 
                        print("-",exI,i,exJ,j,l, sep="") 
                        exI = ""
                        exJ = ""
    ## Row constraints 
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
 
    ## Column constraints 
    for i in range((1+rOff),(10+rOff)): 
        for j in range((1+rOff),(10+rOff)): 
            for k in range(1,10): 
                for l in range((1+rOff),(10+rOff)):  
                    if i is not l: 
                        if i < 10:
                            exI = "0"
                        if j < 10:
                            exJ = "0"
                        if l < 10:
                            exL = "0"
                        print("-",exI,i,exJ,j,k, sep="", end="") 
                        print(" ", end="") 
                        print("-",exL,l,exI,i,k, sep="") 
                        exI = ""
                        exJ = ""
                        exL = ""
 
    #top left 
    for i in range((1+rOff),(4+rOff)): 
        for j in range((1+cOff),(4+cOff)): 
            for k in range(1,10): 
                for l in range((1+rOff),(4+rOff)): 
                    for m in range((1+cOff),(4+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #top
    for i in range((1+rOff),(4+rOff)):
        for j in range((4+cOff),(7+cOff)):
            for k in range(1,10):
                for l in range((1+rOff),(4+rOff)):
                    for m in range((4+cOff),(7+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #top right
    for i in range((1+rOff),(4+rOff)):
        for j in range((7+cOff),(10+cOff)):
            for k in range(1,10):
                for l in range((1+rOff),(4+rOff)):
                    for m in range((7+cOff),(10+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #middle left 
    for i in range((4+rOff),(7+rOff)):
        for j in range((1+cOff),(4+cOff)):
            for k in range(1,10):
                for l in range((4+rOff),(7+rOff)):
                    for m in range((1+cOff),(4+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #middle
    for i in range((4+rOff),(7+rOff)):
        for j in range((4+cOff),(7+cOff)):
            for k in range(1,10):
                for l in range((4+rOff),(7+rOff)):
                    for m in range((4+cOff),(7+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #middle right
    for i in range((4+rOff),(7+rOff)):
        for j in range((7+cOff),(10+cOff)):
            for k in range(1,10):
                for l in range((4+rOff),(7+rOff)):
                    for m in range((7+cOff),(10+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #bottom left 
    for i in range((7+rOff),(10+rOff)):
        for j in range((1+cOff),(4+cOff)):
            for k in range(1,10):
                for l in range((7+rOff),(10+rOff)):
                    for m in range((1+cOff),(4+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #bottom middle
    for i in range((7+rOff),(10+rOff)):
        for j in range((4+cOff),(7+cOff)):
            for k in range(1,10):
                for l in range((7+rOff),(10+rOff)):
                    for m in range((4+cOff),(7+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
    #bottom right
    for i in range((7+rOff),(10+rOff)):
        for j in range((7+cOff),(10+cOff)):
            for k in range(1,10):
                for l in range((7+rOff),(10+rOff)):
                    for m in range((7+cOff),(10+cOff)):
                        if i == l and j == m:
                            continue
                        else:
                            if i < 10:
                                exI = "0"
                            if j < 10:
                                exJ = "0"
                            if l < 10:
                                exL = "0"
                            if m < 10:
                                exM = "0"
                            print("-",exI,i,exJ,j,k, sep="", end="")
                            print(" ", end="")
                            print("-",exL,l,exM,m,k, sep="")
                            exI = ""
                            exJ = ""
                            exL = ""
                            exM = ""
produce(0,0)
produce(0,12)
produce(9,6)
produce(12,0)
produce(12,12)
