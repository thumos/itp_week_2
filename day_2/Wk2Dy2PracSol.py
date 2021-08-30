def use_poke_ball():
    print("You threw a poke ball")

#use_poke_ball()


pokemon = input("What did you catch?")
def catch_pokemon():
    print("You caught a " + pokemon)

#catch_pokemon("Ryachu")
def catch_em_all():
    use_poke_ball()
    catch_pokemon()

catch_em_all()