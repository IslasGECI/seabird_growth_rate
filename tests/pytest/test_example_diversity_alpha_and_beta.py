import lambdas_aves_marinas as lam


def test_temporada():
    expected_season = 2019
    obtained_season = lam.temporada()
    assert expected_season == obtained_season


def test_todos_nidos():
    expected_nest = 1258
    obtained_nest = lam.todos_nidos()
    assert expected_nest == obtained_nest


def test_isla():
    expected_island = "Todos Santos"
    obtained_island = lam.isla()
    assert expected_island == obtained_island


def test_nidos_especie():
    expected_nests = 723
    obtained_nests = lam.nidos_especie()
    assert expected_nests == obtained_nests


def test_especie():
    expected_species = "Brown Pelican"
    obtained_species = lam.especie()
    assert expected_species == obtained_species


def test_proporcion():
    expected_ratio = 0.57
    obtained_ratio = lam.proporcion()
    assert expected_ratio == obtained_ratio


def test_isla_de_interes():
    expected_island = "Coronado"
    obtained_island = lam.isla_de_interes()
    assert expected_island == obtained_island


def test_isla_de_referencia():
    expected_island = "Asuncion"
    obtained_island = lam.isla_de_referencia()
    assert expected_island == obtained_island


def test_a():
    expected_a_value = 5
    obtained_a_value = lam.a()
    assert expected_a_value == obtained_a_value


def test_b():
    expected_b_value = 2
    obtained_b_value = lam.b()
    assert expected_b_value == obtained_b_value


def test_c():
    expected_c_value = 6
    obtained_c_value = lam.c()
    assert expected_c_value == obtained_c_value


def test_beta_example():
    expected_beta = 0.44
    obtained_beta = lam.beta_example()
    assert expected_beta == obtained_beta
