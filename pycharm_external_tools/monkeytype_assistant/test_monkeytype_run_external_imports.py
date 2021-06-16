import inspect
import os
import shutil
import sqlite3
import sys
from collections import defaultdict
from pathlib import Path

from monkeytype.db.sqlite import SQLiteStore



sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from pycharm_external_tools.monkeytype_assistant import create_monkeytype_patch
# import MonkeytypeAssistant, get_module_path,monkeytype_run, monkeytype_list_modules, create_monkeytype_pyment_black_isort_patch
from pycharm_external_tools.tkinter_snippets.tk_snippets import show_info_message

if __name__ == "__main__":
    # prompt = r"Press Enter to start MonkeyType and Create Associated Patches!"
    # show_info_message(title="Starting script",message=prompt)

    # script_ran_on = Path(sys.argv[1])
    script_ran_on = Path("/Users/jd/Dropbox/Python Scripts/pycharm_external_tools/pycharm_external_tools/project_manager_snippets/test_external_import.py")
    root_dir = Path("/Users/jd/Dropbox/Python Scripts/pycharm_external_tools")


    monkeytype_assistant = create_monkeytype_patch.MonkeytypeAssistant(root_dir=root_dir)

    root_dir, module_path = create_monkeytype_patch.get_module_path(monkeytype_assistant, script_ran_on)
    from monkeytype_config import MyConfig
    create_monkeytype_patch.monkeytype_run(module_path)
    create_monkeytype_patch.monkeytype_list_modules()
    db_path = os.environ.get(MyConfig.DB_PATH_VAR, "monkeytype.sqlite3")
    conn = sqlite3.connect(db_path)
    monkeytype_modules_ran = SQLiteStore(conn=conn)
    cur_modules = monkeytype_modules_ran.list_modules()

    cur_module_collector = create_monkeytype_patch.globals_collector[module_path]
    all_modules_to_lookup = defaultdict(list)
    modules_lookedup_on_script = {}
    for k, v in cur_module_collector.items():
        cur_mod_name = getattr(v, "__module__", None)
        if cur_mod_name:
            modules_lookedup_on_script[k] = cur_mod_name
            all_modules_to_lookup[cur_mod_name].append(v)

    for cur_module in cur_modules:
        script_ran_on_dict_temp = {v:k for k,v in monkeytype_assistant.paths_to_modules.items() if v==cur_module}
        script_ran_on_path = script_ran_on_dict_temp.get(cur_module,None)
        if script_ran_on_path:
            script_ran_on_path = Path(script_ran_on_path)
            input_style = "reST"
            output_style = "reST"
            first_line = False
            profile = "black"
            create_monkeytype_patch.create_monkeytype_pyment_black_isort_patch(root_dir=root_dir, script_ran_on=script_ran_on_path,
                                                       module_path=cur_module, input_style=input_style,
                                                       output_style=output_style, first_line=first_line,
                                                       profile=profile)
        else:
            # TODO: Refactor
            if cur_module in all_modules_to_lookup.keys():
                for k, v in sys.modules.items():
                    if k == cur_module:
                        a = inspect.getfile(v)
                        cur_module_path = Path(a)
                        is_package = False
                        if Path(a).name == "__init__.py":
                            is_package = True

                        parent_length = len(cur_module_path.parts) - len(cur_module.split("."))
                        if is_package:
                            parent_length -= 1
                        for p in cur_module_path.parents:
                            if len(p.parts) == parent_length:
                                rel_path_to_create = Path(a).relative_to(p)
                                path_to_copy = root_dir.joinpath(rel_path_to_create)
                                path_to_copy.parent.mkdir(parents=True,exist_ok=True)
                                shutil.copy2(src=a,dst=path_to_copy)

                                script_ran_on_path = Path(path_to_copy)
                                input_style = "reST"
                                output_style = "reST"
                                first_line = False
                                profile = "black"
                                create_monkeytype_patch.create_monkeytype_pyment_black_isort_patch(root_dir=root_dir,
                                                                                                   script_ran_on=script_ran_on_path,
                                                                                                   module_path=cur_module,
                                                                                                   input_style=input_style,
                                                                                                   output_style=output_style,
                                                                                                   first_line=first_line,
                                                                                                   profile=profile)
                                path_to_package_external_module = root_dir.joinpath(rel_path_to_create.parents[0])
                                if path_to_package_external_module.is_dir():
                                    shutil.rmtree(path_to_package_external_module)
                                elif path_to_package_external_module.is_file() and path_to_package_external_module.exists():
                                    path_to_package_external_module.unlink()
            else:
                pass
    sys.exit()