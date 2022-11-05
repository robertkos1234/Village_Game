class Quest:
    hp = 100
    power = 10
    name = ''


class Forest(Quest):
    """ Квесты с лесом"""

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.hp = cls.hp - 10
        instance.power = cls.power + 5
        return instance


rob = Quest()
elf = Forest()

print(elf.hp)
print(rob.hp)
