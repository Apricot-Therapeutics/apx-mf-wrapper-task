import json
from pathlib import Path

import apx_mf_wrapper_task

PACKAGE = "apx_mf_wrapper_task"
PACKAGE_DIR = Path(apx_mf_wrapper_task.__file__).parent
MANIFEST_FILE = PACKAGE_DIR / "__FRACTAL_MANIFEST__.json"
with MANIFEST_FILE.open("r") as f:
    MANIFEST = json.load(f)
    TASK_LIST = MANIFEST["task_list"]
