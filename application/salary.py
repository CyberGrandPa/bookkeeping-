import emoji
def calculate_salary():
    print("Ща зряплатку посчитаем :) ")
    main_part = float(input("Введите оклад(в рублях):OK_hand: : "))
    premium = float(input("Какая премия?(в рублях): "))
    salary = (main_part + premium)-((13 * (main_part + premium))/100)
    print(f" получаеццо {salary} рубликов твоя зряплатка  :")
    return

