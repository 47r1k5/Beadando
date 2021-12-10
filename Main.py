import os
import sys
from time import sleep
import PeopleClass as pc
from pathlib import Path

CLIENTS_DATABASE_PATH=Path("ClientsDatabase.txt")

def menu():
    os.system("cls")
    print("MENU")
    print("1. New person")
    print("2. List people")
    print("3. Quit")

    try:
        userChoice = int(input("Choose from the options: "))
        if int(userChoice) == 1:
            new_person()

        elif int(userChoice) == 2:
            list_people()

        elif int(userChoice) == 3:
            quit()
            
        elif int(userChoice) > 3 or int(userChoice) < 1:
            print("There is no " + str(userChoice) + ". option. Try Again! \n ")
            sleep(2)
            os.system("cls")
            menu()

    except ValueError:
        print("Input Error! Wrong type of input. Please try again! \n")
        sleep(2)
        os.system("cls")
        menu()

def new_person():

    os.system("cls")

    print("New Person's data sheet\n")

    newPerson=pc.People.setData()
    print("\n")
    bmi = newPerson.bmi_calculator()
    newPerson.decide_bmi(bmi)
    bodyFatPercentage=newPerson.body_fat_calculator()

    if bodyFatPercentage==0:
        input("\nPress ENTER to continue!\n")

        print("Back to the Main Menu")
        sleep(2)
        os.system("cls")
        menu()

    newPerson.bmr_calculator(bodyFatPercentage)
    newPerson.write_file(CLIENTS_DATABASE_PATH)

    input("\nPress ENTER to continue!\n")

    print("Back to the Main Menu")
    sleep(2)
    os.system("cls")
    menu()

def list_people():

    os.system("cls")

    print("List people\n")
    read_file(CLIENTS_DATABASE_PATH)

    input("\nPress ENTER to continue!\n")

    print("Back to the Main Menu")
    sleep(10)
    os.system("cls")
    menu()

def quit():
    os.system("cls")

    print("Shutting down")
    sleep(2)
    os.system("cls")

    print("Shutting down.")
    sleep(2)
    os.system("cls")

    print("Shutting down..")
    sleep(2)
    os.system("cls")
    
    print("Shutting down...")
    sleep(1)
    os.system("cls")

    sys.exit()

def read_file(file_path:Path):
    datas=[]
    try:
        file=open(file_path,"r")
        for line in file.readlines():
            datas.append(line.strip().split(","))
        file.close
        print_datas(datas)
    except FileNotFoundError:
        print("You don't have any clients yet in your database.")

def print_datas(datas:list):
    print("ID - NAME - SEX - AGE - HEIGHT - WEIGHT - NECK - WAIST - HIP ")
    for i in range(len(datas)):
        print(str(i) + " - " + datas[i][0] + " - " + datas[i][1] + " - " + datas[i][2] + " - " + datas[i][3] + " - " + datas[i][4] + " - " + datas[i][5] + " - " + datas[i][6]
            + " - " + datas[i][7])

menu()