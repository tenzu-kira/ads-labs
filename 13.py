import hashlib

def sha256_hash_function(word):
    sha256 = hashlib.sha256()
    sha256.update(word.encode('utf-8'))
    return int(sha256.hexdigest(), 16)

def create_hash_table(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    words = text.split()
    hash_table_size = len(words)
    hash_table = [None] * hash_table_size
    for word in words:
        hash_value = sha256_hash_function(word) % hash_table_size
        while hash_table[hash_value] is not None:
            hash_value = (hash_value + 1) % hash_table_size
        hash_table[hash_value] = word
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for index, word in enumerate(hash_table):
            if word is not None:
                result_file.write(f"{index}: {word}\n")

create_hash_table('input.txt', 'output13.txt')
