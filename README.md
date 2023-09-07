# H2O-Wave_Getting-Started

## H2O WAVE TASKS - GETTING STARTED:

**DIRECTIONS:**

Learn how to utilize H2O Wave with Python and your computer's terminal by following the step-by-step instructions outlined in the provided link (https://wave.h2o.ai/docs/getting-started). Our team leader at Lamina Studios recommends delving deeper into understanding how to create AI web apps using H2O Wave as an initial exercise. This foundational knowledge will serve as a valuable precursor to implementing the theory and practices needed for developing the web app for Thumbworx.

---

### Create the following exercises using Python in H20 Wave:

<details><summary><h3>Tutorial: Hello World</h3> </summary>

In this tutorial, we began by running H2O Wave in our terminal with the command "./waved." 

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/64a756a3-b81a-4366-b7cf-c9d3bd232af0)

Next, we opened a new terminal session directly in our repository and set up a virtual environment (venv) using the commands "python3 -m venv venv" and "source venv/bin/activate." 

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/81f3c0a1-84dc-4fb8-bf4b-b38708af5df2)

Moving forward, our next task involves creating a Python program named "hello_world.py" and executing it.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/343fa3bf-11df-4108-8fd4-d6b14196b200)

Upon execution, the following is the resulting program displayed on the local server of H2O Wave:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/48079bfc-f57e-4372-874c-6f12aa8105dd)

Following that, we attempted to make some alterations using the terminal. This is where H2O Wave shines; it seamlessly updates content in real-time. Simply execute the following commands in your terminal: "cd $HOME/wave-apps" and "./venv/bin/python." Here's an illustrative example:

```python
**Grab a reference to our page**
>>>
from h2o_wave import site
page = site['/hello']

**Grab a reference to our card**
>>>
quote = page['quote']

**Change the title**
>>>
quote.title = 'Hello Again!'
page.save()

**Change the content**
>>>
quote.content = "I hate my layf as a programmer!"
page.save()
```

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/3b7d9573-869f-47df-b37a-374f295e867a)

</details>

<details><summary><h3>Tutorial: Beer Wall</h3> </summary>

In our upcoming tutorial, we will delve into the practical application of H2O Wave to enhance our comprehension, specifically focusing on real-time information dissemination. In this project, our aim is to create a verse generator for the iconic mid-20th century chart-topper, "99 Bottles of Beer.”

[Watch the Sample Video](https://wave.h2o.ai/assets/medias/tutorial-beer__demo-cb829b4b335d0d619fa4ce4ff0a516bf.mp4)

To start, we'll create a new Python program called "beer_wall.py." This program is akin to the Hello World Tutorial, with one notable exception: it involves the addition and configuration of content for a markdown card within a for loop.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/b3c06c1b-04eb-46b4-83c9-21779b97cff4)

Subsequently, we attempted to execute it in the terminal using the " /beer" domain.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/db305061-24f9-4044-b210-aa52cfecfeda)

Our program appears to be reasonably accurate but lacks efficiency. Upon examination, we observe that it consistently transmits the entire verse to the Wave server, even when only minor changes (i and i-1) are involved.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/27f57fef-2b16-4e6f-b5b3-d2ef921e9818)

To address this issue efficiently, we'll craft a program that initially sends the verse with placeholders for both "i" and "i-1." Subsequent updates will transmit only "i" and "i-1," reducing network traffic and easing the server's load during updates.

To achieve this, we'll create a markdown card and populate it with the desired content. We'll then embed this content within an expression or formula. Additionally, we'll establish a markdown card for utilizing the verse content. Crucially, we'll store this card in a data attribute, which will be a Python dictionary containing the placeholders for "before" and "after."

Rather than refreshing the entire verse with each update, we'll focus on updating the ".data.before" and ".data.after" attributes of the markdown card, thus optimizing the process.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/8df9b0e4-a1ca-4794-ac69-3d2357beec96)

Run your program again. You should see the same results in your browser as before, but you'll notice that the information flowing through the Wave server is significantly less than before:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/35cd31f7-d61c-42a8-981c-d8fe87a07412)

</details>

<details><summary><h3>Tutorial: System Monitor</h3> </summary>

Prior to diving into code development, our initial step involves the installation of essential dependencies via the terminal. We'll execute the command "pip install psutil" to procure the indispensable 'psutil' package, enabling us to access and process system statistics seamlessly.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/ea5a4ab9-1350-483a-916e-9d00765d34d0)


