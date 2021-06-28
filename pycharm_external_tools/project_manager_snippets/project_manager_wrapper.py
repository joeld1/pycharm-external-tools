import os
import sys
from pathlib import Path


def add_root_dir_to_path(package_name: str = "pycharm_external_tools"):
    cur_path = Path(__file__)
    for p in cur_path.parents:
        if p.name == package_name:
            if p.parent.as_posix() not in sys.path:
                sys.path.insert(0, p.parent.as_posix())
            break


add_root_dir_to_path()
from pycharm_external_tools.project_manager_snippets.wrappers import (
    create_conda_env_for_existing_pyproject_toml_wrapper,
    export_sublime_text_build_config_wrapper,
    generate_sublime_text_3_build_config_from_conda_env_wrapper,
    init_current_dir_as_a_poetry_conda_project_wrapper,
    migrate_pyproject_toml_to_pyproject_toml_wrapper,
    migrate_requirements_to_pypoetry_toml_wrapper,
    uninstall_conda_and_kernel_wrapper,
    uninstall_conda_env_wrapper,
    uninstall_conda_envs_and_kernels_wrapper,
)

if __name__ == "__main__":
    project_path = Path(os.getcwd())
    os.chdir(project_path)
    method_to_call = sys.argv[1]

    if method_to_call == "create_conda_env_for_existing_pyproject_toml":
        create_conda_env_for_existing_pyproject_toml_wrapper()
    elif method_to_call == "export_sublime_text_build_config_wrapper":
        export_sublime_text_build_config_wrapper()
    elif method_to_call == "generate_sublime_text_3_build_config_from_conda_env":
        generate_sublime_text_3_build_config_from_conda_env_wrapper()
    elif method_to_call == "init_current_dir_as_a_poetry_conda_project":
        init_current_dir_as_a_poetry_conda_project_wrapper()
    elif method_to_call == "migrate_pyproject_toml_to_pyproject_toml":
        migrate_pyproject_toml_to_pyproject_toml_wrapper()
    elif method_to_call == "migrate_requirements_to_pypoetry_toml":
        migrate_requirements_to_pypoetry_toml_wrapper()
    elif method_to_call == "uninstall_conda_env":
        uninstall_conda_env_wrapper()
    elif method_to_call == "uninstall_conda_and_kernel":
        uninstall_conda_and_kernel_wrapper()
    elif method_to_call == "uninstall_conda_envs_and_kernels":
        uninstall_conda_envs_and_kernels_wrapper()
