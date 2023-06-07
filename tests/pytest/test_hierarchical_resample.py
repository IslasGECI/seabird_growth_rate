import pytest

from seabird_growth_rate import (
    get_average_lambda_from_group,
    get_bootstraped_lambda_from_group,
    get_group_list,
    get_island_count_from_species,
    get_resampled_lambda_from_group,
    get_resampled_species_from_group,
    get_species_count_from_group,
    get_species_list_from_group,
    resample_lambdas_by_species,
)


def test_get_group_list():
    """Test that the group list is correctly extracted from the csv."""
    csv_path = "tests/data/input_hierarchical_resample.csv"
    obtained_list = get_group_list(csv_path)
    expected_list = ["Charadriiformes", "Pelecaniformes"]
    assert set(obtained_list) == set(expected_list)


def test_get_species_list_from_group():
    """Test that the species list is correctly extracted from the order."""
    group = "Charadriiformes"
    csv_path = "tests/data/input_hierarchical_resample.csv"
    obtained_list = get_species_list_from_group(group, csv_path)
    expected_list = ["Western Gull", "Cassin's Auklet", "Caspian Tern"]
    assert set(obtained_list) == set(expected_list)
    group = "Pelecaniformes"
    obtained_list = get_species_list_from_group(group, csv_path)
    expected_list = ["Brown Pelican"]
    assert set(obtained_list) == set(expected_list)


def test_get_island_count_from_species():
    """Test that the island count is correctly extracted from the order and species."""
    species = "Western Gull"
    csv_path = "tests/data/input_hierarchical_resample.csv"
    obtained_count = get_island_count_from_species(species, csv_path)
    expected_count = 1
    assert obtained_count == expected_count
    species = "Brown Pelican"
    obtained_count = get_island_count_from_species(species, csv_path)
    expected_count = 3
    assert obtained_count == expected_count


def test_resample_lambdas_by_species():
    """Test that the resampling is correctly done."""
    csv_path = "tests/data/input_hierarchical_resample.csv"
    species = "Caspian Tern"
    obtained_lambdas = resample_lambdas_by_species(species, csv_path=csv_path)
    expected_lambdas = [0.61, 1.21]
    assert (obtained_lambdas == expected_lambdas).all()
    species = "Cassin's Auklet"
    obtained_lambdas = resample_lambdas_by_species(species, csv_path=csv_path)
    expected_lambdas = [1.26, 1.14, 1.26]
    assert (obtained_lambdas == expected_lambdas).all()
    species = "Western Gull"
    obtained_lambdas = resample_lambdas_by_species(species, csv_path=csv_path)
    expected_lambdas = [1.12]
    assert (obtained_lambdas == expected_lambdas).all()
    species = "Brown Pelican"
    obtained_lambdas = resample_lambdas_by_species(species, csv_path=csv_path)
    expected_lambdas = [1.19, 1.28, 1.19]
    assert (obtained_lambdas == expected_lambdas).all()
    species = "Brown Pelican"
    obtained_lambdas = resample_lambdas_by_species(species, seed=1, csv_path=csv_path)
    expected_lambdas = [1.28, 1.19, 1.19]
    assert (obtained_lambdas == expected_lambdas).all()


def test_get_resampled_species_from_group():
    """Test that the species list is correctly extracted from the order."""
    group = "Charadriiformes"
    csv_path = "tests/data/input_hierarchical_resample.csv"
    seed = 1
    obtained_list = get_resampled_species_from_group(group, seed=seed, csv_path=csv_path)
    expected_list = ["Cassin's Auklet", "Caspian Tern", "Caspian Tern"]
    assert (obtained_list == expected_list).all()
    seed = 2
    obtained_list = get_resampled_species_from_group(group, seed=seed, csv_path=csv_path)
    expected_list = ["Caspian Tern", "Cassin's Auklet", "Caspian Tern"]
    assert (obtained_list == expected_list).all()
    group = "Pelecaniformes"
    obtained_list = get_resampled_species_from_group(group, seed=seed, csv_path=csv_path)
    expected_list = ["Brown Pelican"]
    assert (obtained_list == expected_list).all()


