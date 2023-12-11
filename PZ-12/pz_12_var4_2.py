

def bukva_generator(s: str):
    for elem in s: 
        if elem.isalpha():
            yield elem
            


gen_obj = bukva_generator('a1s2d4345fvds')

print(next(iter(gen_obj)), end=' ')
print(next(iter(gen_obj)), end=' ')
print(next(iter(gen_obj)), end=' ')
print(next(iter(gen_obj)), end=' ')
print(next(iter(gen_obj)), end=' ')
print(next(iter(gen_obj)), end=' ')
print(next(iter(gen_obj)), end=' ')


#a s d f v d s 

