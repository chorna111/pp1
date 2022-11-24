import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
total=0
for i in temperatures:
    i=int(i)
    total+=i
avg=int(total/len(temperatures))
print(message)
print(f'the average temperature is: {avg}C')
