# Exchange_Course_Mapper
Using NLP techniques learned in CS4248 to determine similarity of courses between 2 exchange universities.

It displays the best 10 matches for each course based on the description of the course.

Dependencies:
- Sklearn
- Numpy
- Requests
## Guide
- Use the CourseGetters folder to extract course information into the JSON format with the following format:
  - ```[ [course_code, course_description], [course_code, course_description], [course_code, course_description], ... ]```
  - The model trains using the course description
- Copy the information to train on into the file `src/main/TRAIN`
- Add the course code and the course details to `src/main/TEST` in the same structure as seen in `src/main/example_TEST`
- Run the `main.py` file. I cannot get it to run from the terminal for some reason, so now I am using PyCharm to run it.

## Work(s) in Progress
- I am currently confused by Python packages, and therefore the folder structure is not as nice at the moment. Once I get the hang of Python packages, the process will be more streamlined.
- Getting it to run from the terminal. I still get the err: `from src.tf_idf_coursemappings.tf_idf_spare_cov import TfIdfMapper
ModuleNotFoundError: No module named 'src'`
- (Very low priority) Adding other algorithms which I find interesting.

## Caveats
- If the course description is vague, and there is no outline of the topics that is taught in the course, this program cannot match the course well.
