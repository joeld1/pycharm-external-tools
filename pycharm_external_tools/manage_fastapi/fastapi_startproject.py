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
from pycharm_external_tools.manage_fastapi.wrappers import manage_fastapi_startproject_wrapper

if __name__ == "__main__":
    project_path = Path(sys.argv[1]).as_posix()
    os.chdir(project_path)
    manage_fastapi_startproject_wrapper(cwd_path=project_path)
    # sys.exit()
