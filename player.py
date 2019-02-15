# Create a class called Player.
class Player:
    # Every player should have three attributes: gold_coins, health_points, and lives.
    # lives should start at 5.
    # gold_coins should start at 0.
    # health_points should start at 10.
    def __init__(self,gold=0,health=10,lives=5):
        self.gold_coins = gold
        self.health_points = health
        self.lives = lives

    # Define an __str__() instance method.
    def __str__(self):
        return("This player currently has {} gold, {} health points, and {} lives remaining.".format(self.gold_coins,self.health_points,self.lives))

    # Your class should have an instance method called level_up that increases lives by one.
    def level_up(self):
        self.lives += 1

    # Your class should have an instance method called collect_treasure that increases gold_coins by one. If gold_coins is a multiple of ten (eg, 10, 20, 30,
    #and so on) then the collect_treasure method should run the level_up method.
    def collect_treasure(self):
        self.gold_coins += 1
        if self.gold_coins % 10 == 0:
            self.level_up()

    # Your class should have an instance method called do_battle that accepts one damage argument and subtracts it from the player's health_points.
    #If health_points falls below one, subtract one from lives and reset health_points to ten. If you have run out of lives, this method should run another
    #method called restart (see below).
    def do_battle(self,damage):
        self.health_points -= damage
        if self.health_points < 1:
            self.lives -= 1
            self.health_points = 10
            # if self.lives < 1:
            #     self.restart()

    # The restart instance method should set all attributes back to their starting values (5, 0, and 10).

p1 = Player()
print(p1)
p1.collect_treasure()
p1.collect_treasure()
p1.collect_treasure()
p1.collect_treasure()
p1.collect_treasure()
p1.collect_treasure()
p1.collect_treasure()
p1.collect_treasure()
p1.collect_treasure()
print(p1)
p1.collect_treasure()
print(p1)
p1.do_battle(5)
print(p1)
p1.do_battle(6)
print(p1)
