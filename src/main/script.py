from src.main.test_parser import parse_text
from src.tf_idf_coursemappings.tf_idf_spare_cov import TfIdfMapper
import json

if __name__ == '__main__':
    # for me to conveniently run on PyCharm
    pass

with open('./TEST', 'r') as test_data:
    test_set = parse_text(test_data.read())

with open('./TRAIN', 'r') as trn_data:
    temp = json.loads(trn_data.read())
    training_set = [tuple(t) for t in temp]

mapper = TfIdfMapper(0.25, top_n=10)
mapper.train_modules(training_set)
mappings = mapper.get_course_mappings(test_set)

for course, course_maps in mappings:
    print(course)
    print('\t', course_maps)
