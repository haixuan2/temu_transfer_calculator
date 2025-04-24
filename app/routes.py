from flask import Blueprint, request, render_template
from app.logic import find_latest_departure_times

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    ata = '04/17/2025 10:19'
    transport = '直入'
    ch_str = '727,730,707,700'
    step = 30
    results = None
    if request.method == 'POST':
        ata = request.form['ata']
        transport = request.form['transport']
        # Retrieve multiple selected channels
        channels_selected = request.form.getlist('channels')
        # For repopulating the template
        ch_str = ','.join(channels_selected)
        step = int(request.form['step'])
        # Convert selected values to integers
        channels = [int(c) for c in channels_selected if c.isdigit()]
        results = find_latest_departure_times(ata, transport, channels, step)
    return render_template('index.html', ata=ata, transport=transport, ch_str=ch_str, step=step, results=results) 