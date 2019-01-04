NUM128 = 128
NUM64 = 64
NUM32 = 32
NUM16 = 16
NUM8 = 8
NUM4 = 4
NUM2 = 2
NUM1 = 1

day_set1="Set 1: "
day_set2="Set 2: "
day_set4="Set 3: "
day_set8="Set 4: "
day_set16="Set 5: "

whatsLeft = 0

for i in range(1,32):
  bi_num=""
  input_num=i
  whatsLeft=input_num

  if input_num >= NUM128:
    whatsLeft= input_num - NUM128
    bi_num+="1"

  else:
    bi_num+="0"

  if whatsLeft >= NUM64:
    whatsLeft-=NUM64
    bi_num+="1"
  else:
    bi_num+="0"

  if whatsLeft >= NUM32:
    whatsLeft-=NUM32
    bi_num+="1"
  else:
    bi_num+="0"

  if whatsLeft >= NUM16:
    whatsLeft-=NUM16
    bi_num+="1"
  else:
    bi_num+="0"

  if whatsLeft >= NUM8:
    whatsLeft-=NUM8
    bi_num+="1"
  else:
    bi_num+="0"

  if whatsLeft >= NUM4:
    whatsLeft-=NUM4
    bi_num+="1"
  else:
    bi_num+="0"

  if whatsLeft >= NUM2:
    whatsLeft-=NUM2
    bi_num+="1"
  else:
    bi_num+="0"

  if whatsLeft >= NUM1:
    whatsLeft-=NUM1
    bi_num+="1"
  else:
    bi_num+="0"


  xnum7 = bi_num[7]
  xnum6 = bi_num[6]
  xnum5 = bi_num[5]
  xnum4 = bi_num[4]
  xnum3 = bi_num[3]
  xnum2 = bi_num[2]
  xnum1 = bi_num[1]
  xnum0 = bi_num[0]

  x=str(i)
  if xnum3 == "1":
    day_set16 += x + " "
  if xnum4 == "1":
    day_set8 += x + " "
  if xnum5 == "1":
    day_set4 += x + " "
  if xnum6 == "1":
    day_set2 += x + " "
  if xnum7 == "1":
    day_set1 += x + " "

answer = ""
print(day_set1)
question1 = input("Do you see your birthday in this set?(y/n)")
if question1.lower() == "y":
  answer += "1"
elif question1.lower() == "n":
  answer += "0"
else:
  print('No bad')
  
print(day_set2)
question1 = input("Do you see your birthday in this set?(y/n)")
if question1.lower() == "y":
  answer += "1"
elif question1.lower() == "n":
  answer += "0"
else:
  print('No bad')
  
print(day_set4)
question1 = input("Do you see your birthday in this set?(y/n)")
if question1.lower() == "y":
  answer += "1"
elif question1.lower() == "n":
 answer += "0"
else:
  print('No bad')
  
print(day_set8)
question1 = input("Do you see your birthday in this set?(y/n)")
if question1.lower() == "y":
  answer += "1"
elif question1.lower() == "n":
  answer += "0"
else:
  print('No bad')
  
print(day_set16)
question1 = input("Do you see your birthday in this set?(y/n)")
if question1.lower() == "y":
  answer += "1"
elif question1.lower() == "n":
  answer += "0"
else:
  print('No bad')
  
birthday = 0

print()
print(answer)
#for num in answer[:5]:
  

  
if answer[0] == "1":
  birthday += 16
if answer[1] == "1":
  birthday += 8
if answer[2] == "1":
  birthday += 4
if answer[3] == "1":
  birthday += 2
if answer[4] == "1":
  birthday += 1
print("Your birthday is: ??/"+str(birthday)+"/????")

  




  
