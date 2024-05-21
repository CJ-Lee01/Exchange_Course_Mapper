import re
from json import JSONDecodeError

import requests
import json

"""
Format:
JSON file in the format of 2d array
[[course code 1, course details], [course code 2, course details], ...]
"""
if __name__ == '__main__':
    pass

EXCLUDED_COURSES = {
    'PC', 'CH', 'CE', 'CA', 'CHC', 'BN', 'LC', 'BMC', 'BMF', 'BMG'
}

try:
    with open('../CourseData/NUS', 'r') as course_list:
        course_list = json.loads(course_list.read())

except (FileNotFoundError, JSONDecodeError):
    print('Getting data from NUSMods...')
    nus_courses = requests.get('https://api.nusmods.com/v2/2023-2024/moduleInfo.json').json()
    courses_list = []
    for course in nus_courses:
        if re.findall('[A-Z]+', course['moduleCode'])[0] in EXCLUDED_COURSES :
            continue
        courses_list.append((course['moduleCode'], course['description']))
    with open('../CourseData/NUS', 'w') as course_list:
        json.dump(courses_list, fp=course_list)
