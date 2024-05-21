from src.MappingAlgorithms import TfIdfMapper
from src.Parsers import *
import json

if __name__ == '__main__':
    # for me to conveniently run on PyCharm
    pass

courses_for_list = get_courses_wishlist()

courses_from_list = course_data_getter_FROM('UWaterloo')


mapper = TfIdfMapper(max_df=0.5, top_n=10, ngram_range=(1,2))
mapper.train_modules(courses_from_list)
mappings = mapper.get_course_mappings(courses_for_list)

for course, course_maps in mappings:
    print(course)
    for c, score in course_maps:
        print('\t', f'similarity: {score}', c)
        print('')
    print("\n\n")
