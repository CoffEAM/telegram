from google.oauth2.service_account import Credentials
import gspread
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'neural-journey-421315-e2648fbc0c3e.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)

timetable_sheet = gc.open("shsheduler").worksheet("timetable")
profiles_sheet = gc.open("shsheduler").worksheet("profiles")
lessons_sheet = gc.open("shsheduler").worksheet("lessons")
time_sheet = gc.open("shsheduler").worksheet("time")

profiles_list = profiles_sheet.get('B3:B7')

timetable_all_values = timetable_sheet.get_all_values()
profiles_all_values = profiles_sheet.get_all_values()
lessons_all_values = lessons_sheet.get_all_values()
time_all_values = time_sheet.get_all_values()


def get_lesson_id(class_num: int, profile_id: int, day: str) -> list:
    lessons = []
    for i in timetable_all_values:
        if str(class_num) == i[2] and str(profile_id) == i[4] and day == i[5]:
            lessons.append(i[6])

    return lessons


def get_num_of_lesson(class_num: int, profile_id: int, day: str) -> list:
    nums = []
    for i in timetable_all_values:
        if str(class_num) == i[2] and str(profile_id) == i[4] and day == i[5]:
            nums.append(i[1])

    return nums


def get_lesson(class_num: int, profile_id: int, day: str) -> list:
    lessons = []
    lessons_id = get_lesson_id(class_num, profile_id, day)
    for i in lessons_id:
        for j in lessons_all_values:
            if j[0] == i:
                lessons.append(j[1])

    return lessons


def get_id_of_time(class_num: int, profile_id: int, day: str) -> list:
    times = []
    for i in timetable_all_values:
        if str(class_num) == i[2] and str(profile_id) == i[4] and day == i[5]:
            times.append(i[7])

    return times


def get_time_of_lesson(class_num: int, profile_id: int, day: str) -> list:
    times = []
    id_times = get_id_of_time(class_num, profile_id, day)
    values = time_all_values
    for i in id_times:
        for j in values:
            if j[0] == i:
                times.append(j[1])

    return times


def get_profile_id_by_name(name_of_profile: str) -> list:
    profile_id = ''

    for i in profiles_all_values:
        if i[1] == name_of_profile:
            profile_id = i[0]

    return profile_id


def get_profiles() -> list:
    profiles = []
    for i in profiles_list:
        profiles.append(i[0])

    return profiles



