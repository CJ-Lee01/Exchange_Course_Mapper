from json import JSONDecodeError

import requests
import json

"""
Format:
JSON file with the 2 attributes:
'course_code'
'course_details'
"""

try:
    with open('./NUS_Course_List', 'r') as course_list:
        course_list = json.loads(course_list.read())

except (FileNotFoundError, JSONDecodeError):
    print('Getting data from NUSMods...')
    nus_courses = requests.get('https://api.nusmods.com/v2/2023-2024/moduleInfo.json').json()
    courses_list = []
    for course in nus_courses:
        courses_list.append((course['moduleCode'], course['description']))
    with open('./NUS_Course_List', 'w') as course_list:
        json.dump(courses_list, fp=course_list)
