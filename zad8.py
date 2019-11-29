txt_file = open('zad8.txt', 'w+')
txt_file.writelines([str(number)+'\n' for number in range(1, 100)])

txt_file1 = open('zad8.txt', 'r')
print(txt_file1.read())

txt_file1.close()
txt_file.close()