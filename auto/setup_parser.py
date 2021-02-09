#!/usr/bin/env python3

import os
import re
from urllib.parse import urlparse

home_path = os.path.expanduser("~")
default_path = f'{home_path}/.apps/common/setup.conf'
def get_config_path_name():
    return os.getenv('SETUP_PATH', default_path)

def import_vars():
    try:
        with open(get_config_path_name()) as file:
            lines = file.readlines()
        lines = [line.strip() for line in lines if not line.strip().startswith('#')]  # remove comment lines
        lines = [line.strip() for line in lines if not line == '']  # remove empty lines
        lines = [line.split('=') for line in lines]
        out, keys, vals = {}, [], []

        # Save occurences to a dict
        for line in lines:
            # If unpacked is not 2, format is wrong, ignored
            if(len(line)!=2):
                continue
            key, val = line

            # Check for duplicates
            if key in keys:
                # Duplicate key
                print(f'The variable in "{key} = {val}" is a duplicate. Ignoring occurence')
                continue
            else:
                keys.append(key)
            if val in vals:
                # Duplicate val
                if 'cam_' in key:
                    print(f'The value in "{key} = {val}" is a duplicate. Ignoring occurence')
                    continue
            else:
                vals.append(val)

            # Create dict
            out[key.strip()] = val.strip()
        print()
        return out
    except Exception as ex:
        print(f'Exception during common file import. Exception: {ex}')
        return None


def update_vars(**kwargs):
    lines_to_update=[] # tuples of (<line_number>, <line_str>)


def remove_vars(*vars):
    lines_to_remove = [] # line numbers


def get_vars(*vars) -> dict:
    '''Receives a list of vars and returns a dict of the found values'''
    vars = set(vars)
    vars_from_file = import_vars()
    vars_found = {key: vars_from_file[key] for key in vars & vars_from_file.items()}
    return vars_found


def insert_vars(**kwargs):
    vars = import_vars()
    vars_to_update = {key: vars[key] for key in kwargs.keys() & vars.items()}
    vars_to_add = dict(vars, **kwargs)
    with open(get_config_path_name(), 'a+') as file:
        for key, val in vars_to_add.items():
            file.write(f'{key}={val}')

def decode_history():
    vars = import_vars()
    history = vars['history']
    history = [x.strip() for x in history.split(',')]
    decoded = {}
    for h in history:
        decoded[h] = vars[h]
    return decoded

def decode_live():
    vars = import_vars()
    livestream = vars['livestream']
    livestream = [x.strip() for x in livestream.split(',')]
    decoded = {}
    for h in livestream:
        decoded[h] = vars[h]
    return decoded    

if __name__=='__main__':
    print(import_vars())

