"""Create manifest for apx mf wrapper task.

Generate JSON schemas for task arguments afresh, and write them
to the package manifest.
"""

from fractal_tasks_core.dev.create_manifest import create_manifest

if __name__ == "__main__":
    PACKAGE = "apx_mf_wrapper_task"
    AUTHORS = "Adrian Tschan"
    docs_link = ""
    if docs_link:
        create_manifest(package=PACKAGE, authors=AUTHORS, docs_link=docs_link)
    else:
        create_manifest(package=PACKAGE, authors=AUTHORS)