def test_get_resampled_lambda_from_group():
    """Test that the bootstrapped lambda is correctly extracted from the order."""
    group = "Charadriiformes"
    csv_path = "tests/data/input_hierarchical_resample.csv"
    seed = 1
    obtained_lambda = get_resampled_lambda_from_group(group, seed=seed, csv_path=csv_path)
    expected_lambda = [1.14, 1.14, 1.26, 1.21, 1.21, 0.61, 1.21]
    assert obtained_lambda == expected_lambda
    seed = 3
    obtained_lambda = get_resampled_lambda_from_group(group, seed=seed, csv_path=csv_path)
    expected_lambda = [1.12, 1.21, 0.61, 1.79, 1.79, 1.79]
    assert obtained_lambda == expected_lambda
    group = "Pelecaniformes"
    obtained_lambda = get_resampled_lambda_from_group(group, seed=seed, csv_path=csv_path)
    expected_lambda = [1.19, 1.21, 1.21]
    assert obtained_lambda == expected_lambda


def test_get_average_lambda_from_group():
    """Test that the bootstrapped lambda is correctly extracted from the order."""
    group = "Charadriiformes"
    csv_path = "tests/data/input_hierarchical_resample.csv"
    seed = 1
    obtained_lambda = get_average_lambda_from_group(group, seed=seed, csv_path=csv_path)
    expected_lambda = 1.1114
    assert obtained_lambda == pytest.approx(expected_lambda, 1e-4)
    seed = 3
    obtained_lambda = get_average_lambda_from_group(group, seed=seed, csv_path=csv_path)
    expected_lambda = 1.385
    assert obtained_lambda == pytest.approx(expected_lambda, 1e-4)
    group = "Pelecaniformes"
    obtained_lambda = get_average_lambda_from_group(group, seed=seed, csv_path=csv_path)
    expected_lambda = 1.2033
    assert obtained_lambda == pytest.approx(expected_lambda, 1e-4)


def test_get_boostraped_lambda_from_group():
    """Test that the bootstrapped lambda is correctly extracted from the order."""
    group = "Charadriiformes"
    seed = 1
    N = 20
    csv_path = "tests/data/input_hierarchical_resample.csv"
    obtained_lambda = get_bootstraped_lambda_from_group(group, seed=seed, N=N, csv_path=csv_path)
    expected_lambda = [
        1.2971,
        1.1114,
        1.0257,
        1.385,
        1.522,
        1.262,
        1.0883,
        1.1683,
        1.5037,
        1.0150,
        1.335,
        1.1424,
        1.5257,
        1.165,
        1.072,
        1.1285,
        1.6014,
        1.286,
        1.1083,
        1.3571,
    ]
    assert obtained_lambda == pytest.approx(expected_lambda, 1e-4)
    group = "Pelecaniformes"
    N = 10
    csv_path = "tests/data/input_hierarchical_resample.csv"
    obtained_lambda = get_bootstraped_lambda_from_group(group, seed=seed, N=N, csv_path=csv_path)
    expected_lambda = [
        1.1966,
        1.25,
        1.1966,
        1.2033,
        1.1966,
        1.2266,
        1.25,
        1.22,
        1.2033,
        1.22,
    ]
    assert obtained_lambda == pytest.approx(expected_lambda, 1e-4)


def test_get_species_count_from_group():
    """Test that the species count is correctly extracted from the order."""
    csv_path = "tests/data/input_hierarchical_resample.csv"
    group = "Charadriiformes"
    obtained_count = get_species_count_from_group(group, csv_path=csv_path)
    expected_count = 3
    assert obtained_count == expected_count
    group = "Pelecaniformes"
    obtained_count = get_species_count_from_group(group, csv_path=csv_path)
    expected_count = 1
    assert obtained_count == expected_count
