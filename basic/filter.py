routes = [{'method':'POST','path':'/user/001'},{'method':'GET','path':'/user/001'}]

method = 'post'
print(filter(lambda x: x['method'] == method.upper(),routes))
print(filter(lambda x: x,routes))

def check_method(routes,method):
    return routes['method'] == method.upper()

print(filter(lambda x: check_method(x,'post'),routes))