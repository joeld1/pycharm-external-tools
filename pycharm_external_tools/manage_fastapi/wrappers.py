import os
import sys
from collections import deque
from pathlib import Path
from typing import Optional, List


def add_root_dir_to_path(package_name: str = "pycharm_external_tools"):
    cur_path = Path(__file__)
    for p in cur_path.parents:
        if p.name == package_name:
            if p.parent.as_posix() not in sys.path:
                sys.path.insert(0, p.parent.as_posix())
            break


add_root_dir_to_path()

from pycharm_external_tools.tkinter_snippets.tk_snippets import TkinterForm, show_info_message, \
    get_directory_path, ask_string, destroy_root

from project_manager import CommonPSCommands


def prompt_for_manage_fastapi_flags():
    permutations_desc = {'database': "Add database?",
                         'docker': "Add Docker?",
                         '--license': "Select a license",
                         '--packaging': "Select packaging",
                         'pre-commit': "Add pre-commit?",
                         '--python': "Select Python version"
                         }
    permutations = {'database': ['--database=Postgres', ''],
                    'docker': ['--docker', '--no-docker'],
                    '--license': ['MIT', 'BSD', 'GNU', 'Apache'],
                    '--packaging': ['poetry', 'pip'],
                    'pre-commit': ['--pre-commit', ''],
                    '--python': ['3.8', '3.7', '3.6']
                    }
    my_form = TkinterForm(dict_to_convert_to_form=permutations_desc, default_form_vals=permutations)
    submitted_form = my_form.submitted_form_values.copy()
    manage_fastapi_flags = deque()
    for k, v in submitted_form.items():
        cur_v = [v]
        if k.startswith('--'):
            new_vals = [f'{k}={v2}' for v2 in cur_v]
            manage_fastapi_flags.extend(new_vals.copy())
        else:
            manage_fastapi_flags.extend(cur_v.copy())
    form_vals = list(manage_fastapi_flags)
    return form_vals


def manage_fastapi_startproject_wrapper(fastapi_project_name: Optional[str] = None,
                                        fastapi_project_root_dir: Optional[str] = None,
                                        cwd_path: Optional[str] = None,
                                        manage_fastapi_flags: Optional[List[str]] = None):
    if fastapi_project_name is None:
        fastapi_project_name = ask_string(title="FastAPI Project Name",
                                          prompt="Enter a valid name to use for your FastAPI project!")
        if fastapi_project_name == "":
            print("manage-fastapi requires a FastAPI project name! Raising exception")
            raise Exception

    if cwd_path is None:
        project_path = Path(".").resolve().as_posix()
    else:
        project_path = Path(cwd_path).resolve()
        assert project_path.exists()
    os.chdir(project_path)

    if fastapi_project_root_dir is None:
        prompt = "Select directory that will contain FastAPI project"
        show_info_message(title="Choose root folder", message=prompt)
        fastapi_project_root_dir = get_directory_path(prompt=prompt, init_dir=project_path)
    os.chdir(fastapi_project_root_dir)

    path_to_manage_fastapi = Path(sys.executable).parent.joinpath("fastapi")

    cmd_args = [path_to_manage_fastapi.as_posix(), 'startproject', fastapi_project_name, '--no-interactive']

    if manage_fastapi_flags is None:
        manage_fastapi_flags = prompt_for_manage_fastapi_flags()
    destroy_root()
    cmd_args.extend(manage_fastapi_flags)
    r = CommonPSCommands.run_command(cmd_args=cmd_args, text=True, verbose=True, cwd=fastapi_project_root_dir)
    assert r == 0
    return r


