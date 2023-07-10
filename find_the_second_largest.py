# Program using function
# list_1=[1,2,7,3,4,9,7,1]
# list_2=list(set(list_1))
# print(f" The second largest number is: {list_2[-2]}")


# Program without using function

list1=[5,4,3,8,6,9] 
new_list=[]
def find_min(x):
  min=x[0]
  for i in x:
      if min>i:
        min=i
  return min

for j in range(len(list1)):
   min_catch=find_min(list1)
   new_list.append(min_catch)
   list1.remove(min_catch)

print(new_list)
print("The second largest number is: ", new_list[-2])
new_list.sort(reverse=True)
print(new_list)


