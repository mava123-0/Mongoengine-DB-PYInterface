from mongoengine import connect
from mongoengine import IntField,StringField,Document


connect('shopDB')

class Products(Document):
    p_id=IntField(required=True)
    p_name=StringField(required=True)
    p_qty=IntField()
    prod_c_id=IntField(required=True)

def print_db(prod_cat_id):
    if(Products.objects.filter(prod_c_id=prod_cat_id)):
        print("\n")
        for prod in Products.objects.order_by('p_id').filter(prod_c_id=prod_cat_id):
            print(prod.p_id,"  ",prod.p_name,"  ",prod.p_qty)
        print("\n")
    else:
        print("\nCollection Empty\n")

def add_product(prod_id,prod_name,prod_qty,prod_cat_id):
    newProd=Products(p_id=prod_id,p_name=prod_name,p_qty=prod_qty,prod_c_id=prod_cat_id)
    newProd.save()
    print("\nProduct Added")
    print_db(prod_cat_id)

def delete_product(prod_id,prod_cat_id):
    if(Products.objects(p_id=prod_id)):
        Products.objects(p_id=prod_id).filter(prod_c_id=prod_cat_id).delete()
        print("Deleted")
        print_db(prod_cat_id)
    else:
        print("\nProduct not Found\n")

def update_id(prod_id,new_id,prod_cat_id):
    if(not Products.objects(p_id=prod_id)):
        print("Product not found")
        return
    Products.objects(p_id=prod_id).filter(prod_c_id=prod_cat_id).update(set__p_id=new_id)
    print("ID Updated")
    print_db(prod_cat_id)    

def update_name(prod_id,new_name,prod_cat_id):
    if(not Products.objects(p_id=prod_id)):
        print("\nProduct not found\n")
        return
    Products.objects(p_id=prod_id).filter(prod_c_id=prod_cat_id).update(set__p_name=new_name)
    print("Name Updated")
    print_db(prod_cat_id)    

def update_qty(prod_id,new_qty,prod_cat_id):
    if(not Products.objects(p_id=prod_id)):
        print("\nProduct not found\n")
        return
    Products.objects(p_id=prod_id).filter(prod_c_id=prod_cat_id).update(set__p_qty=new_qty)
    print("Quantity Updated")
    print_db(prod_cat_id)    

def prod_update_catid(old_id,new_id):
    old_prod_set=Products.objects.filter(prod_c_id=old_id)
    for prod in old_prod_set:
        prod.update(set__prod_c_id=new_id)
    print("\nAll 'Products' references updated")

def prod_delete_cat(cat_id):
    Products.objects(prod_c_id=cat_id).delete()
    print("\nAll 'Products' references updated")


def prod_menu(prod_cat_id):
    qset=Products.objects(prod_c_id=prod_cat_id)
    id_list=[]

    for i in qset:
        id_list.append(i.p_id)

    menu_input=1

    while(menu_input!=5 ):
        print("\nProduct Menu:\n1.Add Product\n2.Print Products\n3.Update Products\n4.Delete Product\n5.Exit\n")
        print("Input: ",end=" ")
        menu_input=int(input())

        if(menu_input==1): 
            print("Enter the new product id: ",end=" ")
            prod_id=int(input())
            if(prod_id in id_list):
                print("ID already exist\n")
                continue
            print("Enter the new product name: ",end=" ")
            prod_name=input()
            print("Enter the new product quantity: ",end=" ")
            prod_qty=int(input())
            add_product(prod_id,prod_name,prod_qty,prod_cat_id)

        elif(menu_input==4):
            print(id_list)
            print("Enter the product id of item to be deleted: ",end=" ")
            prod_id=int(input())
            if(prod_id in id_list):
                delete_product(prod_id,prod_cat_id)
            else:
                print("Product Not Found")

        elif(menu_input==3):
            print("Enter the Product ID of Product to be updated: ",end=" ")
            prod_id=int(input())
            if(prod_id not in id_list):
                print("Invalid ID")
                continue

            upd_flag=0

            while(upd_flag==0):
                print("\nProduct Update Menu:\n1.Product ID\n2.Product Name\n3.Product Quantity\n4.Exit Update Menu\n")
                print("Update: ",end=" ")
                upd_it=int(input())
                
                if(upd_it==4):
                    print("Exited Product Update Menu!\n")
                    break
                elif(upd_it==1):
                    print("Enter new ID: ",end=" ")
                    new_id=int(input())
                    if(new_id not in id_list):
                        update_id(prod_id,new_id,prod_cat_id)
                        upd_flag=1
                    print("ID already exists")
                elif(upd_it==2):
                    print("Enter new name: ",end=" ")
                    new_name=input()
                    update_name(prod_id,new_name,prod_cat_id)
                    upd_flag=1
                elif(upd_it==3):
                    print("Enter new quantity: ",end=" ")
                    new_qty=int(input())
                    update_qty(prod_id,new_qty,prod_cat_id)
                    upd_flag=1
                else:
                    print("Invalid Option")

        elif(menu_input==2):
            print_db(prod_cat_id)

        elif(menu_input==5):
            break

        else:
            print("Invalid Input\n")

    print("Exited Product Menu!\n")