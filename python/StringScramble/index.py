

def StringScramble(str1, str2):

    #first i need an array to pesist some characters
    myArr=[]

    # i need to known the length of both parameters
    len1 = len(str1)
    len2 = len (str2)

    # transform both parameters to lowercase
    str1=str1.lower()
    str2=str2.lower()

    for i in range(len2): 
        for j in range (len1): 
            if str1[j]==str2[i]:
                myArr.append (str1[j])
    myArr = ''. join (myArr)
    # now we can compare the result
    if myArr == str2: 
        return True
    return False


# Program

print(StringScramble("cdore", "code"))
# Result should be: True

print(StringScramble("codak", "code"))
# Result should be: False