mydict = {"Кто ты?": "Программист!", 
"Что делаешь?": "Программирую",
"Где ты?":"Дома"}

def ask_user(question, answer):
    while question == "Как дела?" and answer != "Хорошо":
        print(question)
        answer = str(input())
    if answer == "Хорошо":
        print("Спасибо, пока!")    

ask_user(input(), input())  
       



