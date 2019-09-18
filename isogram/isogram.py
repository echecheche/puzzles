def is_isogram(str):
    
    import string
    
    str = str.lower()
    num = 1
    i = 0

    while((num<2) & (i<len(str))): 
        sub = str[i:i+1]
        
        #Checking if sub is a letter. Otherwise the code would fail to identify '   Amy' as an isogram.
        if string.ascii_lowercase.find(sub,0,len(string.ascii_lowercase))> -1 : num = str.count(sub, 0, len(str))
        i = i+1
        
    #Checking if num still equals 1.    
    if num==1 : return True
    else : return False