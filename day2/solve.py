# https://adventofcode.com/2020/day/2
# part 1
file = open("new.txt","r")
row = file.readlines()
valid = 0

def solveFirst():
    for line in row:
     count = 0
     info = line.split()
     occurrence = info[0].split("-")
     occurrenceMin= int(occurrence[0])
     occurrenceMax = int(occurrence[1])
     letter = info[1][0]
     password = info[2]

     for i in password:
        if i == letter:
            count = count + 1

     if occurrenceMin <= count <= occurrenceMax:
         valid = valid +1

    print valid

# part 2

def solveSecond():

    for line in row:
     info = line.split()
     occurrence = info[0].split("-")
     occurrenceMin= int(occurrence[0])
     occurrenceMax = int(occurrence[1])
     letter = info[1][0]
     password = info[2]



     if password[occurrenceMin-1] == letter and password[occurrenceMax-1] != letter or password[occurrenceMin-1] != letter and password[occurrenceMax-1] == letter:
         valid = valid + 1

    print valid
