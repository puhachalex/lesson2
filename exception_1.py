def ask_user(question, answer):
    try:
        while question == "Как дела?" and answer != "Хорошо":
            print(question)
            answer = str(input())
        if answer == "Хорошо":
            print("Спасибо, пока!")
    except KeyboardInterrupt:
        print("Пока!")            
ask_user(input(), input())
