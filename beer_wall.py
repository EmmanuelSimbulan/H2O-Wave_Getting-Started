import time
from h2o_wave import site, ui

# Grab a reference to the page at route '/beer'
page = site['/beer']

# Making our program more efficient by using this markdown card content
beer_verse = '''={{before}} bottles of beer on the wall, {{before}} bottles of beer.

Take one down, pass it around, {{after}} bottles of beer on the wall...
'''

# Add a markdown card to the page.
beer_card = page.add('wall', ui.markdown_card(
    box='1 1 4 2',
    title='99 Bottles of Beer',
    content=beer_verse,                     # The verse of our content for markdown card
    data=dict(before='99', after='98'),     # We also set the card's data attribute to a Python dictionary, and add containing values for placeholders (before and after)
))

# Instead of updating the whole content of the card, we only need to update the values of the placeholders (.data.before and .data.after)
for i in range(99, 0, -1):
    beer_card.data.before = str(i)
    beer_card.data.after = str(i - 1)
    page.save()
    time.sleep(1)