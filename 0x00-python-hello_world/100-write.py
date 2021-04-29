#!/usr/bin/python3
save_file = open("examplefile.txt", 'r')
save_file_wc = open("examplefile_wc.txt", 'w')
for line in save_file:
    tokens = line.split('')
    save_file_wc.write(line + str(len(tokens)))
save_file.write(
    "and that piece of art is useful - Dora Korpar, 2015-10-19"'\n')
exit(0)
save_file.close()
save_file_wc.close()
