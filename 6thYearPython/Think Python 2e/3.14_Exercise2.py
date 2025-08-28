def do_twice(f,v):
    f(v)
    f(v)

def print_spam(val):
    print(val)

do_twice(print_spam,"HI!")

def print_twice(bruce):
    print(bruce)
    print(bruce)

do_twice(print_twice, "spam")

def do_four(func, value):
    do_twice(func, value)
    do_twice(func, value)

do_four(print_spam, "I am an egghead")