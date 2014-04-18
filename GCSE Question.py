# create an empty file
def create_file():
    file_name = input('\nEnter file name to create: ') + '.txt'
    scores_file = open(file_name, 'w')
    print("\nEmpty file '" + file_name + "' has been created.")
    scores_file.close()
    return file_name


# read from a file and populate a new list
def read_file_to_list():
    scores = []
    file_name = 'None'
    try:
        file_name = input('\nChoose file: ') + '.txt'
        score_file = open(file_name)
        for line in score_file:
            scores.append(line.split())
        score_file.close()
    except FileNotFoundError:
        print('File not found, it will be created.')
    return scores, file_name


# print current file
def print_file(scores, file_name):
    print()
    for record in scores:
        print('[' + record[0] + ' : ' + record[1] + ']')
    return

# write the current list to a file
def write_data_to_file(scores, file_name):
    try:
        score_file = open(file_name, 'w')
        for record in sorted(scores):
            record = ' '.join(record)
            score_file.write(record + '\n')
        score_file.close()
    except FileNotFoundError:
        print('File not found, it will be created.')
    return


# add data to the populated list and write to file
def add_data_to_list(scores, file_name):
    number_of_records = int(input('\nEnter number of records to add: '))
    for i in range(number_of_records):
        username = input('\nEnter username: ')
        score = input('Enter score: ')
        scores.append([username, score])
    write_data_to_file(scores, file_name)
    print('\n' + str(number_of_records) + ' records added to file: ' + file_name + '\n')
    return scores


# read a file, populate a list, search it and print record
def search_file(scores, file_name):
    print('\nSearch by student or score?\n\n1: Student\n2: Score\n')
    choice = input('\nChoose:')
    if choice == '1':
        student_name = input('\nEnter student name:')
        print()
        for record in scores:
            if record[0] == student_name:
                print(record[0] + ' scored ' + record[1])
    elif choice == '2':
        score = input('\nEnter student score:')
        print()
        for record in scores:
            if record[1] == score:
                print(record[0] + ' scored ' + record[1])
    return


# delete record from populated list and write to file
def delete_record_from_file(scores, file_name):
    student_name = input('\nEnter student to delete:')
    for record in scores:
        if record[0] == student_name:
            score = record[1]
            scores.remove(record)
    write_data_to_file(scores, file_name)
    print("\nRecord [" + student_name + ' : ' + str(score) + "] deleted from file: " + file_name)
    return


# update record in populated list and write to file
def update_record_in_file(scores, file_name):
    student_name = input('\nEnter student to update:')
    score = input('\nEnter new score:')
    for record in scores:
        if record[0] == student_name:
            record[1] = score
    write_data_to_file(scores, file_name)
    print("\n[" + student_name + ' : ' + str(score) + "] saved to file: " + file_name)
    return


# print options
def print_interface():
    print('\n1: Create a file')
    print('2: Add data to a file')
    print('3: Locate data in the file by name and their highest score')
    print('4: Delete an item and its associated data from the file')
    print('5: Locate and update a high score for a user')
    print('6: Show file contents')
    print('0: Exit')
    print('\n')
    return


# user makes selection
def choose_option():
    while True:
        print_interface()
        selection = int(input('Choose: '))
        if selection == 1:
            create_file()
        elif selection == 2:
            add_data_to_list(*read_file_to_list())
        elif selection == 3:
            search_file(*read_file_to_list())
        elif selection == 4:
            delete_record_from_file(*read_file_to_list())
        elif selection == 5:
            update_record_in_file(*read_file_to_list())
        elif selection == 6:
            print_file(*read_file_to_list())
        elif selection == 0:
            print('\nGoodbye')
            return


def main():
    choose_option()
    return

main()