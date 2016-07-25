Score = input("Enter your score")


with open("c:\\users\\kevsi\\Desktop\\gamedir\\main\\Last_Score.txt", "w") as text_file:
    print("Last Score: {}".format(Score), file=text_file)
