import shutil
from pathlib import Path

import pytest
from devtools import debug

from apx_mf_wrapper_task.convert_tiff_to_png import convert_tiff_to_png


@pytest.fixture(scope="function")
def test_data_dir(tmp_path: Path) -> str:
    """
    Copy a test-data folder into a temporary folder.
    """
    source_dir = (Path(__file__).parent / "data/ngff_example/my_image").as_posix()
    dest_dir = (tmp_path / "my_image").as_posix()
    debug(source_dir, dest_dir)
    shutil.copytree(source_dir, dest_dir)
    return dest_dir


def test_convert_tiff_to_png(test_data_dir):
    convert_tiff_to_png(
        zarr_urls=["/data/active/apricot/OVP/20250416_OVP_OV-G2-H01-001_O-FAREMON/zarr/20250416_OVP_OFAREMON.zarr"],
        zarr_dir="/data/active/apricot/OVP/20250416_OVP_OV-G2-H01-001_O-FAREMON/zarr/",
        image_dir="/data/active/apricot/OVP/20250416_OVP_OV-G2-H01-001_O-FAREMON/raw_images/test",
        batch=True,
        batch_size=200,)

