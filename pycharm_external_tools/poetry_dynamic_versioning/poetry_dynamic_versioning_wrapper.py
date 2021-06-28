import os
import sys
from pathlib import Path

import pyperclip


def add_root_dir_to_path(package_name: str = "pycharm_external_tools"):
    cur_path = Path(__file__)
    for p in cur_path.parents:
        if p.name == package_name:
            if p.parent.as_posix() not in sys.path:
                sys.path.insert(0, p.parent.as_posix())
            break


add_root_dir_to_path()
from pycharm_external_tools.tkinter_snippets.tk_snippets import (
    TkinterForm,
    destroy_root,
    get_directory_path,
    get_filepath,
    show_info_message,
)


def get_current_commit_hash():
    """
    https://stackoverflow.com/questions/949314/how-to-retrieve-the-hash-for-the-current-commit-in-git
    :return:
    """
    command = "git rev-parse --short HEAD"
    print(command)


def get_poetry_dynamic_versioning_settings():
    """

    :return:
    """
    path_to_file = Path(__file__).parent.joinpath('settings_template.toml')
    with open(path_to_file, 'r', encoding='utf-8') as f:
        template = f.read()
    return template


def copy_poetry_dynamic_versioning_template_to_clipboard():
    template = get_poetry_dynamic_versioning_settings()
    pyperclip.copy(template)


if __name__ == "__main__":
    project_path = Path(os.getcwd())
    os.chdir(project_path)

    cur_dir_files = os.listdir(".")
    assert (".git" in cur_dir_files) and ("pyproject.toml" in cur_dir_files)

    method_to_call = sys.argv[1]

    if method_to_call == "copy_poetry_dynamic_versioning_template_to_clipboard":
        copy_poetry_dynamic_versioning_template_to_clipboard()
