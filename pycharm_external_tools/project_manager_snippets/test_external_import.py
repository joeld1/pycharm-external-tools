import os
import sys
from pathlib import Path
from random import shuffle

sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from pycharm_external_tools.project_manager_snippets.wrappers import LocalProjectManager

init_current_dir_as_a_poetry_conda_project = LocalProjectManager.init_current_dir_as_a_poetry_conda_project

if __name__ == "__main__":
    # prompt = "Now going to start init_current_dir_as_a_poetry_conda_project_wrapper.py's __name__ == '__main__' method"
    # show_info_message(title="Starting script",message=prompt)
    old_path = "/Users/jd/Dropbox/Python Scripts/pycharm_external_tools"
    random_letters = list("uiljfhbnlokwjfakfljfal")
    shuffle(random_letters)
    clean_env_name = "".join(random_letters)
    python_version = "3.9",
    new_path = "/Users/jd/Dropbox/Python Scripts/dummy_proj"
    os.chdir(new_path)
    init_current_dir_as_a_poetry_conda_project(clean_env_name=clean_env_name, python_version=python_version)
    os.chdir(old_path)
    print("foobar")
