import hashlib

string = input('Digite o texto: ')

menu = int(input(''' #### ESCOLHA O TIPO DE HASH #### 
                  1) md5
                  1) sha1
                  3) sha256
                  4) sha512
                  Digite o número do hash a ser gerado: '''))

if menu == 1:
  result = hashlib.md5(string.encode('utf-8')).hexdigest()
  print (f'O hash MD5 da string é {result}')
elif menu == 2:
  result = hashlib.sha1(string.encode('utf-8')).hexdigest()
  print (f'O hash SHA1 da string é {result}')
elif menu == 3:
  result = hashlib.sha256(string.encode('utf-8')).hexdigest()
  print (f'O hash SHA256 da string é {result}')
elif menu == 4:
  result = hashlib.sha512(string.encode('utf-8')).hexdigest()
  print (f'O hash SHA512 da string é {result}')
else:
  print('Algo deu errado')