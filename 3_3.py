#promt the score
score = input('Enter score: ')

#check is score is valid
try:
    score = float(score)
except:
    score = -1

#select score grade
if score == -1:
    grade= 'Score is invalid!'
elif score >= 0.9:
    grade = 'A'
elif score >= 0.8:
    grade = 'B'
elif score >= 0.7:
    grade = 'C'
elif score >= 0.6:
    grade = 'D'
else:
    grade = 'F'

#output
print(grade)
