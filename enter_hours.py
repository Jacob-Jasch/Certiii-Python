from fileinput import close
from csv import *
from csv import reader
hourlist = []
all_hours = []

def enterhours():
  print(" ")
  titleRow = "Week,Employee ID,Employee Name,Mon,Tue,Wed,Thru,Fri,totel hours"
  F = open("timelist.csv", "w")
  F.write(titleRow)
  F.close       
  while(True):
        looptime = looptime =+ 1
        week = input("Enter Current Working Week, or type end to end program:   ")
        if(week == "end"):
            break
        elif(week != "end"):
            hourlist.append(week)
        id = input("Enter Employee " + str(looptime) +  " ID:   ")
        hourlist.append(id)
        name = input("Enter Employee " + str(looptime) + " Name:  ")
        hourlist.append(name)
        Monday = input("Enter Hours Worked for Monday:  ")  
        if (Monday.isdigit()):
            hourlist.append(int(Monday))
        else:
            print("Invailed nummber, will asume 0")
            Monday = 0
            hourlist.append(int(Monday))
        Tuesday = input("Enter Hours Worked for Tuesday:  ")
        if (Tuesday.isdigit()):
            hourlist.append(int(Tuesday))
        else:
            print("Invailed nummber, will asume 0")
            Tuesday = 0
            hourlist.append(int(Tuesday))
        Wednesday = input("Enter Hours Worked for Wednesday:   ")
        if (Wednesday.isdigit()):
            hourlist.append(int(Wednesday))
        else:
            print("Invailed nummber, will asume 0")
            Wednesday = 0
            hourlist.append(int(Wednesday))
        Thursday = input("Enter Hours Worked for Thursday:  ")
        if (Thursday.isdigit()):
            hourlist.append(int(Thursday))
        else:
            print("Invailed nummber, will asume 0")
            Thursday = 0
            hourlist.append(int(Thursday))
        Friday = input("Enter Hours Worked for Friday:  ")
        if (Friday.isdigit()):
            hourlist.append(int(Friday))
        else:
            print("Invailed nummber, will asume 0")
            Friday = 0
            hourlist.append(int(Friday))
        print(hourlist)
        print("**************************************")
        print("Summary for Employee " + str(looptime) + " ")
        all_hours = int(Monday) + int(Tuesday) + int(Wednesday) + int(Thursday) + int(Friday)
        if(int(Monday) < 4):
            print("Insufficient hours worked on Monday")
        elif(int(Monday) > 20):
            print("Too many hours worked on Monday")
        if(int(Tuesday) < 4):
            print("Insufficient hours worked on Tuesday")
        elif(int(Tuesday) > 20):
            print("Too many hours worked on Tuesday")
        if(int(Wednesday) < 4):
            print("Insufficient hours worked on Wednesday")
        elif(int(Wednesday) > 20):
            print("Too many hours worked on Wednesday")
        if(int(Thursday) < 4):
            print("Insufficient hours worked on Thursday")
        elif(int(Thursday) > 20):
            print("Too many hours worked on Thursday")
        if(int(Friday) < 4):
            print("Insufficient hours worked on Friday")
        elif(int(Friday) > 20):
            print("Too many hours worked on Friday")
        if(int(Monday) + int(Tuesday) + int(Wednesday) + int(Thursday) + int(Friday) < 30):
            print("You did not do enough work this week")
        elif(int(Monday) + int(Tuesday) + int(Wednesday) + int(Thursday) + int(Friday) > 40):
            print("You are working too hard!")
        print(all_hours, " hours worked in week ", week)
        empWorkInfo1 = str(week) + "," + str(id) + "," + str(name) + "," + str(Monday) + "," + str(Tuesday) + "," + str(Wednesday) + "," + str(Thursday) + "," + str(Friday) + "," + str(all_hours)
        F = open("timelist.csv", "a")
        F.write("\n"+ empWorkInfo1)
        F.close

def hoursReport():
  LessNo = 0
  MoreNo = 0
  BeNo = 0
  with open('timelist.csv', 'r') as read_obj:
      csv_reader = reader(read_obj)
      next(csv_reader)
      for row in csv_reader:
        if(int(row[8]) < 30):
          LessNo = LessNo + 1
        if(int(row[8]) > 40):
          MoreNo = MoreNo + 1
        if(int(row[8]) >= 37 and int(row[8]) <= 39):
          BeNo = BeNo + 1
      print(LessNo, "employees worked less than 30 hours a week")    
      print(MoreNo, "employees worked more than 40 hours a week")    
      print(BeNo, "employees worked between 37-39 hours")
  chose()

def end():
    close()

def chose():
  print(" ")
  inputNum = input("Please hit the \n1 key to Enter daily hours worked, \n2 key to produce the Hours Worked Report or \n3 key to Quit/Close/Exit the Program \n \n")
  if(str(inputNum) == "1"):
      enterhours()
  elif(str(inputNum) == "2"):
      hoursReport()
  elif(str(inputNum) == "3"):
      end()

chose()