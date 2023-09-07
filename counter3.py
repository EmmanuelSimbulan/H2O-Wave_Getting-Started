from h2o_wave import Q, main, app, ui   # Note: We've also imported the symbol main into our .py file

@app('/counter3', mode = 'broadcast')   # @app is a decorator that takes one required argument - the route to listen to, in this case /counter, then we'll add a broadcast mode argument to syhcnronize the app across multiple users
async def serve(q: Q):      # Now, we applied this to a function called serve(), which is called when the user interacts with the app
    #bean_count = 0          # We've initialized a variable called bean_count to 0

    # This introduces two another concepts in Wave: (q.user) and (q.app)
    bean_count = q.app.bean_count or 0
    if q.args.increment:
        q.app.bean_count = bean_count = bean_count + 1

    # We've added a check to see if q.client.initialized is False. If it is, we set it to True and create the form card.
    if not q.client.initialized:
            q.client.initialized = True
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
    else:
        q.page['beans'].increment.caption = f'{bean_count} beans'
    await q.page.save()