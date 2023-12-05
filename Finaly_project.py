import random
import time

names=["Jotaro", "Vasya", "Oguzok", "Vlad", "Jozeph"]
surnames=["Pupkin", "Ogriziv", "Klichko", "Petuhov", "Kujo"]

class Human:                    #Класс человека
    def __init__(self, health, happy, strength, money, money_bust, kul, nationaliti=None, name=None):
        self.money=money
        self.money_bust=money_bust
        self.kul=kul
        self.health=health
        self.happy=happy
        self.strength=strength
        self.alive=True
        self.random_cube=0
        self.nationaliti=nationaliti
        self.name=name
    def __str__(self):
        return f"money={self.money}\n\nname={self.name}\nhealth={self.health}\nhappy={self.happy}\nstrenght={self.strength}\n" \
               f"Nationaliti={self.nationaliti}"
    def lives(self):
        if self.health<=0:
            self.alive=False
        if self.happy<=0:
            self.alive=False
        if self.money<=0:
            self.alive=False
        if self.alive==False:
            return False
    def live(self):
        self.lives()
        if self.alive==True:
            self.random_cube=random.randint(1,3)
            if self.random_cube==1:
                self.walk()
            if self.random_cube==2:
                self.work()
            if self.random_cube==3:
                self.home()
            self.happy+=20             #Человек поспал
            if self.health>100:
                self.health=100
            if self.happy>100:
                self.happy=100
            if self.strength>100:
                self.strength=100
    def walk(self):
        self.random_cube=random.randint(1,3)
        if self.random_cube==1:
            self.happy+=20         #Человек пошёл в парк
        elif self.random_cube==2:
            if self.money>20:
                self.happy+=30         #Человек пошёл в ресторан
                self.money-=10
            else:
                self.happy-=20        #Человек пошёл в парк из-за недостатка денег
        elif self.random_cube==3:
            self.health+=20
            self.strength+=10
    def work(self):
        self.happy-=20    #Человек пошёл на работу
        self.money+=40
    def home(self):
        self.random_cube=random.randint(1,3)
        if self.random_cube==1:
            self.happy+=10    #Человек играет в игры на компютере
        if self.random_cube==2:
            self.happy+=30     #Человек бухает
            self.health-=20
        if self.random_cube==3:
            self.happy-=10    #Человек провёл уборку в доме
            self.health+=10

class Strana:
    def __init__(self, nation, count, money_bust, kul):
        self.nation=nation
        self.money_bust=money_bust
        self.count=count
        self.kul=kul
        self.time_obj=None
        self.humans=[]
        for i in range(1,self.count+1):
            self.time_obj=Human(money=random.randint(50,100), happy=random.randint(50,100), health=random.randint(50,100),
                                strength=random.randint(50,100),nationaliti=self.nation,
                                name=names[random.randint(0, len(names)-1)]+" "+surnames[random.randint(0, len(surnames)-1)],
                                kul=self.kul, money_bust=self.money_bust)
            self.humans.append(self.time_obj)
            print(self.time_obj)

    def day(self):
        self.colvo = self.count
        for i in range(0, len(self.humans)):
            self.humans[i].live()
            if self.humans[i].alive==False:
                self.colvo-=1
        print(f"\nКол в людей в государстве {self.nation}: {self.colvo}")



class Planet:
    def __init__(self):
        self.day = 1
        self.ogriziya = Strana(nation="Ogriziya", count=10, money_bust=20, kul=10)
        self.oguziya = Strana(nation="Oguziya", count=20, money_bust=10, kul=10)
        self.italiya = Strana(nation="Italiya", count=10, money_bust=10, kul=20)

    def WORLD(self):
        while True:
            print(f"День {self.day}")
            self.oguziya.day()
            self.ogriziya.day()
            self.italiya.day()
            self.day+=1
            time.sleep(0.3)

Tireya=Planet()
Tireya.WORLD()

time.sleep(100)

