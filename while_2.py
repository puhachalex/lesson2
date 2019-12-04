def ask_user(question):
    mydict = {"Кто ты?": "Программист!", 
    "Что делаешь?": "Программирую",
    "Где ты?":"Дома",
    "Как дела?":"Хорошо"}
    questions = mydict.keys()
    while True:
        if question in questions:
            print(mydict[question])
            break
        else:
            print("Пока!")
            break
ask_user(input())        


 
       



