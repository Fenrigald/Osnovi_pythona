staff = "Иван", "Мария", "Петр", "Илья", "Сергей"
letter=[]
capital_letters={}


def thesaurus(staff):
    def same_capital_letters_sch(staff):
        return staff.startswith(my_names)
    for i in staff:
        letter.append(staff[staff.index(i)][:1])
        my_names=staff[staff.index(i)][:1]
        name_staff_test = list(filter(same_capital_letters_sch, staff))
        capital_letters[my_names] = name_staff_test
    return capital_letters


print('Результат:', thesaurus(staff))