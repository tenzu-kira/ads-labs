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
    hash_table = [[] for _ in range(hash_table_size)]
    print(hash_table)
    for word in words:
        hash_value = sha256_hash_function(word) % hash_table_size
        hash_table[hash_value].append(word)
    with open(output_file, 'w', encoding='utf-8') as result_file:
        for index, words_list in enumerate(hash_table):
            if words_list:
                words = ', '.join(words_list)
                result_file.write(f"{index}: {words}\n")

create_hash_table('input.txt', 'output14.txt')

