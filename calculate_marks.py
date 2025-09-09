print("IF You calculate your marks please Enter your name:")
name = input("Enter your name:")
subjects = ["Hindi","English","Math","Physics","Chemistry"]
scores = []
print(len(subjects))
for mark in subjects:
    score = int(input(f"{name} enter your mark's subject {mark}:"))
    scores.append(score)
print(scores)
total_marks = print(f"{name} your total marks is :",sum(scores))
highest_marks = print(f"{name} your highest marks is:",max(scores))
lowest_marks = print(f"{name} your lowest marks is :",min(scores))
percentage = sum(scores)/len(subjects)
percentage = print(f"{name} your total marks percentage is {percentage:.2f} :")
