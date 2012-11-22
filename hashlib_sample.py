import hashlib

message = "python"

print "md5"
print hashlib.md5(message).hexdigest()

print "sha1"
print hashlib.sha1(message).hexdigest()

print "sha512"
print hashlib.sha512(message).hexdigest()

print "sha224"
print hashlib.sha224(message).hexdigest()

print "sha256"
print hashlib.sha256(message).hexdigest()

print "sha384"
print hashlib.sha384(message).hexdigest()