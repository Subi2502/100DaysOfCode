#Create a class for a student with attributes like name, age, and grade.
# print ("\nSubi - Day 35 of #100DaysOfCode\n") 
# print("\nclass for a student with attributes like name, age, and grade\n")

# class Student:
#   def __init__(self, name, age, grade):
#     self.name = name
#     self.age = age
#     self.grade = grade

#   def get_student_info(self):
#     return f"Student(name: {self.name}, age: {self.age}, grade: {self.grade})"

# s1 = Student("nancy", 12, "A")
# s2 = Student("rose", 14, "B")

# print(s1.get_student_info())
# print(s2.get_student_info())


#Implement a class for a simple game character.
print ("\nImplement a class for a simple game character\n") 
    
class GameCharacter:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def take_damage(self, damage):
        actual_damage = max(damage - self.defense, 0)
        self.health -= actual_damage

    def attack(self, target):
        damage = self.attack_power
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack: {self.attack_power}, Defense: {self.defense})"

if __name__ == "__main__":
    player = GameCharacter("Hero", 50, 10, 8)
    enemy = GameCharacter("villain", 65, 15, 10)

    while player.is_alive() and enemy.is_alive():
        player.attack(enemy)
        if enemy.is_alive():
            enemy.attack(player)

    if player.is_alive():
        print(f"{player.name} wins!")
    else:
        print(f"{enemy.name} wins!")
