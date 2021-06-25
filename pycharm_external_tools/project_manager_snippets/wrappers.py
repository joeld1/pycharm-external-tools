import os
import sys
from pathlib import Path


def add_root_dir_to_path(package_name:str="pycharm_external_tools"):
    cur_path = Path(__file__)
    for p in cur_path.parents:
        if p.name == package_name:
            if p.parent.as_posix() not in sys.path:
                sys.path.insert(0, p.parent.as_posix())
            break
add_root_dir_to_path()
from project_manager import LocalProjectManager, SublimeBuildConfigGenerator

from pycharm_external_tools.tkinter_snippets.tk_snippets import (
    TkinterForm,
    get_filepath,
)


def export_sublime_text_build_config_wrapper():
    kwargs_to_pass_into_method = {"build_config_name": "Enter a name for the Sublime Text 3 build config"}
    my_form = TkinterForm(dict_to_convert_to_form=kwargs_to_pass_into_method)
    cur_form = my_form.submitted_form_values.copy()

    kwargs_to_pass_into_method.update(cur_form)
    kwargs_to_pass_into_method["path_to_python_bin"] = get_filepath(
        prompt="Select python interpreter to generate a build config for",
        init_dir=os.getcwd())
    print(f"Kwargs we'll be supplying are:\n{kwargs_to_pass_into_method}")
    r = SublimeBuildConfigGenerator.export_sublime_text_build_config(**kwargs_to_pass_into_method)


def generate_sublime_text_3_build_config_from_conda_env_wrapper():
    kwargs_to_pass_into_method = {
        "env_name": "Enter the Conda Env Name that you'd like to create a Sublime build config for"}
    my_form = TkinterForm(dict_to_convert_to_form=kwargs_to_pass_into_method)
    cur_form = my_form.submitted_form_values.copy()

    kwargs_to_pass_into_method.update(cur_form)
    print(f"Kwargs we'll be supplying are:\n{kwargs_to_pass_into_method}")
    r = SublimeBuildConfigGenerator.generate_sublime_text_3_build_config_from_conda_env(**kwargs_to_pass_into_method)


def migrate_pyproject_toml_to_pyproject_toml_wrapper():
    kwargs_to_pass_into_method = {
        "poetry_proj_conda_env_name": "Enter the Conda Env Name for the Poetry Project you want to update"}
    my_form = TkinterForm(dict_to_convert_to_form=kwargs_to_pass_into_method)
    cur_form = my_form.submitted_form_values.copy()

    kwargs_to_pass_into_method.update(cur_form)
    kwargs_to_pass_into_method["dest_pyproject_toml"] = get_filepath(prompt="Select pyproject.toml to update",
                                                                     init_dir=os.getcwd())
    kwargs_to_pass_into_method["src_pyproject_toml"] = get_filepath(
        prompt="Select pyproject.toml to use for updating/migrating", init_dir=os.getcwd())

    kwargs_to_pass_into_method["warn_before_add"] = True
    print(f"Kwargs we'll be supplying are:\n{kwargs_to_pass_into_method}")
    r = LocalProjectManager.migrate_pyproject_toml_to_pyproject_toml(**kwargs_to_pass_into_method)


def migrate_requirements_to_pypoetry_toml_wrapper():
    kwargs_to_pass_into_method = {
        "poetry_proj_conda_env_name": "Enter the Conda Env Name for the Poetry Project you want to update"}
    my_form = TkinterForm(dict_to_convert_to_form=kwargs_to_pass_into_method)
    cur_form = my_form.submitted_form_values.copy()

    kwargs_to_pass_into_method.update(cur_form)
    kwargs_to_pass_into_method["src_path_to_reqs"] = get_filepath(
        prompt="Select requirements.txt file to migrate to pypoetry.toml",
        init_dir=os.getcwd())
    kwargs_to_pass_into_method["dest_path_to_pyproject_toml"] = get_filepath(prompt="Select pyproject.toml to update",
                                                                             init_dir=os.getcwd())

    kwargs_to_pass_into_method["try_pinned_versions"] = False
    kwargs_to_pass_into_method["warn_before_add"] = True
    print(f"Kwargs we'll be supplying are:\n{kwargs_to_pass_into_method}")
    r = LocalProjectManager.migrate_requirements_to_pypoetry_toml(**kwargs_to_pass_into_method)

def create_conda_env_for_existing_pyproject_toml_wrapper():
    toml_path = get_filepath(
        prompt="Select the pyproject.toml file to create a conda env for",
        init_dir=os.getcwd())
    assert Path(toml_path).name == "pyproject.toml"
    r = LocalProjectManager.create_conda_env_for_existing_pyproject_toml(pyproject_toml_path=toml_path)




# TODO: Create wrappers for following
"""

ProjectManager.add_git_ignore_to_project

PoetryProjectManager.clear_poetry_cache
PoetryProjectManager.execute_poetry_init
PoetryProjectManager.link_poetry_proj_with_conda_env
PoetryProjectManager.create_poetry_project
PoetryProjectManager.init_poetry_project
PoetryProjectManager.add_notebook_ipykernel_dependencies_to_pypoetry
CondaEnvManager.get_path_to_confastapi startappda_env
CondaEnvManager.init_prev_made_conda_env
CondaEnvManager.uninstall_kernel
CondaEnvManager.uninstall_conda_env
CondaEnvManager.uninstall_conda_and_kernel
CondaEnvManager.create_and_init_conda_env

LocalProjectManager.create_init_link_conda_env_to_existing_poetry_project

yapf
auto_py_to_exe
manage_fastapi
run_in_docker"""
