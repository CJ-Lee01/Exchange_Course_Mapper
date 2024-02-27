# Exchange_Course_Mapper
Using NLP techniques learned in CS4248 to determine similarity of courses between 2 exchange universities.

It displays the best 5 matches for each course based on the description of the course.

Dependencies:
- Sklearn
- Numpy

## Guide
- Use the CourseGetters folder to extract course information into the JSON format with the following format:
  - ```[ [course_code, course_description], [course_code, course_description], [course_code, course_description], ... ]```
  - The model trains using the course description
- Copy the information to train on into the file `src/tf_idf_coursemappings/TRAIN`
- Modify the array in the `src/tf_idf_coursemappings/main.py`, following the same format as the example given in the program.
- Run `python3 ./main.py` in the `src/tf_idf_coursemappings` folder (in terminal). Alternatively if you use PyCharm you can just run from the file.

## Work(s) in Progress
- I am currently confused by Python packages, and therefore the folder structure is not as nice at the moment. Once I get the hang of Python packages, the process will be more streamlined.