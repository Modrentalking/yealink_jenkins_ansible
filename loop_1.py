def write_lines_to_file(filename):
    with open(filename, 'w') as file:
        for i in range(1, 61):
           
            label_name = f"paramsJson.linekey{i}label"
            value_name = f"paramsJson.linekey{i}value"
            label_value = f"params.linekey{i}label"
            value_value = f"paramsJson.linekey{i}value"

            label_line = f'{label_name} = {label_value}'
            value_line = f'{value_name} = {value_value}'

            file.write(label_line + '\n')
            file.write(value_line + '\n')

filename = 'params'
write_lines_to_file(filename)
print('Строки успешно записаны в файл', filename)