Next, we endeavored to craft a program tasked with vigilant system monitoring for our device, specifically targeting CPU usage.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/feb67ba0-e5d9-456a-bddf-dd56c2cec04c)

Now, let's attempt to execute our program in the terminal.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/b0d205e7-0fa8-4b8d-9663-18aa2eb2ba7b)

Point your browser to http://localhost:10101/monitor. Here's the result on the webpage server:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/164f86a3-f0bd-43e3-80b6-e9f317f6461b)

After that, we will add another code block to our program to monitor memory usage. In this step, we will simply duplicate the parts of our program to create another card that displays memory statistics.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/f11c9c77-8ca7-4f0f-9914-6b20a01d0d97)

Now, let's attempt to execute our program. We'll save our code and then terminate the program before restarting it.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/5f716242-53e2-45b2-90fb-dc5d55bb45d5)

Here are the updated results for our webpage:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/c4e1e8dc-5d81-437c-87f3-ec3f1845eb51)

</details>

<details><summary><h3>Tutorial: Bean Counter</h3> </summary>

In this tutorial, we will create an interactive application using H2O Wave, which enables user interfaces to dynamically respond to events, such as user actions.

The initial step in crafting this program, which will be actively listening to events from the UI, is to define an `@app` function. Now, let's proceed to write our program:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/ff957df3-5d54-4707-bec1-0b937ffdb8d4)


Now, let's attempt to execute our program within our activated virtual environment. Simply type 'wave run counter'.

At this point, the app will be running, but it hasn't implemented any functionality yet.

To accomplish this task, we need to incorporate a button into our application. Our primary goal is to create a button that increments and displays the bean count every time it's clicked.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/a68280f2-a1d8-4509-8782-1342dea6d9e9)


Additionally, observe the disparity in the script between the current Wave Script and the previous Wave App script.

| Task | Wave Script | Wave App |
| --- | --- | --- |
| Access page at route /foo | page = site['/foo'] | page = q.page |
| Access card named foo | card = page['foo'] | card = q.page['foo'] |
| Save page | page.save() | await q.page.save() |

"In the Wave app, we consistently access pages using the query context 'q'. `q.page` consistently refers to the page located at the route specified in `@app()` (in this instance).

Now, let's proceed to launch our application, directing our browser to [http://localhost:10101/counter."](http://localhost:10101/counter.%22)

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/39bfa25c-c839-4f84-8e4a-ab2c4ffa56e6)


It's evident that clicking the button has no effect because we haven't implemented the button click handling yet. To resolve this, we'll handle button clicks by adding a condition to check if the button has been clicked. If it has, the bean count will be incremented.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/39ae69dc-5541-4a49-9d5a-53f1c1e0bf7c)


The button should now function correctly.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/b11b2475-28f5-4ac5-a42d-f14a80fedf65)


Now, let's endeavor to optimize our application's performance. Currently, with every button click, it redundantly recreates both the form card and the button, instead of efficiently updating the existing button's caption to reflect the current bean count.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/b00092fc-715c-44f5-ac9e-4330f1b0a92a)


Now to make our app more interesting let’s take a look about how `q.client` stores arbitrary information associated with the client, `q.user` and `q.app` store arbitrary information associated with the user and the app, respectively.

In most apps, you'll end up using a mix of `q.client`, `q.user` and `q.app` to correctly handle requests originating from:

1. Different users.
2. Different browser tabs belonging to the same user (possibly from different devices).
3. The same browser tab.

In other words, your Wave app is multi-user by default, but how the app manages data at the app-level, at the user-level and at the client-level is up to you.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/a591d57c-94fe-4407-aab1-ae084e2ef757)


Now, let's execute our program. You will observe that both pages and both cards update simultaneously when opening two distinct web pages.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/2e7a3db1-e366-4540-88a5-d67a94e6e81d)


As real-time synchronization is not feasible, we'll incorporate an 'app mode' into our code to facilitate real-time synchronization among clients.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/47bc859a-6731-49f8-9e15-62d72d9b0070)


The default app mode is `unicast`, which means "don't sync across clients". On the other hand, `multicast` means "sync across clients". 

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/b8cc564d-f455-4929-90d9-4ab089847cd2)


There's also a third mode, `broadcast`, which means "sync across users", which we'll see in the next step.

In order to do that we’re going to make an App-level realtime sync which going from user-level bean counting to app-level bean counting is easy: simply store `bean_count` on `q.app` instead of `q.user`, and switch the app mode to `broadcast`:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/118181a0-2c25-42a1-984e-0ab459f305f4)


