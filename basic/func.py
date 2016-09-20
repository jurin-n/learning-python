def sum_args(*args):
    return sum(args)

def run_with_positionnal_ars(func,*args):
    return func(*args)

print(run_with_positionnal_ars(sum_args,1,2,3,4))