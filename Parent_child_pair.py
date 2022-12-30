with open("data.txt", "r") as pairs:
  data = pairs.read().split("\n")

print(len(data))
data.pop(-1)
#get only two elements.
Bol_lst = []
for i in data:
  D_term = 0 
  p = i.split(",")
  num_pair_01 = p[0].split("-")
  # ele_lst.append(expand(num_pair_01))
  num_pair_02 = p[1].split("-")
  # ele_lst.append(expand(num_pair_02))
  if int(num_pair_01[0]) <= int(num_pair_02[0]) and int(num_pair_01[1]) >= int(num_pair_02[1]):
    D_term = 1
  elif int(num_pair_02[0]) <= int(num_pair_01[0]) and int(num_pair_02[1]) >= int(num_pair_01[1]):
    D_term = 1
  else :
    D_term = 0
  Bol_lst.append(D_term)
print(Bol_lst)

#gives the number of Parent_child_pair
print(sum(Bol_lst))
