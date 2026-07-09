print("Info Collector From User")
def info_collector():
    l_info = []
    while True:
        user_info = {}
        name = input("enter your name: ")
        user_info["name"]= name
        age = input("enter your age: ")
        user_info["age"]= age
        standard = input("enter your standard: ")
        user_info["standard"]= standard
        subject_marks ={}
        while True:
            sub= input("enter the subject name: ")
            marks_obtained = input("enter the marks obtained: ")
            subject_marks[sub]= marks_obtained
            a = input("would you like to add more sub? (y/n): ")
            if a in "nN":
                break
            elif a not in "yYnN":
                print("invalid input")
                continue
        user_info["subject_marks"]= subject_marks
        city = input("enter your city: ")
        user_info["city"]= city
        l_info.append(user_info)
        b = input("would you like to make more entries? (y/n): ")
        if b in "nN":
            break
        elif b not in "yYnN":
            print("invalid input")
            continue
print(l_info)    
    #return l_info
info_collector()
