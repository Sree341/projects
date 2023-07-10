# def sum_server_use_time(server):
#     total_use_time=0.0
#     for key, value in server.items():
#         total_use_time+=server[key]
#     return round(total_use_time,2)
        


# FileServer = {"EndUser1": 2.25, "EndUser2": 4.5, "EndUser3": 1, "EndUser4": 3.75, "EndUser5": 0.6, "EndUser6": 8}

# print(sum_server_use_time(FileServer)) # Should print 20.1


# def list_full_names(employee_dict):
#     new_list=[]
#     for last_name, first_names in employee_dict.items():
#         for first_name in first_names:
#             new_list.append(first_name+ " " + last_name)
#     return new_list
            
# print(list_full_names({"Ali": ["Muhammad", "Amir", "Malik"], "Devi": ["Ram", "Amaira"], "Chen": ["Feng", "Li"]}))
# # Should print ['Muhammad Ali', 'Amir Ali', 'Malik Ali', 'Ram Devi', 'Amaira Devi', 'Feng Chen', 'Li Chen']


# def invert_resource_dict(resource_dict):
#     new_dict={}
#     for category, resources in resource_dict.items():
#         for resource in resources:
#             if resource in new_dict:
#                 new_dict[resource].append(category)
#             else:
#                 new_dict[resource]=[category]
#     return (new_dict)


# print(invert_resource_dict({"Hard Drives": ["IDE HDDs", "SCSI HDDs"],
#         "PC Parts":  ["IDE HDDs", "SCSI HDDs", "High-end video cards", "Basic video cards"], "Video Cards": ["High-end video cards", "Basic video cards"]}))
# # Should print {'IDE HDDs': ['Hard Drives', 'PC Parts'], 'SCSI HDDs': ['Hard Drives', 'PC Parts'], 'High-end video cards': ['PC Parts', 'Video Cards'], 'Basic video cards': ['PC Parts', 'Video Cards']}


# wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
# new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
# wardrobe.update(new_items)
# print(wardrobe)


# def count_substring(string, sub_string):
#     count=0
#     str_len=len(string)
#     substr_len=len(sub_string)
#     for lttr in range(0,str_len-substr_len+1):
#         if string[lttr:lttr+substr_len]==sub_string:
#           count+=1
#           continue
#     return count

# print(count_substring("ABCDCDC.","CDC"))



length = 27/7
print(length)
print(round(length, 2))
print(f"The length is: {length:.2f}")