import json
from tf_idf_spare_cov import TfIdfMapper

test_set = [
    (
        'CS3230',
        "This course introduces different techniques of designing and analysing algorithms. Students will learn about the framework for algorithm analysis, for example, lower bound arguments, average case analysis, and the theory of NP-completeness. In addition, students are exposed to various algorithm design paradigms. The course serves two purposes: to improve the students' ability to design algorithms in different areas, and to prepare students for the study of more advanced algorithms. The course covers lower and upper bounds, recurrences, basic algorithm paradigms (such as prune-and-search, dynamic programming, branch-and-bound, graph traversal, and randomised approaches), amortized analysis, NP-completeness, and some selected advanced topics."
    ),
    (
        'CS2106',
        'This course introduces the basic concepts in operating systems and links it with contemporary operating systems (eg. Unix/Linux and Windows). It focuses on OS structuring and architecture, processes, memory management, concurrency and file systems. Topics include kernel architecture, system calls, interrupts, models of processes, process abstraction and services, scheduling, review of physical memory and memory management hardware, kernel memory management, virtual memory and paging, caches, working set, deadlock, mutual exclusion, synchronisation mechanisms, data and metadata in file systems, directories and structure, file system abstraction and operations, OS protection mechanisms, and user authentication'
    ),
    (
        'CS3264',
        'This course covers the fundamental concepts, theory, and algorithms in machine learning, and a variety of modeling techniques to extract information from raw data. The class will cover topics in both supervised and unsupervised learning, including problems in classification and regression, computational learning theory, reinforcement learning, probabilistic inference, ensemble learning, and more advanced topics. The class will cover both the underlying mathematical tools, as well as practical frameworks for solving real-world problems. At the end of the course, students are expected to be familiar with the theories and paradigms of computational learning, and capable of implementing basic learning systems'
    ),
    (
        'CS4243',
        'This course is for undergraduates who are interested in computer vision and its applications. It covers (a) the basic skills needed in handling images and videos, (b) the basic theories needed to understand geometrical computer vision, and (c) pattern recognition. Topics covered in image handling include: contrast stretch, histogram equalization, noise removal, and color space. Topics covered in geometrical vision include: affine transform, vanishing points, camera projection models, homography, camera calibration, rotation representations including quaternions, epipolar geometry, binocular stereo, structure from motion. Topics covered for pattern recognition include principal component analysis'
    )

]

with open('TRAIN', 'r') as trn_data:
    temp = json.loads(trn_data.read())
    training_set = [tuple(t) for t in temp]

mapper = TfIdfMapper()
mapper.train_modules(training_set)
mappings = mapper.get_course_mappings(test_set)

for course, course_maps in mappings:
    print(course)
    print('\t', course_maps)
