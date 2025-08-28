from random import *

articles =["the", "a", "one", "some", "any"]
nouns =["teacher", "student", "pricipal", "library", "school"]
verbs =["taught", "learned", "read", "walked", "ran"]
prepositions = choice(["to", "from", "over", "under", "on"])

article1 = choice(articles)
article2 = choice(articles)
noun1 = choice(nouns)
noun2 = choice(nouns)
verb1 = choice(verbs)
verb2 = choice(verbs)

print(article1, noun1, verb1, article2, noun2, prepositions, verb2)