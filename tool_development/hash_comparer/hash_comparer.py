import hashlib 

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('sha1')

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('sha1')

hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {file1} é diferente do arquivo {file2}')
else:
    print(f'O arquivo {file1} é igual ao arquivo {file2}')