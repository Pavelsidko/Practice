def format_text(input_text):
    # Удаляем начальные и конечные пробелы
    formatted_text = input_text.strip()

    # Заменяем множественные пробелы на один
    formatted_text = ' '.join(formatted_text.split())

    # Переносим точки и запятые к предыдущему слову
    punctuation_marks = [',', '.']
    for mark in punctuation_marks:
        formatted_text = formatted_text.replace(' ' + mark, mark)

    return formatted_text


input_text = input().strip()
output_text = format_text(input_text)
print(output_text)