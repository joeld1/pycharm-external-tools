import os
import shutil
import sys
import tempfile
from pathlib import Path
from shutil import copy2

from notebooktoall.transform import transform_notebook
from project_manager.project_manager import convert_camel_to_snakecase


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
)

temp_dir = tempfile.TemporaryDirectory()


def convert_jupyter_notebook_to_py_in_tempdir(ipynb_path: str) -> str:
    old_path = os.getcwd()
    nb_path = Path(ipynb_path).resolve()
    temp_ipynb_file = Path(temp_dir.name).with_name(nb_path.name)
    temp_py_file = temp_ipynb_file.with_suffix(".py")
    shutil.copy2(nb_path, temp_ipynb_file)
    os.chdir(temp_ipynb_file.parent.as_posix())
    transform_notebook(ipynb_file=temp_ipynb_file.as_posix(), export_list=["py"])
    os.chdir(old_path)
    return temp_py_file.as_posix()


def convert_ipynb_to_py(ipynb_path: str):
    ipynb_path = Path(ipynb_path)
    try:
        assert ipynb_path.as_posix().lower().endswith(".ipynb") and ipynb_path.exists()
    except Exception as e:
        print("Select an existing ipynb file!")
        raise e

    old_filename = ipynb_path.stem
    temp_py_file = Path(convert_jupyter_notebook_to_py_in_tempdir(ipynb_path=ipynb_path.as_posix()))

    params_to_input = {
        "new_filename": "Rename converted file? (leave blank if No, otherwise enter name w/o .py extension)",
        "use_snake_case_name": "Use snakecase of original name? (default is True, and first form entry always overrides this field)"}
    param_default_vals = {"new_filename": "",
                          "use_snake_case_name": ["True", "False"]}
    my_form = TkinterForm(dict_to_convert_to_form=params_to_input, default_form_vals=param_default_vals)
    submitted_form = my_form.submitted_form_values.copy()
    destroy_root()

    new_filename = submitted_form.get("new_filename")
    use_snake_case_name = submitted_form.get("use_snake_case_name") == "True"

    if new_filename:
        new_name = f"{new_filename}.py"
    elif use_snake_case_name:
        new_name = convert_camel_to_snakecase(old_filename) + ".py"
    else:
        new_name = old_filename + ".py"
    new_filepath = ipynb_path.with_name(new_name)
    try:
        assert not new_filepath.exists()
    except Exception as e:
        print(f"{new_filepath} already exists! Either rename or delete existing file")
        raise e
    copy2(src=temp_py_file, dst=new_filepath)
    temp_dir.cleanup()
    rc = 0
    print(rc)
    return rc


if __name__ == "__main__":
    ipynb_path = sys.argv[1]
    rc = convert_ipynb_to_py(ipynb_path)
