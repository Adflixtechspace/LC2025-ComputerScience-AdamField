words = {"henry": 7, "pistacchio": 3, "larry": 5}

print(words["henry"])

words["henry"] = 101

print(words)

giraffe = words

giraffe["henry"], giraffe["pistacchio"], giraffe["larry"] = 99, 77, False

print(giraffe)

words["mick"] = "one-hundred and twenty-three"

print(words)