# Read File

# my_file = open('file_test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# print(my_file.readlines())

# my_file.close()

# with open('file_test.txt') as my_file:
#    print('no need to worry close the flie',my_file.readlines())



# Write text in the file

# with open('file_test.txt', mode='r+') as my_file:
#     text = my_file.write('I am writing text in the file.')
#     print(text)
    
#with open('file_test.txt', mode='a') as my_file:
#    text = my_file.write('I am writing text in the file.')
#    print(text)

   
#with open('file_test.txt', mode='w') as my_file:
#    text = my_file.write('I am writing text in the file.')
#    print(text)
    
    

# File IO Errors
  
#try: 
#    with open('not_exist.txt', mode='x') as my_file:
#        print(my_file.read())
#except FileNotFoundError as err:
#    print('file does not exist')
#    raise err
#except IOError as err:
#    print('IO error')
#    raise err



# Translate file

from translate import Translator

translator = Translator(to_lang="zh")
try: 
    with open('./translate_eng.txt', mode='r') as my_file:
        text = my_file.read()
        print(text)
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as err:
    print('file does not exist')
