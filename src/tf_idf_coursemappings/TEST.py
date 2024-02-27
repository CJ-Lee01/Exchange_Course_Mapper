from tf_idf_spare_cov import TfIdfMapper

training_set = [
    (
        'CS3230',
        "This course introduces different techniques of designing and analysing algorithms. Students will learn about the framework for algorithm analysis, for example, lower bound arguments, average case analysis, and the theory of NP-completeness. In addition, students are exposed to various algorithm design paradigms. The course serves two purposes: to improve the students' ability to design algorithms in different areas, and to prepare students for the study of more advanced algorithms. The course covers lower and upper bounds, recurrences, basic algorithm paradigms (such as prune-and-search, dynamic programming, branch-and-bound, graph traversal, and randomised approaches), amortized analysis, NP-completeness, and some selected advanced topics."
    ),
    (
        'CS2106',
        'This course introduces the basic concepts in operating systems and links it with contemporary operating systems (eg. Unix/Linux and Windows). It focuses on OS structuring and architecture, processes, memory management, concurrency and file systems. Topics include kernel architecture, system calls, interrupts, models of processes, process abstraction and services, scheduling, review of physical memory and memory management hardware, kernel memory management, virtual memory and paging, caches, working set, deadlock, mutual exclusion, synchronisation mechanisms, data and metadata in file systems, directories and structure, file system abstraction and operations, OS protection mechanisms, and user authentication'
    ),

]

test_set = [
    (
        'CS3243',
        "The course introduces the basic concepts in search and knowledge representation as well as to a number of sub-areas of artificial intelligence. It focuses on covering the essential concepts in AI. The course covers Turing test, blind search, iterative deepening, production systems, heuristic search, A* algorithm, minimax and alpha-beta procedures, predicate and first-order logic, resolution refutation, non-monotonic reasoning, assumption-based truth maintenance systems, inheritance hierarchies, the frame problem, certainly factors, Bayes' rule, frames and semantic nets, planning, learning, natural language, vision, and expert systems and LISP."
    ),
    (
        'CS3244',
        'This course introduces basic concepts and algorithms in machine learning and neural networks. The main reason for studying computational learning is to make better use of powerful computers to learn knowledge (or regularities) from the raw data. The ultimate objective is to build self-learning systems to relieve human from some of already-too-many programming tasks. At the end of the course, students are expected to be familiar with the theories and paradigms of computational learning, and capable of implementing basic learning systems.'
    ),
    (
        'MA1100',
        'This is the entry-level course for a sound education in modern mathematics, to prepare students for higher level mathematics courses. The first goal is to build the necessary mathematical foundation by introducing the basic language, concepts, and methods of contemporary mathematics, with focus on discrete and algebraic notions. The second goal is to develop student’s ability to construct rigorous arguments and formal proofs based on logical reasoning. Main topics: logic, sets, maps, equivalence relations, natural numbers, integers, rational numbers, congruences, counting and cardinality. Major results include: binomial theorem, fundamental theorem of arithmetic, infinitude of primes, Chinese remainder theorem, Fermat-Euler theorem.'
    ),
    (
        'YSC2209',
        'Mathematicians and computer scientists write proofs: convincing arguments, combining clear and concise language, computations and symbolic manipulation, illustrations and tables. By reading, writing, and revising proofs, students will be prepared for modern topics in analysis, algebra, geometry, and theoretical computer science. Students will write proofs that utilize direct deduction and proof by contradiction, complicated logical structures with cases, and mathematical induction. Students will acquire a thorough knowledge of naïve set theory, including sets and functions, equivalence relations and classes, cardinal and ordinal arithmetic. Topics in discrete mathematics will include the combinatorics of finite structures such as graphs and trees.'
    ),
    (
        'CS2040C',
        'This course introduces students to the design and implementation of fundamental data structures and algorithms. The course covers basic data structures (linked lists, stacks, queues, hash tables, binary heaps, trees, and graphs), searching and sorting algorithms, basic analysis of algorithms, and basic object-oriented programming concepts'
    ),
    (
        'CS 466',
        'Algorithmic approaches and methods of assessment that reflect a broad spectrum of criteria, including randomized algorithms, amortized analysis, lower bounds, approximation algorithms, and on-line algorithms. Particular examples will be chosen from different areas of active research and application'
    )
]

mapper = TfIdfMapper()
mapper.train_modules(training_set)
print(mapper.get_course_mappings(test_set))
