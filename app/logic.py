import datetime

def parse_datetime(dt_str):
    # 支持 HTML datetime-local (YYYY-MM-DDTHH:MM) 和 自定义格式 (MM/DD/YYYY HH:MM)
    if 'T' in dt_str:
        return datetime.datetime.strptime(dt_str, "%Y-%m-%dT%H:%M")
    return datetime.datetime.strptime(dt_str, "%m/%d/%Y %H:%M")

def next_post_office_window(arrival_time):
    y, m, d = arrival_time.year, arrival_time.month, arrival_time.day
    day_6 = datetime.datetime(y, m, d, 6, 0)
    day_9 = datetime.datetime(y, m, d, 9, 0)
    if arrival_time <= day_6:
        return day_6
    elif day_6 < arrival_time <= day_9:
        return arrival_time
    else:
        nd = arrival_time + datetime.timedelta(days=1)
        return datetime.datetime(nd.year, nd.month, nd.day, 6, 0)

def get_channel_deadline(ata, channel, transport_type):
    base_hours = 40 if transport_type == "直入" else 64
    delivery_hours = 72 if channel == 727 else 60
    return ata + datetime.timedelta(hours=base_hours + delivery_hours)

def get_channel_travel_time(channel):
    return {707:9, 700:10, 727:7, 730:5}.get(channel)

def find_latest_departure_time_for_channel(ata, transport_type, channel, step):
    deadline = get_channel_deadline(ata, channel, transport_type)
    current = deadline
    delta = datetime.timedelta(minutes=step)
    while current >= ata:
        arrival_raw = current + datetime.timedelta(hours=get_channel_travel_time(channel))
        arrival_actual = next_post_office_window(arrival_raw)
        if arrival_actual <= deadline:
            return current
        current -= delta
    return None

def find_latest_departure_times(ata_str, transport_type, channels, step):
    ata = parse_datetime(ata_str)
    results = {}
    for ch in channels:
        results[ch] = find_latest_departure_time_for_channel(ata, transport_type, ch, step)
    return results 