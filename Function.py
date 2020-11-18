a_list = []
def Average(a_list):
  return sum(a_list) / len(a_list)

while 1:
  command = input("Enter the command: ")
  if command == 'BYE':
    print("Bye Bye")
  elif command == 'ADD':
    num = int(input("Enter the number to add: "))
    a_list.append(num)
  elif command == 'SHOW':
    if a_list == []:
      #Fail Condition
      print("Please ADD a number in the list\n") 
    else:
      print(a_list)
  elif command == 'COUNT':
    if len(a_list) == 0:
      # Fail Condition
      print("No number to count, Please ADD a number in the list\n")
    else:
      print(len(a_list))
  elif command == 'AVERAGE':
    if len(a_list) == 0:
      print("No number in the list, ADD a number in the list\n")
    else:
      print(Average(a_list))
