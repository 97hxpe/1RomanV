import time

print("hallo")

question = input("willst du ein kleines warmup zum denken \n")
if question.lower() == 'ja':
    import random
for i in range(1):
     print(random.randint(1,6))
 
def wuerfeln():
    return(random.randint(1,6))
wuerfeln()

if question.lower() == 'nein':
    print("schade")
