
def add(number):
    Negative_number=filter(lambda x:x < 0,number)
    number = number.replace("\n",",")
    if len(number.strip()) == 0:
        return 0
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
    elif Negative_number:
        raise Exception('Negative not allowed '+str(Negative_number))
    