import math

import numpy as np
from typing import Iterable, Tuple, List, Dict

from nltk.tokenize import wordpunct_tokenize

from IMapper import IMapper
from sklearn.feature_extraction.text import TfidfVectorizer


class TfIdfMapper(IMapper):

    def __init__(self):
        self.vectorizer: TfidfVectorizer = TfidfVectorizer(sublinear_tf=True, stop_words='english')
        self.course_code_lst: np.ndarray | None = None
        self.course_vector: np.ndarray | None = None

    def train_modules(self, module_lst: Iterable[Tuple[str, str]]):
        course_details_lst = []
        course_code_lst = []
        for course_code, course_details in module_lst:
            course_code_lst.append(course_code)
            course_details_lst.append(course_details)
        self.course_vector = self.vectorizer.fit_transform(course_details_lst).toarray()
        self.course_code_lst = np.array(course_code_lst)

    def get_course_mappings(self, module_lst: Iterable[Tuple[str, str]]) -> List[Tuple[str, List[Tuple[str, float]]]]:
        course_code_lst = []
        course_detail_lst = []
        for course_code, detail in module_lst:
            course_code_lst.append(course_code)
            course_detail_lst.append(detail)
        course_vector = self.vectorizer.transform(course_detail_lst).toarray()
        result: np.ndarray = course_vector @ self.course_vector.T
        similarity_courses: np.ndarray = result.argpartition(-5, axis=1)[:, -5:]
        result.partition(-5, axis=1)
        scores = result[:, -5:].round(5)
        ret = list(zip(course_code_lst, self.course_code_lst[similarity_courses], scores))
        ret_2 = []
        for code, lst, scores in ret:
            ret_2.append(
                (
                    code,
                    sorted(zip(lst, scores), key=lambda s: s[1], reverse=True)
                )
            )
        return ret_2