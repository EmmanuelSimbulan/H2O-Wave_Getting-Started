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

### Tutorial: System Monitor

### Tutorial: Bean Counter

### Tutorial: Todo List
