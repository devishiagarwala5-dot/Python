num=[1,2,2,3,3,3,4,4,4,4,4,4,4,4,5,5,5,6,7,7]
ones=[]
twos=[]
threes=[]
fours=[]
fives=[]
sixes=[]
sevens=[]
for x in num:
    if x==7:
        sevens.append(x)
    elif x==2:
        twos.append(x)
    elif x==3:
        threes.append(x)
    elif x==4:
        fours.append(x)
    elif x==5:
        fives.append(x)
    elif x==6:
        sixes.append(x)
    else:
        ones.append(x)
print("no. of ones= ",len(ones))
print("no. of twos= ",len(twos))
print("no. of threes= ",len(threes))
print("no. of fours= ",len(fours))
print("no. of fives= ",len(fives))
print("no. of sixes= ",len(sixes))
print("no. of sevens= ",len(sevens))

  