import os
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from pycharm_external_tools.project_manager_snippets.wrappers import migrate_pyproject_toml_to_pyproject_toml_wrapper


if __name__ == "__main__":
    project_path = Path(sys.argv[1]).as_posix()
    os.chdir(project_path)
    migrate_pyproject_toml_to_pyproject_toml_wrapper()
