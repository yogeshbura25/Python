let_dict = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"10","k":"11",
 "l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"20",
 "u":"21","v":"22","w":"23","x":"24","y":"25","z":"26", " ": " "}


n = input().lower()
lower_split = n.split(" ")
new_combine_list = []
for combine in lower_split:
    first_word_combine_code = ""
    first_word_combine = combine[0]
    for key in let_dict.keys():
        if first_word_combine == key:
            first_word_combine_code = let_dict[key]
    remains_combine = combine[1:]
    remains_combine_code = ""
    for per_word in remains_combine:
        for dict_key in let_dict.keys():
            if per_word == dict_key:
                remains_combine_code = remains_combine_code + "-" + let_dict[per_word]
                
                
    new_combine_word = first_word_combine_code + remains_combine_code
    new_combine_list.append(new_combine_word)
result = " ".join(new_combine_list)
print(result)