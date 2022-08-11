from mongoengine import connect
from mongoengine import IntField,StringField,Document,ListField
from products import *

connect('shopDB')

class Categories(Document):
    c_id=IntField(required=True,unique=True)
    c_name=StringField()
    cat_p_list=ListField(IntField())
    
#CAT FUNCTIONS
def add_category(cat_id,cat_name):
    newCat=Categories(c_id=cat_id,c_name=cat_name)
    newCat.save()
    print_cat()

def delete_category(cat_id):
    Categories.objects(c_id=cat_id).delete()
    print("\nCategory has been deleted")
    print_cat()
    prod_delete_cat(cat_id)

def print_cat():
    if(Categories.objects):
        print("\n")
        for cat in Categories.objects.order_by('c_id'):
            print(cat.c_id,"  ",cat.c_name)
    else:
        print("Collection Empty")

def update_cat_id(cat_id,new_cat_id):
    Categories.objects(c_id=cat_id).update(set__c_id=new_cat_id)
    print("Category ID Updated")
    print_cat()
    prod_update_catid(cat_id,new_cat_id)

def update_cat_name(cat_id,new_cat_name):
    Categories.objects(c_id=cat_id).update(set__c_name=new_cat_name)
    print("Category Name Updated")
    print_cat()

#MAIN FN
def cat_menu():
    menu_input=0
    cat_id_list=[]
    cat_set=Categories.objects
    for cat in cat_set:
        cat_id_list.append(cat.c_id)
    
    while(menu_input!=5):
        menu_input=0
        cat_id_list=[]
        cat_set=Categories.objects
        for cat in cat_set:
            cat_id_list.append(cat.c_id)

        print("\nCategory Menu:\n1.Create Category\n2.View Categories\n3.Update Category\n4.Delete Category\n5.Exit\n")
        print("Input: ",end=" ")
        menu_input=int(input())
        if(menu_input==1):
            print("Enter Category ID: ",end=" ")
            cat_id=int(input())
            if(cat_id in cat_id_list):
                print("\nID already exists")
                continue
            print("Enter Category Name: ",end=" ")
            cat_name=input()
            add_category(cat_id,cat_name)
            
        elif(menu_input==2):
            print_cat()

        elif(menu_input==3):
            cat_id_list=[]
            cat_set=Categories.objects
            for cat in cat_set:
                cat_id_list.append(cat.c_id)
            print("Enter the Category ID to be updated: ",end=" ")
            cat_id=int(input())
            if(cat_id not in cat_id_list):
                print("\nCategory not found")
                continue

            cat_up_it=0
            cat_up_flag=0
            while(cat_up_flag!=1 and cat_up_it!=4):
                print("\nCategory Update Menu:\n1.Update Category ID\n2.Update Category Name\n3.Update Products in Category\n4.Exit")
                print("Input: ",end=" ")
                cat_up_it=int(input())
                if(cat_up_it==1):
                    print("Enter new Category ID: ",end=" ")
                    new_cat_id=int(input())
                    if(new_cat_id not in cat_id_list):
                        update_cat_id(cat_id,new_cat_id)
                        cat_up_flag=1
                    else:
                        print("ID already exists")
                elif(cat_up_it==2):
                    print("Enter new Category Name: ",end=" ")
                    new_cat_name=input()
                    update_cat_name(cat_id,new_cat_name)
                    cat_up_flag=1
                elif(cat_up_it==3):
                    prod_menu(cat_id)
                    cat_up_flag=1
                elif(cat_up_it==4):
                    print("\nExited Category Update Menu!")
                    break
                else:
                    print("Invalid Input")
        elif(menu_input==4):
            print("Enter the ID of category to be deleted: ",end=" ")
            cat_id=int(input())
            if(cat_id not in cat_id_list):
                print("Category not found")
                continue
            delete_category(cat_id)
        elif(menu_input==5):
            print("\nCategory Menu Exited!")
        else:
            print("Invalid Input")