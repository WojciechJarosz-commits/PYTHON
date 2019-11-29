txt_file = open('zad8.txt', 'w+')
txt_file.writelines([str(number)+'\n' for number in range(1, 200)])

txt_file.seek(0)
print(txt_file.read())
txt_file.close()
