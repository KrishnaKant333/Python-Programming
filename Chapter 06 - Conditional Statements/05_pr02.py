marks1 = int(input("Enter marks in 3 subjects :"))
marks2 = int(input())
marks3 = int(input())
total_percent = (marks1+marks2+marks3)/3
if(marks1<33 or marks2<33 or marks3<33 or total_percent<40):
	print("You are fail.")
else:
	print("You are pass.")
