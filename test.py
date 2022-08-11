from mongoengine import connect,Document,IntField,StringField
connect('shopDB')

class Rando(Document):
    rand_name=StringField()

def test():
    catTest=Rando(rand_name="TEST")   
    catTest.save() 

if __name__=='__main__':
    test()