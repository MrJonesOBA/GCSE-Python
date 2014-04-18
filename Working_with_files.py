def read_file_to_list(my_list):
    file1 = open('file1.txt')
    for line in file1:
        my_list.append(line.split())
    file1.close()

    return my_list


def add_record(my_list):
    student_name = input('Enter student name:')
    score = input('Enter student score:')

    my_list.append([student_name, score])

    return my_list


def update_data(my_list):
    student_name = input('Enter student name:')
    score = input('Enter student score:')

    for i in my_list:
        if i[0] == student_name:
            i[1] = score

    return my_list


def write_data_to_file(my_list):
    file2 = open('file2.txt', 'w')
    for record in sorted(my_list):
        record = ' '.join(record)
        file2.write(record + '\n')

    return

