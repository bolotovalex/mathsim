from platform import system as check_system
from os import system, mkdir, path
from json import dump


def check_platform():
    # If platform not Windows
    if check_system() != 'Windows':
        platform = 'unix'
        home = path.expanduser(f'~/')
        home_local = home + '.mathsim/'
        name_config = 'config.json'
        path_to_config = home_local + name_config
        path_to_db = home + 'mathsim.db'

        # Check ~/.mathsim folder
        check_folder = path.exists(home_local)
        if check_folder is False:
            mkdir(home_local)
            with open(path_to_config, 'tw', encoding='utf-8') as f:
                dump({}, f, indent=4)
            f.close()

        # Check ~/.mathsim/config.json file
        check_config = path.exists(path_to_config)
        if check_config is False:
            with open(path_to_config, 'tw', encoding='utf-8') as f:
                dump({}, f, indent=4)
            f.close()


    # If platform Windows
    else:
        platform = 'win'
        home = path.expanduser(f"~\\")
        home_local = home + str(".mathsim\\")
        check = system(f'cd {home_local}')
        name_config = 'config.json'
        path_to_config = home_local + name_config
        path_to_db = home_local + 'mathsim.db'
        if check == 1:
            mkdir(home_local)
            with open(path_to_config, 'tw', encoding='utf-8') as f:
                dump({}, f, indent=4)
            f.close()

        else:
            if path.exists(path_to_config) is False:
                with open(path_to_config, 'tw', encoding='utf-8') as f:
                    dump({}, f, indent=4)
                f.close()

    return path_to_config, path_to_db


#print(check_platform())
