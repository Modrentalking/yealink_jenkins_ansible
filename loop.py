def write_lines_to_file(filename):
    with open(filename, 'w') as file:
        for i in range(1, 61):
                    
                 
            
            label_name = f"linekey{i}label"
            value_name = f"linekey{i}value"
            label_default = f"${{params.{label_name} ?: '-'}}"
            value_default = f"${{params.{value_name} ?: '-'}}"
            label_description = f"linekey.{i}.label"
            value_description = f"linekey.{i}.value"

            label_line = f'string(name: "{label_name}", defaultValue: "{label_default}", description: "{label_description}")'
            value_line = f'string(name: "{value_name}", defaultValue: "{value_default}", description: "{value_description}")'

            file.write(label_line + '\n')
            file.write(value_line + '\n')

filename = 'output.txt'
write_lines_to_file(filename)
print('Строки успешно записаны в файл', filename)