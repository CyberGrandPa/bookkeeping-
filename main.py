from application.salary import calculate_salary
from application.DB.people import get_employees
import datetime
import emoji
emoji.LANGUAGES = 'ru'

if __name__ == '__main__':
    current_date = datetime.date.today().isoformat()
    print(current_date)
    print(emoji.emojize(':thumbs_up:'))
    calculate_salary()
    get_employees()










