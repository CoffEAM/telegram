import sqlite3

connection = sqlite3.connect('DataBaze')
cursor = connection.cursor()


def get_lesson_id(class_num: int, profile_id: int) -> list:
    data = cursor.execute('SELECT lesson_id FROM timetable WHERE class = (?) AND profile_id = (?) ORDER BY num ASC ',
                          (class_num, profile_id,))
    data = data.fetchall()
    print(data)
    return data


def get_lesson(class_num: int, profile_id: int) -> list:
    lesson_list_obj = get_lesson_id(class_num, profile_id)
    lessons = []
    for i in lesson_list_obj:
        data = cursor.execute('SELECT name FROM lessons WHERE id = (?)',(i[0],)).fetchall()
        lessons.append(data[0][0])

    print(lessons)
    return lessons


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

