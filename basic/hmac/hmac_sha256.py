import hmac
import hashlib

key="secret"
text="foo bar"
signature=hmac.new(key,text,hashlib.sha256).hexdigest()
print signature
 
m=hmac.new(key,'',hashlib.sha256)
m.update("foo ")
m.update("bar")
signature=m.hexdigest()
print signature
 
key="secret2"
text="foo bar"
signature=hmac.new(key,text,hashlib.sha256).hexdigest()
print signature