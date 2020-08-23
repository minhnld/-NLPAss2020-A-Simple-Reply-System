"""
© 2020 Nguyen Linh Dang Minh aka Minh Ng
If there are any problems, contact me at minh.nldang@gmail.com or minh.nguyenlinhdang@hcmut.edu.vn 
"""
import sys

file_name=["output_a.txt",
           "output_b.txt",
           "output_c.txt",
           "output_d.txt",
           "output_e.txt"]

def write_file(question_number, content):
    file = open(file_name[question_number-1], 'w', encoding='utf-8')
    file.write(content)
    file.close()
