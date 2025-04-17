import colorama
import json
import assets.configs.menus_text as menus_text
import os
import importlib
import importlib.util

MODULE_PATH = "modules"
MODULE_NAME = "module_main"
module_dict = {}

def import_all_modules():
    for dirpath, dirnames, filenames in os.walk(MODULE_PATH):
        if f"{MODULE_NAME}.py" in filenames:
            module_path = os.path.join(dirpath, f"{MODULE_NAME}.py")
            module_spec = importlib.util.spec_from_file_location(MODULE_NAME, module_path)
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            print(f"Импортирован модуль {module}... ")
            module_dict[os.path.basename(dirpath)] = module

def main():
    colorama.init()
    import_all_modules()

    # print(colorama.Fore.MAGENTA + menus_text.main_menu)
     
    print(module_dict)
            
    
if __name__ == "__main__":
    main()