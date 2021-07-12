from humans.child import Child
from basetypes.human import HumanSex
from basetypes.goverment import TaxPayer


if __name__ == "__main__":
    print("starting app")
    ch1 = Child(5)
    ch2 = Child(17)

    ch2.name = "Alice"
    ch2.sex = HumanSex.FEMALE

    ch1.make_friend(ch2)
    ch1.drive_car()
    ch1.drink()
    print(ch1.thirsty)

    adult = ch2.grow_older()
    print(adult.get_age())
    print(ch2.get_age())

    ch3 = ch2.make_child()
    print(ch3)
    if not ch3:
        ch3 = adult.make_child()
        print(ch3)

    tax = TaxPayer(
        human=adult
    )

    print(tax)
