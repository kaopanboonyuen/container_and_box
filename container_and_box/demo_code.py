# Revised: March 2021

from code import Packer, Container, Box

NewPacker = Packer()

NewPacker.add_bin(Container('Container1', 1000, 1000, 3000, 70.0)) # name, width, height, depth, max_weight
NewPacker.add_bin(Container('Container2', 3000, 3000, 4000, 120.0))

NewPacker.add_item(Box('50g [Box 1]', 50, 50, 50, 2)) # name, width, height, depth, weight
NewPacker.add_item(Box('50g [Box 2]', 50, 50, 50, 2))
NewPacker.add_item(Box('50g [Box 3]', 50, 50, 50, 2))
NewPacker.add_item(Box('250g [Box 4]', 150, 150, 250, 5))
NewPacker.add_item(Box('250g [Box 5]', 150, 150, 250, 5))
NewPacker.add_item(Box('250g [Box 6]', 150, 150, 250, 5))
NewPacker.add_item(Box('250g [Box 7]', 150, 150, 250, 5))
NewPacker.add_item(Box('250g [Box 8]', 150, 150, 250, 5))
NewPacker.add_item(Box('250g [Box 9]', 150, 150, 250, 5))

NewPacker.add_item(Box('250g [Box 10]', 4000, 4000, 4250, 5))

NewPacker.pack()

for b in NewPacker.bins:
    print(":::::::::::", b.string())

    print("FITTED ITEMS:")
    for item in b.items:
        print("====> ", item.string())

    print("UNFITTED ITEMS:")
    for item in b.unfitted_items:
        print("====> ", item.string())

    print("***************************************************")
    print("***************************************************")
