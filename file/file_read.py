# -*- coding: utf-8 -*-
__author__ = 'zhangyunrui'

# all_the_text = open('thefile.txt').read()
# all_the_data = open('abinfile', 'rb').read()
#
#
# print all_the_text
# print all_the_data

# file_object = open('thefile.txt')
# try:
#     # all_the_text = file_object.read()
#     # print all_the_text
#     # list_of_all_lines = file_object.readlines()
#     # print list_of_all_lines
#     # list_of_all_lines = file_object.read().splitlines()
#     # print list_of_all_lines
#     # list_of_all_lines = file_object.read().split('\n')
#     # print list_of_all_lines
#     list_of_all_lines = [L.rstrip('\n') for L in file_object]
#     print list_of_all_lines
# finally:
#     file_object.close()

# file_object = open('abinfile', 'rb')
# try:
#     while True:
#         chunk = file_object.read(5)
#         if not chunk:
#             break
#         print chunk
# finally:
#     file_object.close()

# def read_file_by_chuncks(filename, chuncksize=100):
#     file_object = open(filename, 'rb')
#     while True:
#         chunk = file_object.read(chuncksize)
#         if not chunk:
#             break
#         yield chunk
#     file_object.close()
#
# for chunk in read_file_by_chuncks('abinfile', 10):
#     print chunk


file_object = open('thefile.txt', 'rU')
try:
    for line in file_object:
        print line
finally:
    file_object.close()


