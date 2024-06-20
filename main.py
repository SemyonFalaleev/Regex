import csv
import re

def change_name(contact_list):
    correct_contact_list = []
    for contact in contact_list[1:]:
        name = contact[0:3]
        name_str = (' ').join(name).rstrip()
        name = name_str.split(' ')
        contact[0] = name[0]
        contact[1] = name[1]
        try:
            contact[2] = name[2]
        except IndexError:
            pass
        coincidences = [idx for idx, x in enumerate(correct_contact_list)
        if x[0] == contact[0] and x[1] == contact[1]]
        try:
            contact_coincidence = correct_contact_list[coincidences[0]]
            for indx, info in enumerate(contact_coincidence):
                if contact[indx] == info:
                    continue
                elif info == '':
                    correct_contact_list[coincidences[0]][indx] = contact[indx]
        except IndexError:
            correct_contact_list.append(contact)
            continue
    return correct_contact_list

def change_phone_number(contact_list):
    pattern = r"(\+7|8)\s*\(*(\d{3})[\)\s-]*(\d{3})[\)\s-]*[-|\s]*([\d]{2})[-\s]*([\d]{2})[\s+\(]*(доб\.)?\s*(\d+)?"
    result = []
    for element in contact_list:
        element_str = ','.join(element)
        element_change = re.sub(pattern, r"+7(\2)\3-\4-\5 \6\7", element_str)
        result.append(element_change.split(","))
    return result
if __name__ == "__main__":
    with open('phonebook_raw.csv', encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=',')
        contact_list = list(rows)
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(change_phone_number(change_name(contact_list)))

