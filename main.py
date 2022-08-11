from category import *

def print_all():
    all_cat=Categories.objects
    if(all_cat):
        for i in all_cat:
            print("\nCategory: ",i.c_name)
            print_db(i.c_id)

def main():
    main_menu_input=0
    while(main_menu_input!=3):
        print("\nMain Menu\n1.Print DataBase\n2.Modify\n3.Exit")
        print("\nInput: ",end=" ")
        main_menu_input=int(input())
        if(main_menu_input==1):
            print_all()
        elif(main_menu_input==2):
            cat_menu()
        elif(main_menu_input==3):
            exit()
        else:
            print("\nInvalid Input")

if __name__=='__main__':
    main()