def count_vowels(stri):
    con_vow,con_cons,con_digi,con_space = 0,0,0,0
    for i in stri:
        if i.isdigit():
            con_digi += 1
            continue
        if i.isspace():
            con_space += 1
            continue
        if i.lower() in ['a','i','o','e','u']:
            con_vow += 1
        else:
            con_cons += 1
    print(f'{con_vow},{con_cons},{con_digi},{con_space}')
    
count_vowels("Hello 123")   

            