The `broadcast` mode can be used to build collaborative apps that need to synchronize state across all users, like group chat or multiplayer games.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/3d224462-f075-4762-ae71-f4ad53a8efea)


## Summary[](https://wave.h2o.ai/docs/tutorial-counter#summary)

In this tutorial, we learned how to author interactive applications, or *apps*, and easily add realtime sync capabilities to our apps. More importantly, we learned how to deal with events and manage state using four dictionary-like objects:

| Attribute | Type | Use |
| --- | --- | --- |
| q.args | Read-only | Stores command arguments |
| q.client | Read/Write | Stores client-level state |
| q.user | Read/Write | Stores user-level state |
| q.app | Read/Write | Stores app-level state |

Also, we built ourselves a little app that counts beans, and you can now put that knowledge to good use, like build an online voting app.

</details>

<details><summary><h3>Tutorial: Todo List</h3> </summary>

In this tutorial, we will now craft a program of greater substance and utility—a real-time synchronized to-do list.

Let's start by creating the initial skeleton of our code. The first step is to define an `@app` function. Additionally, we want to set up a landing page to display a list of to-dos. To achieve this, we will create a `show_todos()` function for now and call it from `serve()`.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/a7d69048-48ac-4645-babd-3074464ac1b1)


A to-do item has some basic attributes: an ID, some text content, and whether it's completed or not. Let's define a `class` for that, with a global one-up `id`.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/0246f59e-cef1-4b86-adbf-8c63ff2544ce)


Next, we'll create a to-do list in 'q.user' mode. We're doing this because we want to generate a list from 'q.user' or create one if it doesn't already exist.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/39d85934-623f-485b-ba2c-856bc01b0d0e)


Next, we turn each incomplete to-do item into a checkbox (using `ui.checkbox()`), and display it in a form card (using `ui.form_card()`). Also, we want each checkbox to raise an event immediately when checked, so we set its `trigger` attribute to `True`.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/b0bf8aff-9282-477d-9873-bfc0fe80dc96)


We also turn each completed to-do item into another list of checkboxes, checked by default (using its `value` attribute). We append this to the form card and put a separator in between (using `ui.separator()`) to distinguish the completed items from the incomplete ones.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/e0867271-6844-4cea-a4e7-cc6437785ee9)


Point your browser to http://localhost:10101/todo.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/3f2c90e2-573a-46b2-9b4f-24d972060eb9)


You should be able to see your todo list in all its glory. Unfortunately, checking any of the items seems to have no effect. Let's fix that next.

Each time a checkbox is checked or unchecked, our `serve()` function is called, which in turn calls `show_todos()`.

- If a checkbox is checked, `q.args` will contain a `True` for that checkbox.
- If a checkbox is unchecked, `q.args` will contain a `False` for that checkbox.

So, we iterate through all the to-do items and set their `done` attribute based on the value of their corresponding checkbox.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/15779475-a975-44de-a4ef-186db8bfbfa1)


You should now be able to check/uncheck the items in your todo list.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/e869886a-b47f-4153-b675-cf6ea2530812)


Next, let's display a form to add new items to our list. For that, we'll add a new button to our existing form, named `new_todo`, and direct the `serve()` function to the `new_todo()` function if the button is clicked. Recall that when buttons are clicked, `q.args.button_name` will be `True`, so we check if `q.args.new_todo` is `True`.

In the `new_todo()` function, we display a new form containing a textbox (using `ui.textbox()`) and a set of buttons to add the item or return to to-do list (a `ui.buttons()` helps us display buttons side-by-side).

```python
from typing import List                 # We've added a new import statement for the List type
from h2o_wave import Q, main, app, ui

_id = 0

# A simple class that represents a to-do item.
class TodoItem:
    def __init__(self, text):
        global _id
        _id += 1
        self.id = f'todo_{_id}'
        self.text = text
        self.done = False

@app('/todo')           # We've added a route called /todo
async def serve(q: Q):  # We've added a function called serve() that will be called when the user interacts with the app
    if q.args.new_todo:  # Display an input form.
        new_todo(q)
    else:  # Show all items.
        show_todos(q)   # We've added a function called show_todos() that will be the landing page of our app  
    await q.page.save()

def show_todos(q: Q):
    # Get items for this user.
    todos: List[TodoItem] = q.user.todos

    # Create a sample list if we don't have any.
    if todos is None:
        q.user.todos = todos = [TodoItem('Do this'), TodoItem('Do that'), TodoItem('Do something else')]

    # If the user checked/unchecked an item, update our list.
    for todo in todos:
        if todo.id in q.args:
            todo.done = q.args[todo.id]

 # Create done/not-done checkboxes.
    done = [ui.checkbox(name=todo.id, label=todo.text, value=True, trigger=True) for todo in todos if todo.done]
    not_done = [ui.checkbox(name=todo.id, label=todo.text, trigger=True) for todo in todos if not todo.done]

    # Display list
    q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('To Do'),
        ui.button(name='new_todo', label='New To Do...', primary=True),
        *not_done,
        *([ui.separator('Done')] if len(done) else []),
        *done,
    ])

    def new_todo(q: Q):
    # Display an input form
    q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('New To Do'),
        ui.textbox(name='text', label='What needs to be done?', multiline=True),
        ui.buttons([
            ui.button(name='add_todo', label='Add', primary=True),
            ui.button(name='show_todos', label='Back'),
        ]),
    ])
```

