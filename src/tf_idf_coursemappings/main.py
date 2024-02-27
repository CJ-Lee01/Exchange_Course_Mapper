import json
from tf_idf_spare_cov import TfIdfMapper

if __name__ == '__main__':
    # for me to conveniently run on PyCharm
    pass

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
    ),
    (
        'CS2107',
        'This course serves as on information security. secure  and implementation. Topics covered include classical/historical ciphers, modern ciphers and cryptosystems, ethical, legal and organisational aspects, classic examples of direct attacks on computer systems such as input validation vulnerability, examples of other forms of attack such as social engineering/phishing attacks, and the practice of secure programming'
    ),
    (
        'CS3223',
        'This system-oriented course provides an in-depth study of the concepts and implementation issues related to database management systems. It first covers the physical implementation of the relational data model, which includes storage management, access methods, query processing, and optimisation. Then it covers issues and techniques dealing with multi-user application environments, namely, transactions, concurrency control, and recovery. The third part covers advanced topics such as on-line analytical processing, in-memory databases, and column stores'
    )

]

with open('../main/TRAIN', 'r') as trn_data:
    temp = json.loads(trn_data.read())
    training_set = [tuple(t) for t in temp]

mapper = TfIdfMapper()
mapper.train_modules(training_set)
mappings = mapper.get_course_mappings(test_set)

for course, course_maps in mappings:
    print(course)
    print('\t', course_maps)
