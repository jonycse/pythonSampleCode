import uuid

print uuid.uuid1()
print "[Hex]",uuid.uuid1().hex
print uuid.uuid4()
print "[Hex]",uuid.uuid4().hex
print uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
print "[Hex]",uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org').hex
print uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
print "[Hex]",uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org').hex
