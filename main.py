from datetime import datetime, timedelta


users = [
    {"name": "Bill", "birthdate": datetime(year=1990, month=12, day=30)},
    {"name": "Gill", "birthdate": datetime(year=1990, month=1, day=1)},
    {"name": "Till", "birthdate": datetime(year=1990, month=1, day=2)},
    {"name": "Dill", "birthdate": datetime(year=1990, month=1, day=3)},
    {"name": "Bilg", "birthdate": datetime(year=1990, month=1, day=4)},
    {"name": "Gilg", "birthdate": datetime(year=1990, month=1, day=8)},
    {"name": "Tilg", "birthdate": datetime(year=1990, month=1, day=6)},
    {"name": "Dilg", "birthdate": datetime(year=1990, month=1, day=6)},
]

current_date = datetime.now().date()
start_period = current_date - timedelta(days=current_date.weekday()) + timedelta(days=5)
end_period = start_period + timedelta(days=6)
print(start_period, end_period)


def get_str_period(start_period: datetime, end_period: datetime) -> dict:
    delta = end_period - start_period
    days = [start_period + timedelta(days=i) for i in range(delta.days + 1)]
    return {d.strftime("%m-%d"): d.strftime("%Y") for d in days}
    # print({d.strftime("%m-%d"): d.strftime("%Y") for d in days})


def get_birthdays_per_week(users: list):
    current_week_bd = {}
    period_bd = get_str_period(start_period, end_period)
    for user in users:
        user_bd = datetime.strftime(user["birthdate"], "%Y-%m-%d")
        if user_bd[5:] in period_bd:
            cur_year_bd = user_bd.replace(str(user_bd[0:4]), period_bd[user_bd[5:]])
            if cur_year_bd[5:] in list(period_bd):
                day = datetime.strptime(cur_year_bd, "%Y-%m-%d")
                day_name = day.strftime("%A")
                if day_name == "Saturday" or day_name == "Sunday":
                    day_name = "Monday"
                if day_name not in current_week_bd.keys():
                    current_week_bd[day_name] = user["name"]
                else:
                    new_user = current_week_bd[day_name] + ", " + user["name"]
                    current_week_bd[day_name] = new_user

    print("Happy Birthday!")
    for day_bd, user in current_week_bd.items():
        print(f"{day_bd}: {user}")


get_birthdays_per_week(users)
