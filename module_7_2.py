import io


def custom_write(file_name, strings: list):
    string_position = {}
    line = 1
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        string_position[line, file.tell()] = i
        file.write(i + '\n')
        line += 1
        file.close()

    return string_position.items()



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
print(result)
for elem in result:
    print(elem)
