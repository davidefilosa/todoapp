from functions import get_todos, write_todos
import time

now = time.strftime('%b %d, %Y %H:%M:%S')

print(f'Today is {now}')


while True:
    user_action = input('Type add, show, edit, complete, or exit: ').strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'
        todos = get_todos()
        todos.append(todo)
        write_todos(todos)
    elif 'show' in user_action:
        todos = get_todos()
        todos = [todo.strip('\n') for todo in todos]
        for index, todo in enumerate(todos):
            print(f'{index + 1}. {todo}')
    elif 'edit' in user_action:
        todos = get_todos()
        print('Here the list of existing todos: ', [(index+1, todo.strip()) for index, todo in enumerate(todos)])

        try:
            n = int(input('Which todo do you want to change? Enter the number: '))
            todos[n - 1] = ""
            todo = input('Enter a new todo: ') + '\n'
            todos[n - 1] = todo
        except ValueError:
            print('Your command was not valid. You should provide a number')
            continue
        except IndexError:
            print('Your command was not valid. There is not todo with this number')
            continue
        write_todos(todos)
    elif 'complete' in user_action:

        todos = get_todos()
        print('Here the list of existing todos: ', [(index+1, todo.strip()) for index, todo in enumerate(todos)])
        try:
            n = int(input('Which todo do you want to remove? Enter the number: '))
            todo_to_remove = todos[n-1]
            todos.pop(n-1)
        except ValueError:
            print('Your command was not valid. You should provide a number')
            continue
        except IndexError:
            print('Your command was not valid. There is not todo with this number')
            continue
        write_todos(todos)
        print(f'{todo_to_remove.strip()}  was removed!')

    elif 'exit' in user_action:
        break
    else:
        print('You entered an unknown command')

print('Bye!')
