from h2o_wave import site, ui

# Grab a reference to the page at route '/hello'
page = site['/hello']

# Add a markdown card to the page.
page['quote'] = ui.markdown_card(
    box='2 2 4 5',
    title='Hello World',
    content='"The Internet? Is that thing still around?" - *Homer Simpson*',
)

# Finally, save the page.
page.save()