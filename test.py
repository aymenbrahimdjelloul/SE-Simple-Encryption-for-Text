from Scripts import SE, key_generator


text = 'aymen'
key = key_generator.generate_random_key()
print(key)

obj = SE.new(key)
print(obj.encrypt(text))