# Идея:
# 5 классов донатов на сервере майнкрафт с привелигиями и командами доступными.Каждая привелегия выше имеет функции доната ниже


class VIP:
    def __init__(self):
        self.go_spawn = True
        self.tp_player = True
        self.set_home = 5
        super().__init__()


class Premium:
    def __init__(self):
        super().__init__()
        self.give_money = True
        self.ban = True
        self.gm1 = True


class Legend(VIP, Premium):
    def __init__(self):
        super().__init__()
        self.vanish = True
        self.restart_server = True
        self.set_home = 10


class Moderator(Legend, Premium):
    def __init__(self):
        super().__init__()
        self.ban_forever = True
        self.balance = "10_Bilions $"
        self.mute = True


class Owner(Moderator, Legend):
    def __init__(self):
        super().__init__()
        self.balance = "Infinity"
        self.give_donate = True
        self.console = True


class Donate(Owner, Moderator):
    def print_info(self):
        d = f"Возможности Доступные "
        print(f"{d:=^50}")

        print(f"Бан: {self.ban}")
        print(f"Бан навсегда: {self.ban_forever}")
        print(f"баланс: {self.balance}")
        print(f"мут: {self.mute}")
        print(f"ГМ1: {self.gm1}")
        print(f"спавн: {self.go_spawn}")
        print(f"тп к игроку: {self.tp_player}")
        print(f"выдать донат {self.give_donate}")
        print(f"дать денег: {self.give_money}")
        print(f"ваниш: {self.vanish}")
        print(f"Доступных точек дома: {self.set_home}")
        print(f"рестарт сервера: {self.restart_server}")


Donates = Donate()
Donates.print_info()
