import hashlib

inputs = str(input()).encode()
sha = hashlib.new("sha256")
sha.update(inputs)
print(sha.hexdigest())