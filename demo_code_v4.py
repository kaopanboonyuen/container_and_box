# Revised: July 2021

from code import Packer, Container, Box

#Step1 
NewPacker = Packer()

#Step2 add Container        # name, width, height, depth, max_weight
NewPacker.add_bin(Container('Container1', 310, 210, 360, 25000.0))

#Step3 add Box
#						# name, width, height, depth, weight
NewPacker.add_item(Box('[Box 1]', 200, 200, 150, 50)) 
NewPacker.add_item(Box('[Box 2]', 100, 150, 150, 50))
NewPacker.add_item(Box('[Box 3]', 100, 150, 100, 50))
NewPacker.add_item(Box('[Box 4]', 100, 150, 100, 50)) 
NewPacker.add_item(Box('[Box 5]', 100,  150, 100, 80))
NewPacker.add_item(Box('[Box 6]', 75, 65, 50, 100)) 
NewPacker.add_item(Box('[Box 7]', 75, 65, 50, 100)) 
NewPacker.add_item(Box('[Box 8]', 75, 65, 50, 100))
NewPacker.add_item(Box('[Box 9]', 75, 65, 50, 100)) 
NewPacker.add_item(Box('[Box 10]', 50, 135, 25, 100))
NewPacker.add_item(Box('[Box 11]', 50, 100, 50, 80)) 
NewPacker.add_item(Box('[Box 12]', 50, 100, 50, 80)) 
NewPacker.add_item(Box('[Box 13]', 50, 100, 50, 80))
NewPacker.add_item(Box('[Box 14]', 50, 100, 50, 100))
NewPacker.add_item(Box('[Box 15]', 100, 50, 100, 100)) 
NewPacker.add_item(Box('[Box 16]', 100, 50, 100, 50))
NewPacker.add_item(Box('[Box 17]', 100, 50, 100, 50))
NewPacker.add_item(Box('[Box 18]', 100, 50, 150, 50))
NewPacker.add_item(Box('[Box 19]', 100, 100, 50, 80))
NewPacker.add_item(Box('[Box 20]', 100, 100, 50, 80))
NewPacker.add_item(Box('[Box 21]', 50, 200, 50, 50))
NewPacker.add_item(Box('[Box 22]', 50, 200, 50, 50))
NewPacker.add_item(Box('[Box 23]', 50, 135, 25, 100))
NewPacker.add_item(Box('[Box 24]', 50, 135, 25, 100))
NewPacker.add_item(Box('[Box 25]', 50, 135, 25, 100))
NewPacker.add_item(Box('[Box 26]', 50, 135, 25, 100))
NewPacker.add_item(Box('[Box 27]', 50, 135, 25, 100))
NewPacker.add_item(Box('[Box 28]', 50, 135, 25, 100))
NewPacker.add_item(Box('[Box 29]', 50, 80, 25, 100))
NewPacker.add_item(Box('[Box 30]', 50, 80, 25, 100))
NewPacker.add_item(Box('[Box 31]', 50, 80, 25, 100))
NewPacker.add_item(Box('[Box 32]', 50, 80, 25, 100))
NewPacker.add_item(Box('[Box 33]', 50, 80, 25, 100))
NewPacker.add_item(Box('[Box 34]', 50, 55, 25, 100))
NewPacker.add_item(Box('[Box 35]', 50, 55, 25, 100))
NewPacker.add_item(Box('[Box 36]', 50, 55, 25, 100))
NewPacker.add_item(Box('[Box 37]', 50, 55, 25, 100))
NewPacker.add_item(Box('[Box 38]', 50, 55, 25, 100))
NewPacker.add_item(Box('[Box 39]', 50, 55, 25, 100))
NewPacker.add_item(Box('[Box 40]', 50, 55, 25, 250000))

NewPacker.pack(status='Normal') # 'Normal', 'Size', 'Height'

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
