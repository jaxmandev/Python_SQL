import pypyodbc
from sql_movies import Crud

def main():
    print('Available Options: C=Create, R=Read, U=Update, D=Delete ')
    choice = input('Choose your option = ')
    action = Crud()
    while True:
        if choice == 'C':
            action.create_table()
        elif choice == 'R':
            action.read_table()
        elif choice == 'U':
            action.update_table()
        elif choice == 'D':
            action.delete_table()
        else:
            print('Wrong choice.')

# call the main function
main()