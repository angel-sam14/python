# # 26/10/26
# # ----------

# # SET:creating using {} used to store multiple data type
# # unodered
# # unindexed
# # support unique element
# # mutable
# # donot allow duplicate values


# # Functions
# # ----------

# # add():new add akkan
# # update():
# # remove()
# # discard():element undenki remove akm illenki error onnum varilla
# # pop()
# # clear()

# s1={4,5,6,9}
# l1=["python","js","js","Flutter","DS","DS","DA","Python"]
# courses = []
# for course in l1:
#     if course not in courses:
#         courses.append(course)
# print(courses)
# s2 = set(l1)
# print(s2)
# s3 = {45,89,89,76,"Alan","Alan",45}
# print(type(s2))
# # d1 = dict([("name","Albin"),("rno",5),("age",18)])
# # print(d1)
# print(s1)
# print(len(s3))
# print(s3)

# new_set ={1,True,45,"Hello","",0,False}
# print(new_set)
# print(0 in new_set)
# for s in s1:
#     print(s)
# s1.add("python programming")   
# s1.update([88,89,45,4,5,6])
# s1.remove("python programming")
# # s1.remove("python programming") ---------->generates an error if not present
# s1.discard("python programming") # --------------> removes the element if exists and does not generate an error if does not exist
# s1.pop()
# s1.clear()
# print(s1)
# new_set.remove("Hello")
# new_set.add("hello world")


# # union():(|)
# # intersection():common elements(&)
# # symmetric difference:(^)
# # difference:common element remove chyum(-)
# # ethil niin ano remove akunne ath first il kodkknm
# # intersection update:
# # symmetric difference update:. operator inu nump kodukkunathilek values assign chyth kodukkn
# # update:union kndathin shesham value assign chyn
# # issuperset:
# # issubset:
# # isdisjoint:


# python = {"Hari","Amal","Arun","Pooja","Carlo"}
# mern = {"Hari","Amal","Pallavi","kavya","Reena"}
# print(python.union(mern))
# print(python | mern)
# print(python.intersection(mern))
# print(python & mern)
# print(python.symmetric_difference(mern))
# print(python ^ mern)
# print(python.difference(mern))
# print(mern.difference(python))
# print(mern - python)

# # python.symmetric_difference_update
# # python.difference_update(mern)
# # python.intersection_update(mern)
# # print(python)

# numbers = {20,40,1,2,3,4,5,6,8,11,13,26,35,42,0}
# even_numbers = {20,40,2,6,8,26,42,0,1224}

# print(numbers.issuperset(even_numbers))
# print(even_numbers.issubset(numbers))
# print((1,2).issubset({1,2}))
# print((1,2).issubset({1,2,3}))
# print((1,2,3,4).issubset({1,2,3}))
# print((1,2,3,4).issuperset({1,2,3,4}))
# print((1,3,5).isdisjoint({2,4,6}))
# print((1,3,5).isdisjoint({2,4,5,6}))