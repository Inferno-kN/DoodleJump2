import pytest
from refactoring.source.AbstractPlatform import AbstractPlatform
from refactoring.source.Doodler import Doodler
from refactoring.source.Field import Field
from refactoring.source.Game import Game
from refactoring.source.Score import Score
from refactoring.source.StorageManager import StorageManager
from src.background import Background


#Тест 1
@pytest.mark.parametrize('x, expected_result',
                         [
                             (1, 1),
                             (3, 3),
                             (10, 10)
                         ])

def test_set_x_positive(x, expected_result):
    doodler = Doodler(0, 100, 100)
    doodler.set_x(x)
    x, y = doodler.get_position()
    assert x == expected_result


@pytest.mark.parametrize('x, expected_result',
                         [
                             ('', TypeError),
                             ([55], TypeError),
                             ('0', TypeError),
                         ])

def test_set_x_negative(x, expected_result):
    with pytest.raises(expected_result):
        Doodler(0, 100, 100).set_x(x)


#Тест 2

@pytest.mark.parametrize('value, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                         ])

def test_set_y_speed_negative(value, expected_result):
    with pytest.raises(expected_result):
        Doodler(0, 100, 100).set_y_speed(value)


#Тест 3 -

@pytest.mark.parametrize('platform_count, expected_result',
                         [
                             (13, [13]),
                             (5, [5]),
                             (10, [10])
                         ])

def test_generate_platforms_positive(platform_count, expected_result):
    assert Field(0).generate_platforms(platform_count) == expected_result


@pytest.mark.parametrize('platform_count, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             (3.14, TypeError)
                         ])

def test_generate_platforms_negative(platform_count, expected_result):
    with pytest.raises(expected_result):
        Field(0).generate_platforms(platform_count)


#Тест 4 -
@pytest.mark.parametrize('score, expected_result',
                         [
                             (13, 13),
                             (5, 5),
                             (22, 22)
                         ])

def test_game_over_positive(score, expected_result):
    assert Game().game_over(score) == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             ([0], TypeError)
                         ])

def test_game_over_negative(score, expected_result):
    with pytest.raises(expected_result):
        Game().game_over(score)

#Тест 5 -
@pytest.mark.parametrize('running, expected_result',
                         [
                             (True, True),
                             (False, True),
                             (True, True)
                         ])

def test_get_is_running_positive(running, expected_result):
    assert Game().get_is_running() == expected_result


@pytest.mark.parametrize('running, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError)
                         ])

def test_get_is_running_negative(running, expected_result):
    with pytest.raises(expected_result):
        Game().get_is_running()



# Тест 6 -
@pytest.mark.parametrize('type, expected_result',
                         [
                             ('normal', 'normal'),
                             ('broken', 'broken')
                         ])

def test_get_type_positive(type, expected_result):
    assert AbstractPlatform(85, 15, None).get_type() == expected_result


@pytest.mark.parametrize('type, expected_result',
                         [
                             (3, TypeError),
                             (15, TypeError)
                         ])

def test_get_type_negative(type, expected_result):
    with pytest.raises(expected_result):
        AbstractPlatform(85, 15, None).get_type()
