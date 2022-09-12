from enemy import Enemy, Troll

ugly_troll = Troll("Pug")
print(f"Ugly troll - {ugly_troll}")

another_troll = Troll("Ug")
print(f"Another troll - {another_troll}")

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()
