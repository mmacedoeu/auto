from auto.diff import diff
from auto.generate import generate_setup_conf, generate_alarm_conf
from auto.restart import restart

default_history_name_container = "history"
default_livestream_name_container = "livestream"
default_alarm_name_container = "alarm"
default_movement_name_container = "movement"

def run():
    (
        change_history,
        change_live,
        change_alarm,
        server_history,
        server_live,
        server_alarm,
        server_tag,
    ) = diff()
    if change_history or change_live or change_alarm:
        generate_setup_conf(server_history, server_live, server_alarm, server_tag)
        if change_history:
            restart(default_history_name_container)
        if change_live:
            restart(default_livestream_name_container)
        if change_alarm:
            # generate_alarm_conf(server_alarm)
            restart(default_movement_name_container)
