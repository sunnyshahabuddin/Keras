from datetime import datetime, timedelta

current_date = datetime.now()
start_of_month = current_date.replace(day=1)
next_month = start_of_month.replace(month=start_of_month.month + 1, day=1)
end_of_month = next_month - timedelta(days=1)

start_of_month_str = start_of_month.strftime('%Y-%m-%d')
end_of_month_str = end_of_month.strftime('%Y-%m-%d')

print(f"Start date of the current month: {start_of_month_str}")
print(f"End date of the current month: {end_of_month_str}")
