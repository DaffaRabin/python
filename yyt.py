#create list of "my hobby"
my_hobby=['coding','reading','eating','drawing']

#['coding','reading','eating','drawing']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ArithmeticError                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 #['coding','reading','eating','drawing']
print my_hobby

#get first element of list
#use name_of_list followed by[0]
#example
print my_hobby[0]
print "my first hobby is {}".format(my_hobby[0])


print len(my_hobby)
print "I have {} hobbies".format(len(my_hobby))
print""

#print all off items on a list
for name_of_varible in my_hobby:
    print name_of_varible
print""

#adding and item to a list
#use name_of_list.append(item)
hobby=raw_input("input a hobby to be added")
my_hobby.append(hobby)
print my_hobby
