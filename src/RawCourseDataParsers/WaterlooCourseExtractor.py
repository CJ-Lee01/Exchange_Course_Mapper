import json
import re

if __name__ == '__main__':
    pass

with open('RawData/RAW_WATERLOO', 'r') as raw_waterloo:
    s = raw_waterloo.read()


course_lst = s.split('\n\n')

def text_to_format(s: str):
    s_strip = s.strip()
    lines = s_strip.splitlines()
    course_code = re.findall('\w+\s\d+\w?', lines[0])[0]
    course_weight = re.findall('\d\.\d\d', lines[0])[0]
    course_description = lines[2]
    prereq = ''
    for line in lines:
        if len(re.findall('Prereq:', line)) > 0:
            prereq = line
            break

    return [f'{course_code}, credits: {course_weight}\n\t{prereq}', course_description]

course_lst = [text_to_format(s) for s in course_lst if s.strip() != '']

with open('../CourseData/UWaterloo', 'w') as course_list:
    json.dump(course_lst, fp=course_list)

