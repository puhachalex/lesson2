#Практика: Возраст
a= input()  
def work_place (age):
    age = int(age)
    if 1<= age <= 5:
        return"Должен учиться в детском саду"
    if 6<= age <=16:
         return"Должен учиться в школе"
    if 17<= age <=22:
        return"Должен учиться в ВУЗе"
    if 23<= age <=70:
        return"Должен работать"
    else:
        return"Должен отдыхать"   
x= work_place(a)
print(x)  

      


       
     
              