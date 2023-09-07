from h2o_wave import Q, main, app, ui   # Note: We've also imported the symbol main into our .py file

@app('/counter')            # @app is a decorator that takes one required argument - the route to listen to, in this case /counter (this uses unicast)
async def serve(q: Q):      # Now, we applied this to a function called serve(), which is called when the user interacts with the app
    #bean_count = 0          # We've initialized a variable called bean_count to 0

    # This introduces two importand concepts in Wave: (q.client) and (q.args)
    # q.client is a dictionary that Wave uses to store data that persists across requests
    # q.args is a dictionary that Wave uses to store data that is passed from the client to the server
    bean_count = q.client.bean_count or 0
    if q.args.increment:
        q.client.bean_count = bean_count = bean_count + 1

    q.page['beans'] = ui.form_card(     # We've created a form card with a button that increments the bean_count variable
        box='1 1 1 2',
        items=[
            ui.button(
                name='increment',       # The button has a name called increment, which we can use to identify the button
                label='Click me!',
                caption=f'{bean_count} beans',  # The caption shows the current value of bean_count
                primary=True,                   # The button is the primary action of the form
            ),
        ],
    )
    await q.page.save()