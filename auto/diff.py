from auto.json_parser import decode_history, decode_live, decode_movement, decode_tag
from auto.sync import sync
from auto.setup_parser import import_vars
from auto.setup_parser import decode_history as sdh
from auto.setup_parser import decode_live as sdl
from auto.setup_parser import decode_movement as sdm

def contains(address, local):
    for a in local:
        if address in a:
            return True
    return False

def has_changed(server, local):
    local_values = local.values()
    for c in server:
        if not contains(c["networkAddress"], local_values):
            return True
    return False

def diff():
    server_config = sync()
    server_history = decode_history(server_config)
    server_live = decode_live(server_config)
    server_alarm = decode_movement(server_config)
    server_tag = decode_tag(server_config)
    setup_vars = import_vars()
    if setup_vars is not None:
        change_history, change_live, change_alarm = False, False, False
        local_history = sdh()
        local_live = sdl()
        local_alarm = sdm()
        local_tag = setup_vars['stream_desc']
        local_stream = setup_vars['stream_name']
        if len(server_history) != len(local_history):
            change_history = True
        if len(server_live) != len(local_live):
            change_live = True
        if len(server_alarm) != len(local_alarm):
            change_alarm = True
        if not change_history:
            change_history = has_changed(server_history, local_history)
        if not change_live:
            change_live = has_changed(server_live, local_live)
        if not change_alarm:
            change_alarm = has_changed(server_alarm, local_alarm)                       

        return (change_history, change_live, change_alarm, server_history, server_live, server_alarm, server_tag)
    else:
        return (True, True, True, server_history, server_live, server_alarm, server_tag)

    return None

if __name__ == "__main__":
    diff()