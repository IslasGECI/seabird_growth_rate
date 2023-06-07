import pandas as pd
import hashlib
import pytest
import numpy as np

from seabird_growth_rate import (
    get_lambda_from_csv,
    get_number_of_nests,
    get_to_plot_from_island_and_specie,
    plot_log_linear_tendency,
)


expected_path = "tests/data/expected_number_of_nests_seabirds.csv"
expected_dataframe = pd.read_csv(expected_path)


def test_get_number_of_nests():
    path = "tests/data/number_of_nests_seabirds.csv"
    obtained_dataframe = get_number_of_nests(path)
    pd.testing.assert_frame_equal(obtained_dataframe, expected_dataframe)


EXPECTED_PLOT_CONFIG = {
    "resources": [
        {
            "name": "table",
            "data": expected_dataframe[
                (expected_dataframe.Species_name == "Brown Pelican")
                & (expected_dataframe.Island == "Coronado")
            ].sort_values(by="Season"),
            "island": "Coronado",
            "species": "Brown Pelican",
        },
        {
            "name": "fitted_model",
            "data": {"x": [2014, 2019], "y": [189.8008, 936.8397]},
            "lambda": 1.28,
        },
    ],
    "scales": [
        {
            "name": "Season",
            "type": "linear",
            "range": "width",
            "domain": {"data": "table", "field": "Season"},
        },
        {
            "name": "Logarithmic number of breeding pairs",
            "type": "log",
            "range": "height",
            "domain": {"data": "table", "field": "Maximum_number_of_nests"},
        },
    ],
    "style": [{"point": "o"}, {"line": "-k"}],
}


def test_get_to_plot_from_island_and_specie():
    csv_path = "tests/data/input_get_lambda_from_csv.csv"
    brpe_to_plot = get_to_plot_from_island_and_specie(
        expected_dataframe, "Coronado", "Brown Pelican", csv_path
    )
    assert brpe_to_plot["resources"][0]["data"].equals(EXPECTED_PLOT_CONFIG["resources"][0]["data"])
    assert (
        brpe_to_plot["resources"][1]["data"]["x"]
        == EXPECTED_PLOT_CONFIG["resources"][1]["data"]["x"]
    )
    assert (
        pytest.approx(brpe_to_plot["resources"][1]["data"]["y"], 0.001)
        == EXPECTED_PLOT_CONFIG["resources"][1]["data"]["y"]
    )
    assert brpe_to_plot["resources"][1]["lambda"] == EXPECTED_PLOT_CONFIG["resources"][1]["lambda"]


def test_get_lambda_from_csv():
    csv_path = "tests/data/input_get_lambda_from_csv.csv"
    expected = 1.19
    species = "Brown Pelican"
    island = "Asuncion"
    obtained = get_lambda_from_csv(species, island, csv_path)
    assert obtained == expected
    expected = 2.73
    species = "Western Gull"
    island = "San Jeronimo"
    obtained = get_lambda_from_csv(species, island, csv_path)
    assert obtained == expected


@pytest.mark.xfail(strict=True, reason="no way of currently testing this")
def test_plot_log_linear_tendency_hash():
    expected_hash = "c43a5c5b80d0497152c38f1e66ed0570"
    png_path = "tests/data/log_linear_tendency.png"
    plot_log_linear_tendency(EXPECTED_PLOT_CONFIG, png_path)
    obtained_hash = _get_hash_from_file(png_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {png_path}"

    expected_hash = "19cdddc69bebc9d0b2827637ada8417d"
    png_path = "tests/data/log_linear_tendency_albatros_guadalupe.png"
    csv_path = "tests/data/input_get_lambda_from_csv.csv"
    OBTAINED_PLOT_CONFIG = get_to_plot_from_island_and_specie(
        expected_dataframe, "Guadalupe", "Albatros", csv_path
    )
    plot_log_linear_tendency(OBTAINED_PLOT_CONFIG, png_path)
    obtained_hash = _get_hash_from_file(png_path)
    assert obtained_hash == expected_hash, f"El hash de la figura {png_path}"


def test_plot_log_linear_tendency_properties():
    png_path = "tests/data/log_linear_tendency.png"
    fig, ax = plot_log_linear_tendency(EXPECTED_PLOT_CONFIG, png_path)
    obtained_xlabel = ax.get_xlabel()
    expected_xlabel = "Season"
    assert obtained_xlabel == expected_xlabel
    obtained_ylabel = ax.get_ylabel()
    expected_ylabel = "Logarithmic number of breeding pairs"
    assert obtained_ylabel == expected_ylabel
    line = ax.lines[0]
    obtained_x_data = line.get_xdata()
    expected_x_data = np.array([2014, 2015, 2016, 2017, 2018, 2019])
    assert (obtained_x_data == expected_x_data).all()
    obtained_y_data = line.get_ydata()
    expected_y_data = np.array([283, 126, 395, 344, 921, 847])
    assert (obtained_y_data == expected_y_data).all()
    obtained_y_scale = ax.get_yscale()
    expected_y_scale = "log"
    assert obtained_y_scale == expected_y_scale


def _get_hash_from_file(png_path):
    file_content = open(png_path, "rb").read()
    obtained_hash = hashlib.md5(file_content).hexdigest()
    return obtained_hash
