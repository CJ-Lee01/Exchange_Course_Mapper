from src.tf_idf_coursemappings.tf_idf_spare_cov import TfIdfMapper

if __name__ == '__main__':
    pass

training_set = [
    (
        'CS2109S',
        'This course introduces basic concepts in Artificial Intelligence (AI) and Machine Learning (ML). It adopts the perspective that planning, games, and learning are related types of search problems, and examines the underlying issues, challenges and techniques. Planning/games related topics include tree/graph search, A* search, local search, and adversarial search (e.g., games). Learning related topics include supervised and unsupervised learning, model validation, and neural networks.'
    ),
    (
        'CS4248',
        'This course deals with computer processing of human languages, including the use of neural networks and deep learning in natural language processing. The topics covered include: regular expressions, words and edit distance, n-grams, part-of-speech tagging, feed-forward neural networks, neural network training, word embedding, convolutional neural networks, recurrent neural networks, sequence-to-sequence models with attention, transformers, context-free grammars, syntactic parsing, semantics, and discourse.'
    ),
    (
        'CS3264',
        'This course covers the fundamental concepts, theory, and algorithms in machine learning, and a variety of modeling techniques to extract information from raw data. The class will cover topics in both supervised and unsupervised learning, including problems in classification and regression, computational learning theory, reinforcement learning, probabilistic inference, ensemble learning, and more advanced topics. The class will cover both the underlying mathematical tools, as well as practical frameworks for solving real-world problems. At the end of the course, students are expected to be familiar with the theories and paradigms of computational learning, and capable of implementing basic learning systems.'
    ),
    (
        'CS1231S',
        'This course introduces mathematical tools required in the study of computer science. Topics include: (1) Logic and proof techniques: propositions, conditionals, quantifications. (2) Relations and Functions: Equivalence relations and partitions. Partially ordered sets. Well-Ordering Principle. Function equality. Boolean/identity/inverse functions. Bijection. (3) Mathematical formulation of data models (linear model, trees, graphs). (4) Counting and Combinatoric: Pigeonhole Principle. Inclusion-Exclusion Principle. Number of relations on a set, number of injections from one finite set to another, Diagonalization proof: An infinite countable set has an uncountable power set; Algorithmic proof: An infinite set has a countably infinite subset. Subsets of countable sets are countable.'
    )
]

test_set = [
    (
        'CS3243',
        "The course introduces the basic concepts in search and knowledge representation as well as to a number of sub-areas of artificial intelligence. It focuses on covering the essential concepts in AI. The course covers Turing test, blind search, iterative deepening, production systems, heuristic search, A* algorithm, minimax and alpha-beta procedures, predicate and first-order logic, resolution refutation, non-monotonic reasoning, assumption-based truth maintenance systems, inheritance hierarchies, the frame problem, certainly factors, Bayes' rule, frames and semantic nets, planning, learning, natural language, vision, and expert systems and LISP."
    ),
]

mapper = TfIdfMapper()
mapper.train_modules(training_set)
print('training set')
print(mapper.course_vector)
print('test set')
