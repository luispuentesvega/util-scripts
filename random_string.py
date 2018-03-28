import uuid

def get_random_string(string_length=10):
    random = str(uuid.uuid4()).replace('-','')
    return random[0:string_length]

print(get_random_string(10))