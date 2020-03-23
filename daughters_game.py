import os

def clear():
    os.system('clear')

def redwood_forest():
    print("\nThe cat has just been taken to the Redwood Forest!!\n")

def type_of_cat():
    clear()
    print("create your cat")
    print("""1. name your cat
2. color
3. EYE color""")
    type_reply = input("> ")
    if type_reply == "1":
        cat_name = input('Name of cat: ')
        print(f"The name of your cat is {cat_name}")
    else:
        exit()

def cat_menu():
    print("\nWhat do you want to do?\n")
    print("""1. Choose your cat
2. Choose your environment
3. exit""")
    cat_menu_reply = input('\n> ')
    if cat_menu_reply == '1':
        type_of_cat()
    elif cat_menu_reply == '2':
        environment()
    else:
        exit()

def environment():
    # places will be Redwood forest, winter forest, desert, neighborhood
    print("Choose where you want the cat to live\n")
    print("""1. Redwood Forest
2. Winter Forest
3. Desert
4. Neighborhood""")
    env_reply = input('\n> ')
    if env_reply == "1":
        redwood_forest()
    elif env_reply == "2":
        pass
    elif env_reply == "3":
        pass
    elif env_reply == "4":
        pass
    else:
        exit()



def game_intro():
    clear()
    print("\n*****Welcome to Cat Sim******\n")
    cat_menu()



game_intro()


