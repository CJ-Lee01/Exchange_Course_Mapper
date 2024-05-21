# Exchange_Course_Mapper
Using NLP techniques learned in CS4248 to determine similarity of courses between 2 exchange universities.

It displays the best 5 matches for each course based on the description of the course.

Dependencies:
- Sklearn
- Numpy
- Requests
## Guide
- Use the CourseGetters folder to extract course information into the JSON format with the following format:
  - ```[ [course_code, course_description], [course_code, course_description], [course_code, course_description], ... ]```
  - The model trains using the course description
- Copy the information to train on into the file `src/main/TRAIN`
- Modify the array in the `src/main/main.py`, following the same format as the example given in the program.
- Run the `main.py` file. I cannot get it to run from the terminal for some reason, so now I am using PyCharm to run it.

## Work(s) in Progress
- ~~I am currently confused by Python packages, and therefore the folder structure is not as nice at the moment. Once I get the hang of Python packages, the process will be more streamlined.~~ 
  - [ ] Move algorithms and models to a custom_utils package folder
  - [ ] Add a proper data folder
- ~~Getting it to run from the terminal. I still get the err: `from src.tf_idf_coursemappings.tf_idf_spare_cov import TfIdfMapper
ModuleNotFoundError: No module named 'src'`~~
  - [ ] Run from root directory if needed. Need to implement the command. 
  - [ ] Implement a simple GUI, that will be extendable to other features.
- ~~(Very low priority)~~ Adding other algorithms which I find interesting.
  - [ ] Explore similarity comparison using Deep Neural Networks, in particular RNNs, GRUs, LSTMs and Transformers.
  - [ ] Explore course recommendation chatbots, starting with Retrieval Augmented Generation (RAG).
  - [ ] Explore scraping reviews as well and answering them in the chatbots as well.

## Future Direction
The ultimate goal of this application is to find a course that is similar to what you want to learn.
This extends to finding similar courses between exchange universities.

The stretch goal would be to evaluate the different models and techniques of NLP, especially when there is a lot of research output on the subject matter.

The milestones are as follows:
1. Restructure the project:
   1. Move the models and utils into a package
   2. Implement skeleton GUI
   3. Allow program to run from command line
2. Use vector databases (to store vectors of the courses)
3. Implement an efficient algorithm for getting similar courses (using transformers against every course is not a good idea)
4. Implement a chatbot that recommends and evaluates courses using RAG.

## Caveats
- If the course description is vague, and there is no outline of the topics that is taught in the course, this program cannot match the course well.
