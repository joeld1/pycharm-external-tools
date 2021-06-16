import os
import sys
from pathlib import Path

sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())
from pycharm_external_tools.project_manager_snippets.wrappers import \
    generate_sublime_text_3_build_config_from_conda_env_wrapper


if __name__ == "__main__":
    project_path = Path(sys.argv[1]).as_posix()
    os.chdir(project_path)
    generate_sublime_text_3_build_config_from_conda_env_wrapper()
