## At least 1 number in a cell: 
for i in range(1,10): 
    for j in range(1,10): 
        for k in range(1,10): 
            print(i,j,k, sep="", end="")         
            print(" ", end="") 
        print("\n", end="") 
 
## No duplicates: 
for i in range(1,10): 
    for j in range(1,10): 
        for k in range(1,10): 
            for l in range(1,10): 
                    if l is not k: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-i,j,l, sep="") 
## Row constraints 
for i in range(1,10): 
    for j in range(1,10): 
        for k in range(1,10): 
            for l in range(1,10): 
                if j is not l: 
                    print(-i,j,k, sep="", end="") 
                    print(" ", end="") 
                    print(-i,l,k, sep="") 
 
## Column constraints 
for i in range(1,10): 
    for j in range(1,10): 
        for k in range(1,10): 
            for l in range(1,10):  
                if i is not l: 
                    print(-i,j,k, sep="", end="") 
                    print(" ", end="") 
                    print(-l,i,k, sep="") 
 
#top left 
for i in range(1,4): 
    for j in range(1,4): 
        for k in range(1,10): 
            for l in range(1,4): 
                for m in range(1,4): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
#top 
for i in range(1,4): 
    for j in range(4,7): 
        for k in range(1,10): 
            for l in range(1,4): 
                for m in range(4,7): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
#top right                
for i in range(1,4): 
    for j in range(7,10): 
        for k in range(1,10): 
            for l in range(1,4): 
                for m in range(7,10): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
 
#middle left 
for i in range(4,7): 
    for j in range(1,4): 
        for k in range(1,10): 
            for l in range(4,7): 
                for m in range(1,4): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
#middle 
for i in range(4,7): 
    for j in range(4,7): 
        for k in range(1,10): 
            for l in range(4,7): 
                for m in range(4,7): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
#middle right 
for i in range(4,7): 
    for j in range(7,10): 
        for k in range(1,10): 
            for l in range(4,7): 
                for m in range(7,10): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
#bottom left 
for i in range(7,10): 
    for j in range(1,4): 
        for k in range(1,10): 
            for l in range(7,10): 
                for m in range(1,4): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
#bottom 
for i in range(7,10): 
    for j in range(4,7): 
        for k in range(1,10): 
            for l in range(7,10): 
                for m in range(4,7): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
#bottom right 
for i in range(7,10): 
    for j in range(7,10): 
        for k in range(1,10): 
            for l in range(7,10): 
                for m in range(7,10): 
                    if i is not l & m is not j: 
                        print(-i,j,k, sep="", end="") 
                        print(" ", end="") 
                        print(-l,m,k, sep="") 
