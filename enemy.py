# class Enemy:
class Enemy(object): 
    
    def __init__(self, name='Enemy', hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True
                
    def take_damage(self, damage):
        remaining_points =self.hit_points - damage
        if remaining_points >=0:
            self.hit_points = remaining_points
            print(f"I took {damage} points damage and have {self.hit_points} left")
        else:
            self.lives -= 1
            if self.lives > 0:
                print(f"{self.name} lost a life")
            else:
                print(f"{self.name} is dead")
                self.alive = False
                            
    def __str__(self):
        return f"Name: {self.name}, Lives: {self.lives}, Hit points: {self.hit_points}"
    

class Troll(Enemy):

    # def __init__(self, name):
        # Enemy.__init__(self, name=name, lives=1, hit_points=23)

    def __init__(self, name):
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print(f"Me {self.name}. {self.name} stomp you.")

class Vampire(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)

    def suction(self):
        print(f"I'm {self.name}. I will suck you out to death.")
        

