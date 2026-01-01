import tiktoken



encoder = tiktoken.encoding_for_model('gpt-4o')

text = "My name is debabrata Bar 33"

encoded = encoder.encode(text)
decoded = encoder.decode(encoded)


print(encoded)
print(decoded)