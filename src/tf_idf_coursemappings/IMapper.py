from typing import Iterable, Tuple, List


class IMapper:

    def train_modules(self, module_lst: Iterable[Tuple[str, str]]):
        """
        Trains the model based on the modules given.
        :param module_lst: List of tuples, with 1st elem being the course identifier and 2nd elem being the course description.
        :return:
        """
        raise NotImplementedError

    def get_course_mappings(self, module_lst: Iterable[Tuple[str, str]]) -> List[Tuple[str, str, float]]:
        """
        Matches the query to the trained modules.
        :param module_lst: List of modules to map to.
        :return: List of similar modules, with a similarity score given.
        """
        raise NotImplementedError
