from datetime import datetime


def get_deadline(start_date: str, deadline: int, time_format='weeks'):
    seconds_in_month = 30.44 * 24 * 60 * 60
    seconds_in_week = 7 * 24 * 60 * 60
    seconds_in_day = 24 * 60 * 60
    seconds_in_hour = 3600

    [year, month, day] = start_date.split('-')[0].split(' ')
    year = int(year)
    month = int(month)
    day = int(day)

    start_datetime_object = datetime(int(year), int(month), int(day))
    start_timestamp = datetime.timestamp(start_datetime_object)

    current_date = datetime.now()
    current_timestamp = datetime.timestamp(current_date)

    if current_timestamp > start_timestamp and time_format == 'weeks':
        deadline_epoch_date = start_timestamp + (deadline * seconds_in_week)
        deadline_date = datetime.fromtimestamp(deadline_epoch_date)

        seconds_passed = current_timestamp - start_timestamp
        deadline_in_seconds = deadline * seconds_in_week
        time_left_in_seconds = deadline_in_seconds - seconds_passed
        weeks_left = time_left_in_seconds // seconds_in_week
        days_left = (time_left_in_seconds % seconds_in_week) // seconds_in_day

        if time_left_in_seconds > 0:
            return {
                "deadline": f"{deadline} weeks",
                "estimated-deadline-date": f"{deadline_date.month}/{deadline_date.day}/{deadline_date.year}",
                "weeks-left": round(weeks_left),
                "days-left": round(days_left),
            }

        else:
            return {
                "info": "Deadline has been exhausted",
                "relative": abs(round(weeks_left))
            }

    elif current_timestamp > start_timestamp and time_format == 'months':
        deadline_epoch_date = start_timestamp + (deadline * seconds_in_month)
        deadline_date = datetime.fromtimestamp(deadline_epoch_date)

        seconds_passed = current_timestamp - start_timestamp
        deadline_in_seconds = deadline * seconds_in_month
        time_left_in_seconds = deadline_in_seconds - seconds_passed
        months_left = time_left_in_seconds // seconds_in_month
        weeks_left = round((time_left_in_seconds % seconds_in_month) // seconds_in_week)
        days_left = round((time_left_in_seconds % seconds_in_month) % seconds_in_week) // seconds_in_day

        if time_left_in_seconds > 0:
            return {
                "deadline": f"{deadline} months",
                "estimated-deadline-date": f"{deadline_date.month}/{deadline_date.day}/{deadline_date.year}",
                "months-left": round(months_left),
                "weeks-left": weeks_left,
                "days-left": round(days_left),
            }

        else:
            return {
                "info": "Deadline has been exhausted",
                "relative": f"{abs(round(months_left))} months ago"
            }

    elif current_timestamp < start_timestamp:
        return {
            "info": "Project start date has not been reached",
            "estimated_start_date":
                f"{start_datetime_object.month}/{start_datetime_object.day}/{start_datetime_object.year}",
            "hours-to-start": f"{round(start_timestamp - current_timestamp) // seconds_in_hour} hours"
        }


# TEST
# print(get_deadline('Aug 2 2021', 12, 'weeks'))
