import re

def filter_langs():
    processed_lines = [] 

    with open("lang.eris", "r") as list:
        list2 = list.readlines()
        for lang in list2:
            lang = lang.strip() 
            
            lang = re.sub(r'\(.*?\)', '', lang)
            
            lang = re.sub(r'\s[a-z]\w*', '', lang)
            processed_lines.append(lang)
    return processed_lines

def langs_list():
    filter_langs()

if  __name__ == '__main__':
    print(filter_langs())