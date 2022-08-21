
def add(number):
    if len(number.strip()) == 0:
        return 0
    elif len(number) == 1:
        return int(number)
    
    elif len(number) >= 2:
        token=number.split(",")
        sumoftwostring=list(map(int,token))
        sum=0
        for i in sumoftwostring:
            sum += i
        return sum