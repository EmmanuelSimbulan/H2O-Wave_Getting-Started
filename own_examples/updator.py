import time
from h2o_wave import site, ui

page = site['/updator']

time_left = '''=The remaining {{seconds}} seconds left is now being updated by the updator card.
'''

updator_card = page.add('updator', ui.markdown_card(
    box = '1 1 5 3',
    title = '30 seconds countdown',
    content = time_left,
    data = dict(seconds = '30'),
))

for i in range(30, 0, -1):
    updator_card.data.seconds = str(i)
    page.save()
    time.sleep(1)