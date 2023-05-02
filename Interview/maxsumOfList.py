list1 = [1,2,6,33,4,7,71,8,9]

maxsum = 0
number = [0,0]

for i in range(len(list1)):
  for j in range(i+1,len(list1)):
    s=list1[i]+ list1[j]
    if s>maxsum:
      number[0],number[1] = list1[i], list1[j]
      maxsum = s
     


print(maxsum)

