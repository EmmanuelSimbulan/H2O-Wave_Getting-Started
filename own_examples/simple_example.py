# This is a simple example of how to use H2O Wave that is similar to hello_world.py

from h2o_wave import ui, site

page = site['/Sentence']

page['Sentence'] = ui.markdown_card(
    box = '1 2 5 2',
    title = 'This is a sentence',
    content = ' My name is *Emmanuel Robledo Simbulan*, and I am trying to learn how to use **H2O Wave.** </br> This is amazing, and I am eager to learn more.',
)

page.save()