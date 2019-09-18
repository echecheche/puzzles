def steps(n):
    
    count = 0

    while n != 1:

        print(count, n)
        
        if n == int(n) and (n > 0) == False:
            raise ValueError('not an integer or negative')
            break
            
        else:
            if (n % 2) == 0:
                n = n/2

            else:
                n = 3*n + 1

        count += 1
            
    print(count,n)


        
        
