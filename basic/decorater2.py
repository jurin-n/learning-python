def run(message):
    def callback(func):
        def new_run():
            print('print:', func , ',message=', message)
            func()
        return new_run
    return callback

@run('message at run!!')
def print_message():
    print('print_message!')

def run2(func):
    def new_run2():
        print('print:', func )
        func()
    return new_run2

@run2
def print_message2():
    print('print_message2!')

print('### call print_message() ###')
print_message()

print('### call print_message2() ###')
print_message2()