You should now be able to bring up the new to-do form.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/4849e971-3b5b-4503-8e60-d753a89523ff)


Finally, we handle the `add_todo` button-click, redirecting `serve()` to a new `add_todo()` function, which simply inserts a the new to-do item into our user-level todo list and calls `show_todos()` to redraw the to-do list.

```python
from typing import List                 # We've added a new import statement for the List type
from h2o_wave import Q, main, app, ui

_id = 0

# A simple class that represents a to-do item.
class TodoItem:
    def __init__(self, text):
        global _id
        _id += 1
        self.id = f'todo_{_id}'
        self.text = text
        self.done = False

@app('/todo')           # We've added a route called /todo
async def serve(q: Q):  # We've added a function called serve() that will be called when the user interacts with the app
    if q.args.new_todo:  # Display an input form.
        new_todo(q)
    elif q.args.add_todo:  # Add an item.
        add_todo(q)
    else:  # Show all items.
        show_todos(q)   # We've added a function called show_todos() that will be the landing page of our app  
    await q.page.save()

def show_todos(q: Q):
    # Get items for this user.
    todos: List[TodoItem] = q.user.todos

    # Create a sample list if we don't have any.
    if todos is None:
        q.user.todos = todos = [TodoItem('Do this'), TodoItem('Do that'), TodoItem('Do something else')]

    # If the user checked/unchecked an item, update our list.
    for todo in todos:
        if todo.id in q.args:
            todo.done = q.args[todo.id]

 # Create done/not-done checkboxes.
    done = [ui.checkbox(name=todo.id, label=todo.text, value=True, trigger=True) for todo in todos if todo.done]
    not_done = [ui.checkbox(name=todo.id, label=todo.text, trigger=True) for todo in todos if not todo.done]

    # Display list
    q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('To Do'),
        ui.button(name='new_todo', label='New To Do...', primary=True),
        *not_done,
        *([ui.separator('Done')] if len(done) else []),
        *done,
    ])

def add_todo(q: Q):
    # Insert a new item
    q.user.todos.insert(0, TodoItem(q.args.text or 'Untitled'))

    # Go back to our list.
    show_todos(q)

def new_todo(q: Q):
    # Display an input form
        q.page['form'] = ui.form_card(box='1 1 3 10', items=[
        ui.text_l('New To Do'),
        ui.textbox(name='text', label='What needs to be done?', multiline=True),
        ui.buttons([
            ui.button(name='add_todo', label='Add', primary=True),
            ui.button(name='show_todos', label='Back'),
        ]),
    ])
```

You should now be able to add new to-do items to your list. Congratulations!

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/2c22cd8d-196b-4a29-908c-d4b2be465f8f)


To make your app realtime, simply pass `mode='multicast'` to `@app()`.

```python
@app('/todo', mode = 'multicast')
```

Now try opening http://localhost:10101/todo from multiple browser tabs:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/e09b514d-8d12-44fe-9f70-c9f0183f1d84)

## Exercise[](https://wave.h2o.ai/docs/tutorial-todo#exercise)

A little housekeeping goes a long way: add a "Clear" button on the main page to clear all completed to-dos.

To add a "Clear" button on the main page to clear all completed to-dos, you can make the following modifications to your code:

1. Define a new function called `clear_completed` to handle the clearing of completed to-dos.
2. Add a "Clear" button to the `show_todos` function's form.
3. Handle the "Clear" button click in the `serve` function.

Here's the updated code:

```python
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

```

With these modifications, you've added a "Clear Completed" button that will clear all completed to-dos when clicked.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/f8b4b165-70bf-42d3-8a8e-765d0fe7525c)

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/83953080-2eed-4420-891a-1661168f4a24)


</details>
