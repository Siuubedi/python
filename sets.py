marks = {98, 97, 95, 96, 95, 96}
print(marks) # {96, 97, 98, 95} -> This is because sets are unordered and also don't allow duplicates.
print(len(marks)) # 4

for score in marks:
    print(score)
    

marks.remove(98)
marks.add(99)
print(marks)