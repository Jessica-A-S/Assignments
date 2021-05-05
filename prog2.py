def main():
    vegetarian = input("Is anyone in your party vegetarian? ".lower())
    vegan = input("Is anyone in your party vegan? ".lower())
    gluten_free = input("Is anyone in your party gluten free? ".lower())
    print("Here are your restaurant choices:")
    if vegetarian == "yes" and vegan == "yes":
        if gluten_free == "yes":
            print("Corner Cafe", "\nThe Chef's Kitchen")
        else:
            print("Corner Cafe", "\nThe Chef's Kitchen")
    elif vegetarian == "yes" and vegan == "no":
        if gluten_free == "yes":
            print("Main Street Pizza", "\nCorner Cafe", "\nThe Chef's Kitchen")
        else:
            print("Main Street Pizza", "\nCorner Cafe", "\nLuigi's Fine Italian Restaurant", "\nThe Chef's Kitchen")
    elif vegetarian == "no" and vegan == "yes":
        if gluten_free == "yes":
            print("Corner Cafe", "\nThe Chef's Kitchen")
        else:
            print("Corner Cafe", "\nThe Chef's Kitchen")
    else:
        if gluten_free == "yes":
            print("Main Street Pizza", "\nCorner Cafe", "\nThe Chef's Kitchen")
        else:
            print("Joe's Gourmet Burgers", "\nMain Street Pizza", "\nCorner Cafe", "\nLuigi's Fine Italian Restaurant",
                  "\nThe Chef's Kitchen")


main()
