import random
from enum import Enum


class HumanState:
    def __init__(self, state: str):
        self.state = state

    def __str__(self):
        return self.state


class HumanSex(Enum):
    MALE = 1
    FEMALE = 2
    rand = random.choice([FEMALE, MALE])


class Human:
    """ base class of humanoids """
    # __doc__ defined above
    def __init__(self, age=0):
        self._age = age

    def check_adult(f):
        def checking(self, *args, **kwargs):
            if self.get_age() < 18:
                print("I'm not 18 years old")
                return False
            return f(self, *args, **kwargs)

        return checking

    state: HumanState = HumanState("calm")
    name: str = "Bob"
    sex: HumanSex = HumanSex.MALE
    greeting: str = "Hello!"
    _age: int
    starve: bool = True
    thirsty: bool = True

    # getter and setter for _age
    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> bool:
        self._age = age
        return True

    def __call__(self, *args, **kwargs):
        # greets you when call
        print(self.greeting)
        return self.greeting

    def __str__(self):
        # returns info about human
        return f'{self.name}: age is {self._age}'

    def eat(self) -> bool:
        # eat if it's starving
        if self.starve:
            self.starve = False
            return True
        print("I don't want to eat")
        return False

    def drink(self) -> bool:
        if self.thirsty:
            self.thirsty = False
            return True
        print("i'm not thirsty")
        return False

    def change_state(self, state: HumanState) -> bool:
        self.state = state
        return True

    @check_adult
    def drive_car(self) -> bool:
        self.change_state(HumanState('driving car'))
        return True

    def grow_older(self):
        self.set_age(self.get_age() + 1)
        print("Happy birthday!")

    @check_adult
    def make_child(self):
        h = Human(0)
        h.sex = HumanSex.rand
        return h
