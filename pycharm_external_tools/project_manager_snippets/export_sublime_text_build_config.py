import os
import sys
from pathlib import Path

from pycharm_external_tools.project_manager_snippets.wrappers import export_sublime_text_build_config_wrapper

sys.path.insert(0, Path(__file__).parent.parent.parent.as_posix())

if __name__ == "__main__":
    project_path = Path(sys.argv[1]).as_posix()
    os.chdir(project_path)
    export_sublime_text_build_config_wrapper()
