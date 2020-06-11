def bottles_of_beer(bob):
    if bob<1:
        print("""No more bottles of beer on the wall, No more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall...""")
        return

    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall. {} bottles of beer!
Take one down and pass it around, {} bottles of beer on the wall...""".format(tmp,tmp,bob))
    print()
    bottles_of_beer(bob)

bottles_of_beer(99)