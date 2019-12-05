#Практика: Сравнение строк
def str_compare (a1, b1):
    if type(a1)!=str or type(b1)!=str:
        return 0
    elif a1==b1 :
        return 1
    elif a1!=b1 and len(a1)>len(b1) and  b1!='learn' :
        return 2  
    elif a1!=b1 and b1=='learn':
        return 3
       
x = str_compare('lear111','learn')              
print(x)
