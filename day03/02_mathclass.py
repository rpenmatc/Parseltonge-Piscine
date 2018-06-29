import math
import sys
a = (sys.argv[1:])
a = list(map(int, a))
print("Min:", min(a))
mins = int(min(a))
lent = len(a)

print("Max:", max(a))
maximum = int(max(a))

summ = 0
num = 1
while  num < len(sys.argv):
  summ += int(sys.argv[num])
  num = num + 1
print("Mean:", summ / lent)
a.sort()
if(lent &2 ==0):
    median = (a[(lent)//2] + a[(lent)//2-1]) / 2
else:
    median = a[(lent - 1)// 2]
print("Median:", median)

mode = max(set(a), key=a.count)
print("Mode:", mode)



print("Range:", maximum - mins)
