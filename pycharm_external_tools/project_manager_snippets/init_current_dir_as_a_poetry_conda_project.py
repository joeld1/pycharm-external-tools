import os
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from pycharm_external_tools.tkinter_snippets.tk_snippets import (
    TkinterForm,
    get_directory_path, show_info_message,
)

sys.path.insert(0, r"/Users/jd/Dropbox/Python Scripts/project_manager")
# noinspection PyUnresolvedReferences
from project_manager import LocalProjectManager


def init_current_dir_as_a_poetry_conda_project_wrapper():
    """ """
    kwargs_to_pass_into_method = {
        "clean_env_name": "Enter a name to use for the Poetry Conda environment",
        "python_version": "Enter a Python Version to Use",
    }
    input("Enter the following values in the form! [enter any key to continue]")
    print("-" * 60)
    for k, v in kwargs_to_pass_into_method.items():
        print(f"{k}:\t\t\t{v}")
    print("")
    my_form = TkinterForm(dict_to_convert_to_form=kwargs_to_pass_into_method)
    cur_form = my_form.submitted_form_values.copy()
    kwargs_to_pass_into_method.update(cur_form)
    kwargs_to_pass_into_method["add_git"] = False
    LocalProjectManager.init_current_dir_as_a_poetry_conda_project(
        **kwargs_to_pass_into_method
    )
    print("Success!")


if __name__ == "__main__":
    prompt = "Now going to start init_current_dir_as_a_poetry_conda_project_wrapper.py's __name__ == '__main__' method"
    show_info_message(title="Starting script", message=prompt)
    try:
        project_path = Path(sys.argv[1])
        if project_path.exists():
            project_path = project_path.as_posix()
    except Exception as e:
        project_path = Path(__file__).parent.parent.parent.as_posix()
    prompt = "Select directory to init conda poetry project in!"
    show_info_message(title="Select Directory",
                      message=prompt)
    dir_to_cd_into = get_directory_path(prompt=prompt, init_dir=project_path)
    os.chdir(dir_to_cd_into)
    init_current_dir_as_a_poetry_conda_project_wrapper()
