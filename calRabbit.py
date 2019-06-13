import sys

mon=5
num=3
total=1
pre=1
mature=0
temp=mon+1

for i in range(1,mon+1):
	if i==1:
		continue
	elif i==2:
		mature=pre
		pre=0
	elif i==temp:
		mature=pre+mature
	else:
		temp=pre
		pre=mature*num
		mature=temp+mature
	print("Mature had ",mature," while pre-mature had ",pre," at month ",i)

total=mature+pre
print(total)

