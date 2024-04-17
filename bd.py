import sqlite3

connection = sqlite3.connect('DataBaze')
cursor = connection.cursor()


def get_lesson_id(class_num: int, profile_id: int) -> list:
    data = cursor.execute('SELECT lesson_id FROM timetable WHERE class = (?) AND profile_id = (?)',
                          (class_num, profile_id,))
    data = data.fetchall()
    return data


def get_number_of_lessons(class_num: int, day: str, profile_id: int) -> list:
    data = cursor.execute('SELECT profile_id FROM timetable WHERE class = (?) AND day = (?) AND profile_id = (?)', (class_num, day, profile_id))
    


def get_lesson(class_num: int, profile_id: int) -> list:
    lesson_list = get_lesson_id(class_num, profile_id)
    lesson_list = [i[0] for i in lesson_list]
    lesson_list_str = " ,".join(lesson_list)
    # print(lesson_list_str)
    data = cursor.execute('SELECT name FROM lessons WHERE id IN (?, ?, ?, ?, ?, ?, ?)', (lesson_list_str.split(' ,')[0],
                                                                                         lesson_list_str.split(' ,')[1],
                                                                                         lesson_list_str.split(' ,')[2],
                                                                                         lesson_list_str.split(' ,')[3],
                                                                                         lesson_list_str.split(' ,')[4],
                                                                                         lesson_list_str.split(' ,')[5],
                                                                                         lesson_list_str.split(' ,')[6], ))
    data = data.fetchall()
    data = [i[0] for i in data]
    return data


def get_profile_id(class_num: int) -> list:
    data = cursor.execute('SELECT profile_id FROM timetable WHERE class = (?) GROUP BY profile_id', (class_num,))
    data = data.fetchall()
    return data


def get_profiles(class_num: int) -> list:
    profiles_list = get_profile_id(class_num)
    profiles_list = [i[0] for i in profiles_list]
    profiles_list_str = " ,".join(profiles_list)
    # print(profiles_list_str)
    data = cursor.execute('SELECT name FROM profiles WHERE id IN (?, ?, ?, ?, ?)', (profiles_list_str.split(' ,')[0],
                                                                                    profiles_list_str.split(' ,')[1],
                                                                                    profiles_list_str.split(' ,')[2],
                                                                                    profiles_list_str.split(' ,')[3],
                                                                                    profiles_list_str.split(' ,')[4],))
    data = data.fetchall()
    data = [i[0] for i in data]
    return data


print(get_lesson(10, 2))

