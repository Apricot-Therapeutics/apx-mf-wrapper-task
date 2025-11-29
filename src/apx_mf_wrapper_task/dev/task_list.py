"""Contains the list of tasks available to fractal."""

from fractal_task_tools.task_models import (
    ConverterNonParallelTask,
)

AUTHORS = "Adrian Tschan"
DOCS_LINK = None
INPUT_MODELS = []

TASK_LIST = [
    ConverterNonParallelTask(
        name="Convert TIFF to PNG",
        executable="convert_tiff_to_png.py",
        meta={"cpus_per_task": 1, "mem": 4000},
        category="Image Processing",
        tags=["Conversion"],
    ),
]
