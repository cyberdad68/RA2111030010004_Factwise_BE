def solve(n):
    unit_places=["","one","two","three","four","five","six","seven","eight","nine"]
    tenth_places=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens_places=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    if 1<=n<10:
        return unit_places[n]
    elif 10<=n<20:
        return tenth_places[n-10]
    elif 20<=n<100:
        return tens_places[n//10]+unit_places[n%10]
    elif 100<=n<1000:
        if n%100==0:
            return unit_places[n//100]+ "hundred"
        else:
            return unit_places[n//100]+"hundred and"+solve(n%100)
    elif n==1000:
        return "one thousand"
    else:
        return ""

def count(n):
    ans=0
    for i in range(1,n+1):
        words=solve(i)
        ans+=len(words)
    return ans
total_words=count(1000)  
print(total_words)















