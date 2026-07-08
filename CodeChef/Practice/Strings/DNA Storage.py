t = int(input())

while t > 0:
    n = int(input())
    s = input()
    
    i=0
    DNA=""
    while i<=n:
        match (s[i:i+2]):
            case "00":
                DNA+="A"
            case "01":
                DNA+="T"
            case "10":
                DNA+="C"
            case "11":
                DNA+="G"
        i+=2
    print(DNA)
    t -= 1
