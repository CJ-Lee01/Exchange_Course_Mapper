# Implementation

Currently, a modified version of tf-idf is used to implement the checker.

This is due to some special attributes of the data
1. Additional words on top of stop words should be removed, such as 'course', 
which does not contribute meaning to the details.
2. The names of the key topics are probably only mentioned once in the details.

For point 1, it would be easy to cut off words that appear across the majority of the details of the courses.

For point 2, rather than using the conventional count, 
the log count is used in order to reduce the weights of higher frequency terms with the details
and give more weight to the more important lower frequency terms.