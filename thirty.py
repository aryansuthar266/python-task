#Average & Grade

marks = [float(input("Mark: ")) for _ in range(5)]
avg = sum(marks)/5

if avg < 50: grade="F"
elif avg < 60: grade="D"
elif avg < 70: grade="C"
elif avg < 80: grade="B"
elif avg < 90: grade="A"
else: grade="A+"

print("Average:", avg, "Grade:", grade)
