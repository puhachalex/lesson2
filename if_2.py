#Практика: Сравнение строк
a = input()
b = input()
def str_compare (a1, b1):
    if a1 is not str and b1 is not str:
        return 0
    if a1==b1 :
        return 1
    if a1!=b1 and len(a1)>len(b1):
        return 2  
    if a1!=b1 and b1=='learn':
        return 3      
x = str_compare(a, b) 
print(x) 