#!/usr/bin/env python3

import os
import re

def import_vars(lines):
    try:
        lines = [line.strip() for line in lines if not line.strip().startswith('#')]
        lines = [line.strip() for line in lines if not line == '']
        lines = [line.split('=') for line in lines]
        out, keys, vals = {}, [], []

        for line in lines:
            if(len(line)!=2):
                continue
            key, val = line

            if key in keys:
                print(f'The variable in "{key} = {val}" is a duplicate. Ignoring occurence')
                continue
            else:
                keys.append(key)
            if val in vals:
                if 'cam_' in key:
                    print(f'The value in "{key} = {val}" is a duplicate. Ignoring occurence')
                    continue
            else:
                vals.append(val)

            out[key.strip()] = val.strip()
        return out
    except Exception as ex:
        print(f'Exception during common file import. Exception: {ex}')
        return None