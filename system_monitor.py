import time
import psutil
from h2o_wave import site, ui, data

# Grab a reference to the page at route '/monitor'
page = site['/monitor']

# This displays a value and a time series visualization
cpu_card = page.add('cpu_stats', ui.small_series_stat_card( # instead of using  ui.markdown_card()
    box='1 1 1 1',                                          # we use ui.small_series_stat_card()
    title='CPU',                                            # to display the CPU usage
    value='={{usage}}%',
    data=dict(usage=0.0),                                   # This card is capable of dealing with multiples rows of data

    # Declaring a Data Buffer
    plot_data=data('tick usage', -15),
    plot_category='tick',                                   # This method is to display information on the card, 
    plot_value='usage',                                     # you only need to send it new values (and not all the data rows all over again)
    plot_zero_value=0,
    plot_color='$red',
))

# Adding Monitor for Memory Usage
mem_card = page.add('mem_stats', ui.small_series_stat_card( # Again, we also uses ui.small_series_stat_card() in this code
    box='1 2 1 1',
    title='Memory',
    value='={{usage}}%',
    data=dict(usage=0.0),
    plot_data=data('tick usage', -15),
    plot_category='tick',
    plot_value='usage',
    plot_zero_value=0,
    plot_color='$blue',
))


tick = 0
while True:
    tick += 1

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_card.data.usage = cpu_usage
    cpu_card.plot_data[-1] = [tick, cpu_usage]             # This measure CPU usage every second and append a new row to the end of card's data buffer

    mem_usage = psutil.virtual_memory().percent            # We also addeed this new line of code to measure memory usage every second
    mem_card.data.usage = mem_usage
    mem_card.plot_data[-1] = [tick, mem_usage]

    page.save()
    time.sleep(1)