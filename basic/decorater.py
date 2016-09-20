def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:' ,func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    
    return new_function

def add_ints(a,b):
    return a + b

print('*********************************************')
print(add_ints(3,5))

print('*********************************************')
add_ints2 = document_it(add_ints)
print(add_ints2(3,5))

print('*********************************************')
@document_it
def add_ints3(a,b):
    return a + b
print(add_ints3(3,5))