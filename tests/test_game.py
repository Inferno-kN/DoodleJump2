import pytest
from src.AbstractPlatform import AbstractPlatform
from src.Doodler import Doodler
from src.Field import Field
from src.Game import Game
from src.Score import Score
from src.StorageManager import StorageManager
from src.Background import Background


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



@pytest.mark.parametrize('x, expected_result',
                         [
                             (1, 1),
                             (3, 3),
                             (10, 10)
                         ])

def test_set_y_speed_positive(x, expected_result):
    doodler = Doodler(0, 100, 100)
    doodler.set_y_speed(x)
    assert doodler.get_y_speed() == expected_result


@pytest.mark.parametrize('platform_count, expected_result',
                         [
                             (13, 15),
                             (5, 7),
                             (10, 12)
                         ])
def test_generate_platforms_positive(platform_count, expected_result):
    platforms = Field(0).generate_platforms(platform_count)
    assert isinstance(platforms, list)
    assert len(platforms) == expected_result


@pytest.mark.parametrize('platform_count, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             (3.14, TypeError)
                         ])

def test_generate_platforms_negative(platform_count, expected_result):
    with pytest.raises(expected_result):
        Field(0).generate_platforms(platform_count)


@pytest.mark.parametrize('score, expected_result',
                         [
                             (13, 13),
                             (5, 5),
                             (22, 22)
                         ])

def test_game_over_positive(score, expected_result):
    assert Game().end_game(score) == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             ([0], TypeError)
                         ])

def test_game_over_negative(score, expected_result):
    with pytest.raises(expected_result):
        Game().end_game(score)


@pytest.mark.parametrize('running, expected_result',
                         [
                             (True, True),
                             (False, True),
                             (True, True)
                         ])

def test_get_is_running_positive(running, expected_result):
    assert Game().is_running() == expected_result


@pytest.mark.parametrize('running, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError)
                         ])

def test_get_is_running_negative(running, expected_result):
    game = Game()
    game.set_running(running)
    with pytest.raises(expected_result):
        game.is_running()



# Тест 6 -
@pytest.mark.parametrize('type_value, expected_result',
                         [
                             ('normal', 'normal'),
                             ('broken', 'broken')
                         ])
def test_get_type_positive(type_value, expected_result):
    platform = AbstractPlatform(10, 20)
    platform._AbstractPlatform__type = type_value
    assert platform.get_type() == expected_result


@pytest.mark.parametrize('type_value, expected_exception',
                         [
                             (3, TypeError),
                             (15, TypeError)
                         ])
def test_get_type_negative(type_value, expected_exception):
    platform = AbstractPlatform(85, 15, None)
    platform.set_type(type_value)
    with pytest.raises(expected_exception):
        platform.get_type()


