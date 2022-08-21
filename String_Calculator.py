
def add(number):
    if len(number.strip()) == 0:
        return 0
    # elif len(number) == 1:
    #     return int(number)
    
    # elif len(number) >= 1:
    #     token=number.split(",")
    #     sumoftwostring=list(map(int,token))
    #     sum=0
    #     for i in sumoftwostring:
    #         sum += i
    #     return sum
    
    elif len(number) >= 1:
        token=number.split(",")
        sum=0
        for i in token:
            if(not i.isdigit()):
                sum+=(ord(i)-96)
            else:
                if(not int(i) >1000):
                    sum+=int(i)
        return sum
    # ignore 1000
    # elif len(number) >=1:
    #     token = number.split(",")
    #     sum=0
    #     for i in token:
    #         if(not int(i)==1000):
    #             sum+=int(i)
    #     return sum
    # # Handling unknow amount of string
    # elif len(number) >= 2:
    #     token=number.split(",")
    #     sumoftwostring=list(map(int,token))
    #     sum=0
    #     for i in sumoftwostring:
    #         sum += i
    #     return sum