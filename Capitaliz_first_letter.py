def format_name(f_name):
  new_string=''
  new_list=[]
  flist=f_name.split()
  for i in flist:
    temp=i.capitalize()
    new_list.append(temp)
    new_string=' '.join(new_list)
  return new_string

print(format_name("they're bill's friends from the UK."))