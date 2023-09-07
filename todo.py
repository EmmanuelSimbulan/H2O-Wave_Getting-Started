from typing import List
from h2o_wave import Q, main, app, ui

_id = 0


class TodoItem:
    def __init__(self, text):
        global _id
        _id += 1
        self.id = f'todo_{_id}'
        self.text = text
        self.done = False

@app('/todo', mode='multicast')
async def serve(q: Q):
    if q.args.new_todo:
        new_todo(q)
    elif q.args.add_todo:
        add_todo(q)
    elif q.args.clear_completed:  # Handle the "Clear" button click.
        clear_completed(q)  # Call the clear_completed function.
    else:
        show_todos(q)
    await q.page.save()

def show_todos(q: Q):
    todos: List[TodoItem] = q.user.todos

    if todos is None:
        q.user.todos = todos = [TodoItem('Do this'), TodoItem('Do that'), TodoItem('Do something else')]

    for todo in todos:
        if todo.id in q.args:
            todo.done = q.args[todo.id]

    done = [ui.checkbox(name=todo.id, label=todo.text, value=True, trigger=True) for todo in todos if todo.done]
    not_done = [ui.checkbox(name=todo.id, label=todo.text, trigger=True) for todo in todos if not todo.done]

    # Add a "Clear" button to the form.
    q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('To Do'),
        ui.button(name='new_todo', label='New To Do...', primary=True),
        *not_done,
        *([ui.separator('Done')] if len(done) else []),
        *done,
        ui.button(name='clear_completed', label='Clear Completed', primary=True),  # "Clear" button
    ])

def add_todo(q: Q):
    q.user.todos.insert(0, TodoItem(q.args.text or 'Untitled'))
    show_todos(q)

def new_todo(q: Q):
    q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('New To Do'),
        ui.textbox(name='text', label='What needs to be done?', multiline=True),
        ui.buttons([
            ui.button(name='add_todo', label='Add', primary=True),
            ui.button(name='show_todos', label='Back'),
        ]),
    ])

def clear_completed(q: Q):
    # Remove completed to-dos from the list.
    q.user.todos = [todo for todo in q.user.todos if not todo.done]
    show_todos(q)  # Show the updated to-do list.

if __name__ == '__main__':
    main()
