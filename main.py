from enemy import Enemy, Troll, Vampire

ugly_troll = Troll("Pug")
print(f"Ugly troll - {ugly_troll}")

another_troll = Troll("Ug")
print(f"Another troll - {another_troll}")
another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vamp1 = Vampire("Damon")
vamp2 = Vampire("Stefan")
print(f"Vampire - {vamp2}")
vamp1.suction()

vamp1.take_damage(5)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

while vamp1.alive:
    if not vamp1.dodges():
        vamp1.take_damage(1)
        print(vamp1)
