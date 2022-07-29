
##==============================Strings============
#a1 = 'Hello'
#a2 = 'World'
#a4 = 'Who'

#a3 =  "{:<10} {:<10}"
#a4 =  "{:10} {:10}"
#a5 =  "{:>10} {:>10}"


#print(a3.format('Ivan!', "Ne Ivan"))
#print(a4.format('Ivan!', "Ne Ivan"))
#print(a5.format('Ivan!', "Ne Ivan"))

##========================List============

#list1 = [1,'2', [1,2,'7']]
#dict1 = {1:'hi', 2:'2'}
#list2 = list(dict1)
#print(list1[2][2])
#print(list2)
#print(list1.index(2))

##================dict===================
##=============================




#vlans = ['1', '30', '11', '3', '10', '20', '30', '100']
#vlans2 = {}
#for i, y in enumerate(vlans):
#    vlans2[i] = int(y)
#print(sorted(vlans2))

##=====================Tasks======================
#nums = [1, 2, 3, 4, 5]

#nums2 = [100, 200, 300, 400, 500]

#print([x * y for x, y in zip(nums, nums2)])

##===================File=========================



file = open('new_text.txt', 'wt')

x = 'Привет андрей \n'

file.write(x)

file.close()

print(file.closed)

file = open('new_text.txt', 'r')

print(file.read())

print("Ну ты валера и чмо")

x = 10/56