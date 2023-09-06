# H2O-Wave_Getting-Started

## H2O WAVE TASKS - GETTING STARTED:

**DIRECTIONS:**

Learn how to utilize H2O Wave with Python and your computer's terminal by following the step-by-step instructions outlined in the provided link (https://wave.h2o.ai/docs/getting-started). Our team leader at Lamina Studios recommends delving deeper into understanding how to create AI web apps using H2O Wave as an initial exercise. This foundational knowledge will serve as a valuable precursor to implementing the theory and practices needed for developing the web app for Thumbworx.

---

### Create the following exercises using Python in H20 Wave:

<details><summary><h3>Tutorial: Hello World</h3> </summary>

In this tutorial, we began by running H2O Wave in our terminal with the command "./waved." 

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/43e2acca-8ee1-4cd3-93e0-2cd718497681)

Next, we opened a new terminal session directly in our repository and set up a virtual environment (venv) using the commands "python3 -m venv venv" and "source venv/bin/activate." 

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/c6c521c5-8090-44a1-b3d6-763e39b1f615)

Moving forward, our next task involves creating a Python program named "hello_world.py" and executing it.

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/92fc5a29-c2c8-48a6-a698-b7f33998aaaa)

Upon execution, the following is the resulting program displayed on the local server of H2O Wave:

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/83e66efc-aa4e-4f67-b874-0c139bfb3c76)

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

![image](https://github.com/EmmanuelSimbulan/H2O-Wave_Getting-Started/assets/72858389/4efe09e6-bb37-43de-a44a-b76e5496c7c8)

</details>

### Tutorial: Beer Wall

### Tutorial: System Monitor

### Tutorial: Bean Counter

### Tutorial: Todo List
