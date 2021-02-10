import jinja2
import os
import pathlib

default_setup_template = "setup.jinja"
default_alarm_template = "alarm.jinja"
default_movement_template = "movement.jinja"

home_path = os.path.expanduser("~")
default_path = f"{home_path}/.apps/common/setup.conf"


def get_config_path_name():
    return os.getenv("SETUP_PATH", default_path)


def get_default_template_search_path():
    return f"{pathlib.Path(__file__).parent.absolute()}/templates/"


def get_template_search_path():
    return os.getenv("TEMPLATE_SEARCH_PATH", get_default_template_search_path())


def get_setup_template_path():
    return os.getenv("SETUP_TEMPLATE_PATH", default_setup_template)


def get_alarm_template_path():
    return os.getenv("ALARM_SETUP_PATH", default_alarm_template)


def merge(history, live, movement):
    cams = history.copy()
    ips = [c["networkAddress"] for c in history]
    for cam in live:
        if not cam["networkAddress"] in ips:
            cams.append(cam)
    ips = [c["networkAddress"] for c in cams]
    for cam in movement:
        if not cam["networkAddress"] in ips:
            cams.append(cam)
    return cams


def generate_conf(template, data):
    searchpath = get_template_search_path()
    print(searchpath)
    templateLoader = jinja2.FileSystemLoader(searchpath=searchpath)
    templateEnv = jinja2.Environment(loader=templateLoader, autoescape=True)
    template = templateEnv.get_template(template)
    outputText = template.render(data)
    setup_file = open(get_config_path_name(), "w")
    setup_file.write(outputText)
    setup_file.close()


def generate_setup_conf(server_history, server_live, server_alarm, server_tag):
    name = server_history[0]["streamName"].split("_")[0]
    cams = merge(server_history, server_live, server_alarm)
    history_list = [c["streamName"] for c in server_history]
    live_list = [c["streamName"] for c in server_live]
    movement_list = [c["streamName"] for c in server_alarm]
    data = {
        "tag": server_tag,
        "name": name,
        "history": server_history,
        "live": server_live,
        "cams": cams,
        "history_list": history_list,
        "live_list": live_list,
        "movement_list": movement_list,
    }
    generate_conf(get_setup_template_path(), data)


def generate_alarm_conf(server_alarm):
    data = {"pinlist": [], "idlist": []}
    generate_conf(get_alarm_template_path(), data)

