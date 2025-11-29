# Original authors:
# Adrian Tschan <adrian.tschan@uzh.ch>
#
# This file is part of the Apricot Therapeutics Fractal Task Collection, which
# is developed by Apricot Therapeutics AG and intended to be used with the
# Fractal platform originally developed by eXact lab S.r.l.
# <exact-lab.it> under contract with Liberali Lab from the Friedrich Miescher
# Institute for Biomedical Research and Pelkmans Lab from the University of
# Zurich.


import logging
import subprocess
import fractal_tasks_core
from pydantic import validate_call
from pathlib import Path
import time

__OME_NGFF_VERSION__ = fractal_tasks_core.__OME_NGFF_VERSION__


logger = logging.getLogger(__name__)


@validate_call
def convert_tiff_to_png(  # noqa: C901
        *,
        # Default arguments for fractal tasks:
        zarr_dir: str,
        # Task-specific arguments:
        image_dir: str,
        batch: bool = True,
        batch_size: int = 200,
) -> None:
    """
    Convert all TIFF files in a directory to PNG files.
    See https://github.com/pelkmanslab/mf

    Args:
        Args:
        zarr_dir: path of the directory where the new OME-Zarrs will be
            created.
            (standard argument for Fractal tasks, managed by Fractal server).
        image_dir: Directory where the TIF files are located.
        batch: Whether to process the images in batches.
        batch_size: Number of images to process in each batch.
            Default is 200.
    """

    files_to_convert =list(Path(image_dir).glob("*.tif"))

    # run mf from a subprocess

    logger.info(f"Converting TIFF to PNG files in {image_dir}")
    logger.info("Submitting the following command to the shell:"
                f"{[
            '/data/homes/apricot/.conda/envs/mf_env/bin/python',
            "/data/homes/apricot/Code/mf/mf.py",
            image_dir,
            "--convert",
            "--batch" if batch else "",
            "--batch-size" if batch else "",
            str(batch_size) if batch else "",
        ]} ")

    subprocess.call(
        [
            '/data/homes/apricot/.conda/envs/mf_env/bin/python',
            "/data/homes/apricot/Code/mf/mf.py",
            image_dir,
            "--convert",
            "--batch" if batch else "",
            "--batch-size" if batch else "",
            str(batch_size) if batch else "",
        ]
    )

    # check occasionally if all TIF files have been converted
    remaining_files = list(Path(image_dir).glob("*.tif"))
    while len(remaining_files) > 0:
        logger.info(f"Waiting for {len(remaining_files)} files to be converted")
        remaining_files = list(Path(image_dir).glob("*.tif"))
        time.sleep(30)



if __name__ == "__main__":
    from fractal_task_tools.task_wrapper import run_fractal_task

    run_fractal_task(
        task_function=convert_tiff_to_png,
        logger_name=logger.name,
    )
