s1 = {1,2,3}
s2 = {2,3,4}

s3 = s1 | s2
#Unite sets
print(s3)

s3 = s1 & s2
#Set intersection
print(s3)

s3 = s1 - s2
#Shows the items that only exist in the left set.
print(s3)

s3 = s1 ^ s2
#Shows the items that not exist in the sets at the same time
print(s3)


