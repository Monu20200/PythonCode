import random
print("""====Snake Water Gun Game===
1. start game
2. show rules
3. show leaderboard
4. reset score
5. exit
""")
def greet(fx):
    def mfx(*args,**kwargs):
        print('welcome to SWG game')
        fx(*args,**kwargs)
    return mfx
rounds = 0
count_user = 0 
count_comp = 0
count_draw = 0
option = ['snake', 'gun', 'water']
def show_rules():
    print("""=====Rules======
•Gun beats Snake
•Water beats Gun
•Snake beats Water
================
""")
def game_reset():
    global count_user, count_comp, count_draw , rounds
    count_user, count_comp, count_draw, rounds = 0,0,0,0
    print()
    print('---Reset score successful---')
def show_leaderboard():
    print()
    print(f"Total no. of rounds played : {rounds}")
    print('User total wins : ', count_user)
    print('Computer total wins : ', count_comp)
    print('Total draw rounds : ', count_draw)
    if count_user > count_comp:
        print('User win overall')
    elif count_user < count_comp:
        print('Computer win overall')
    elif count_user !=0 and count_comp !=0:
        if count_user == count_comp:
            print('Draw match')
    print()
@greet
def start_game():
    while True:
            print()
            global count_user, count_comp, count_draw, rounds 
            rounds += 1
            print('Options are : snake, gun and water')
            comp = random.choice(option)
            c =  comp.lower()
            while True:
                 user = input('Enter your option : ')
                 u = user.lower()
                 if u in option:
                      break
                 else:
                        print('Invalid option choose again!!')                  
            print(f"""User chooses : {u}
Computer chooses : {c}""")
            print('Therefor, ')
            if u == 'snake' and c == 'water':
                print('User Wins')
                count_user += 1
            elif u == 'water' and c == 'snake':
                print('Computer wins')
                count_comp += 1
            elif u == 'gun' and c == 'water':
                print('Computer Wins')
                count_comp += 1
            elif u == 'water' and c == 'gun':
                print('User Wins')
                count_user += 1
            elif u == 'snake' and c == 'gun':
                print('Computer Wins')
                count_comp += 1
            elif u == 'gun' and c == 'snake':
                print('User Wins')
                count_user += 1
            else:
                print('Draw Match')
                count_draw += 1
            print()
            b = input('Would you like to play another round y/n ? ')
            if b in 'nN':
               break       
while True:   
    try: 
        print()
        num = int(input('Enter the operation number: '))
        if 1<= num <= 5:
            if num ==1:
                start_game()
            elif num ==2:
                show_rules()
            elif num ==3:
               show_leaderboard()
            elif num ==4:
                game_reset()    
            elif num ==5:
                print("---Exiting game---")
                break
        else:
                print('enter valid operation no. 1-5')
    except ValueError:
        print('Invalid input!! , enter again')