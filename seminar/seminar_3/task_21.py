list_general = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
                {"VII": " S005 "}, {" V ": " S009 "},
                {" VIII": " S007 "}]
dict_new = {}
for i in list_general:
    for i["V"] in i.values():

print(dict_new)