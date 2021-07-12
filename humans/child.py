from basetypes.human import Human


class Child(Human):
    def drive_car(self) -> bool:
        return False

    def drink(self) -> bool:
        if super().drink():
            print("Mom, can I have a drink?")
            return True
        return False

    def grow_older(self) -> Human:
        super().grow_older()
        if self.get_age() >= 18:
            self.set_age(17)
            return Human(18)

    def make_friend(self, h: Human):
        print(f"Let's be friends {h.name}")
