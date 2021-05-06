from platform import system as check_system
from os import system, mkdir, path


def check_platform():
    # If platform not Windows
    if check_system() != 'Windows':
        platform = 'unix'
        home = path.expanduser(f'~/')
        home_local = home + '.mathsim/'
        name_config = 'config.ini'
        path_to_config = home_local + name_config
        path_to_db = home + 'mathsim.db'

        # Check ~/.mathsim folder
        check_folder = path.exists(home_local)
        if check_folder is False:
            mkdir(home_local)

        # Check ~/.mathsim/config.ini file
        check_config = path.exists(path_to_config)
        if check_config is False:
            f = open(path_to_config, 'tw', encoding='utf-8')
            f.close()


    # If platform Windows
    else:
        platform = 'win'
        home = path.expanduser(f"~\\")
        home_local = home + str(".mathsim\\")
        check = system(f'cd {home_local}')
        name_config = 'config.ini'
        path_to_config = home_local + name_config
        path_to_db = home_local + 'mathsim.db'
        if check == 1:
            mkdir(home_local)
            system(f'type nul > {home_local}\\config.ini')
            mkdir(path_to_keys)
        else:
            if path.exists(path_to_config) is False:
                f = open(path_to_config, 'tw', encoding='utf-8')
                f.close()

    return path_to_config, path_to_db


print(check_platform())
