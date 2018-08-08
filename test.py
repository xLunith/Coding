class test:
    dict = {'a': 1, 'b': 4}

test1 = test()
test1.dict['a'] = 2
test2 = test()

print(test1.dict)
print(test2.dict)
