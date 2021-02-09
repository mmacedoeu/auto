import os

home_path = os.path.expanduser("~")
default_path = f'{home_path}/.apps/modules/alarm/alarm.conf'
def get_config_path_name():
    return os.getenv('ALARM_PATH', default_path)    

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
        return out
    except Exception as ex:
        print(f'Exception during common file import. Exception: {ex}')
        return None