
def ask_user(question, answer):
    try:
        question=input()
    
        mydict = {"Кто ты?": "Программист!", 
                "Что делаешь?": "Программирую",
                "Где ты?":"Дома",
                "Как дела?":"Хорошо"}
    
        questions = mydict.keys()            

        if question == "Как дела?":
            while answer!="Хорошо":
                answer = input()
                print(question)
            if answer == "Хорошо":
                print("Спасибо, пока!")

        elif question != "Как дела?":
            if question in questions:
                print(mydict[question])
            else:
                print("Окей, пока!")
    except KeyboardInterrupt:
        print("Пока!")          
                    
            
ask_user("","")   
