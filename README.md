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

</details>
