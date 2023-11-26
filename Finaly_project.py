import random

names=["Jotaro", "Vasya", "Oguzok", "Vlad", "Jozeph"]
surnames=["Pupkin", "Ogriziv", "Klichko", "Petuhov", "Kujo"]

class Human:                    #Класс человека
    def __init__(self, health, happy, strength, money, nationaliti=None, name=None):
        self.money=money
        self.health=health
        self.happy=happy
        self.strength=strength
        self.live=True
        self.random_cube=0
        self.car=None
        self.nationaliti=nationaliti
        self.name=name
    def __str__(self):
        return f"money={self.money}\n\nname={self.name}\nhealth={self.health}\nhappy={self.happy}\nstrenght={self.strength}\n" \
               f"Nationaliti={self.nationaliti}"
    def alive(self):
        if self.health<=0:
            self.live=False
        if self.live==False:
            return False
    def live(self):
        if self.alive==True:
            self.random_cube=random.randint(1,3)
            if self.random_cube==1:
                self.walk()
            if self.random_cube==2:
                self.work()
            if self.random_cube==3:
                self.home()
            self.happy=+20             #Человек поспал
            if self.health>100:
                self.health=100
            if self.happy>100:
                self.happy=100
            if self.strength>100:
                self.strength=100
    def walk(self):
        self.random_cube=random.randint(1,3)
        if self.random_cube==1:
            self.happy=+20         #Человек пошёл в парк
        elif self.random_cube==2:
            if self.money>20:
                self.happy=+30         #Человек пошёл в ресторан
                self.money=-10
            else:
                self.happy=+20        #Человек пошёл в парк из-за недостатка денег
        elif self.random_cube==3:
            self.health=+20
            self.strength=+10
    def work(self):
        self.happy=-20    #Человек пошёл на работу
        self.money=+40
    def home(self):
        self.random_cube=random.randint(1,3)
        if self.random_cube==1:
            self.happy=+10    #Человек играет в игры на компютере
        if self.random_cube==2:
            self.happy=+30     #Человек бухает
            self.health=-20
        if self.random_cube==3:
            self.happy=-10    #Человек провёл уборку в доме
            self.health=+10

class Strana:
    def __init__(self, nation, count):
        self.nation=nation
        self.count=count
        self.time_obj=None
        self.humans=[]
        for i in range(1,self.count+1):
            self.time_obj=Human(money=random.randint(50,100), happy=random.randint(50,100), health=random.randint(50,100),
                                strength=random.randint(50,100),nationaliti=self.nation,
                                name=names[random.randint(0, len(names)-1)]+" "+surnames[random.randint(0, len(surnames)-1)])
            self.humans.append(self.time_obj)
            print(self.time_obj)

ogriziya=Strana(nation="ogriziya", count=10)