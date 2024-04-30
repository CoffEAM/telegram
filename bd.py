# import sqlite3
#
# connection = sqlite3.connect('DataBaze')
# cursor = connection.cursor()
#
#
# def get_lesson_id(class_num: int, profile_id: int, day: str) -> list:
#     data = cursor.execute('SELECT lesson_id FROM timetable WHERE class = (?) AND profile_id = (?) AND day = (?) ORDER BY num ASC',
#                           (class_num, profile_id, day))
#     data = data.fetchall()
#     nums = get_num_lesson(class_num, profile_id, day)
#     dicts = {}
#
#     for i in range(len(data)):
#         dicts[nums[i][0]] = int(data[i][0])
#
#     return dicts
#
#
# def get_num_lesson(class_num: int, profile_id: int, day: str) -> dict:
#     data = cursor.execute('SELECT num FROM timetable WHERE class = (?) AND profile_id = (?) AND day = (?) ORDER BY num ASC',
#                           (class_num, profile_id, day)).fetchall()
#
#     return data
#
#
# def get_lesson(class_num: int, profile_id: int, day: str) -> list:
#     lesson_list_obj = list(dict(get_lesson_id(class_num, profile_id, day)).values())
#     lessons = []
#     for i in lesson_list_obj:
#         data = cursor.execute('SELECT name FROM lessons WHERE id = (?)', (i,)).fetchall()
#         lessons.append(data[0][0])
#
#     return lessons
#
#
# def get_id_of_time(class_num: int, profile_id: int, day: str) -> list:
#     data = cursor.execute('SELECT time_id FROM timetable WHERE class = (?) AND profile_id = (?) AND day = (?) ORDER BY num ASC',
#                           (class_num, profile_id, day)).fetchall()
#
#     return data
#
#
# def get_time_of_lesson(class_num: int, profile_id: int, day: str) -> list:
#     time_list = get_id_of_time(class_num, profile_id, day)
#     times = []
#     for i in time_list:
#         data = cursor.execute('SELECT time FROM time WHERE id = (?)', (i[0],)).fetchall()
#         times.append(data[0][0])
#
#     return times
#
#
# def get_profile_id_by_name(name_of_profile: str) -> list:
#     data = cursor.execute('SELECT id FROM profiles WHERE name = (?)', (name_of_profile, )).fetchall()
#
#     return data
#
#
# def get_profile_id(class_num: int) -> list:
#     data = cursor.execute('SELECT profile_id FROM timetable WHERE class = (?) GROUP BY profile_id', (class_num,))
#     data = data.fetchall()
#
#     return data
#
#
# def get_profiles(class_num: int) -> list:
#     profiles_list = get_profile_id(class_num)
#     profiles_list = [i[0] for i in profiles_list]
#     profiles_list_str = " ,".join(profiles_list)
#     # print(profiles_list_str)
#     data = cursor.execute('SELECT name FROM profiles WHERE id IN (?, ?, ?, ?, ?)', (profiles_list_str.split(' ,')[0],
#                                                                                     profiles_list_str.split(' ,')[1],
#                                                                                     profiles_list_str.split(' ,')[2],
#                                                                                     profiles_list_str.split(' ,')[3],
#                                                                                     profiles_list_str.split(' ,')[4],))
#     data = data.fetchall()
#     data = [i[0] for i in data]
#     return data
#
#
# print(get_lesson_id(10, 2, 'пн'))
# print(get_lesson(10, 2, 'пн'))
# print(get_time_of_lesson(10, 2, 'пн'))
#
#
#
