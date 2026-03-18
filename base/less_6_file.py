# открыть файл для чтения
file = open(file="myfile.txt", mode="r", encoding="utf-8")
text = file.readlines(-1)
file.seek(0)
text_str = file.read()
file.close()
print(text)
print(text_str)


output_file = open("myfile_2.txt", mode="w", encoding="utf-8") # создать новый файл
text_to_write = "Hello World!" # создаем текст в файле
output_file.write(text_to_write)
file.close() # закрываем файл

