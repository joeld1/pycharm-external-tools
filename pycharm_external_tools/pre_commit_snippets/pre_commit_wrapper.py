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


def read_pre_commit_sample():
    """

    :return:
    """
    path_to_file = Path(__file__).parent.joinpath("pre_commit_sample.txt")
    with open(path_to_file, "r", encoding="utf-8") as f:
        template = f.read()
    return template


def copy_pre_commit_sample_template_to_clipboard():
    template = read_pre_commit_sample()
    pyperclip.copy(template)


if __name__ == "__main__":
    method_to_call = sys.argv[1]

    if method_to_call == "copy_pre_commit_sample_template_to_clipboard":
        copy_pre_commit_sample_template_to_clipboard()
