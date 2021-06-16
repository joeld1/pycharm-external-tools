import os
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from pycharm_external_tools.project_manager_snippets.wrappers import migrate_requirements_to_pypoetry_toml_wrapper

if __name__ == "__main__":
    project_path = Path(sys.argv[1]).as_posix()
    os.chdir(project_path)
    migrate_requirements_to_pypoetry_toml_wrapper()
