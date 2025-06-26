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

def test_positive(x, expected_result):
    assert Doodler(0, 100, 100).set_x(x) == expected_result


@pytest.mark.parametrize('x, expected_result',
                         [
                             ('', TypeError),
                             ([55], TypeError),
                             ('0', TypeError),
                         ])

def test_negative(x, expected_result):
    with pytest.raises(expected_result):
        Doodler(0, 100, 100).set_x(x)


#Тест 2
@pytest.mark.parametrize('value, expected_result',
                         [
                             (50, 50),
                             (20, 20),
                             (10, 10)
                         ])

def test_positive(value, expected_result):
    assert Doodler(0, 100, 100).set_y_speed(value) == expected_result


@pytest.mark.parametrize('value, expected_result',
                         [
                             ('', TypeError),
                             ([3, 5], TypeError),
                             ('0', TypeError),
                         ])

def test_negative(value, expected_result):
    with pytest.raises(expected_result):
        Doodler(0, 100, 100).set_y_speed(value)


#Тест 3

@pytest.mark.parametrize('platforms, expected_result',
                         [
                             ([20], [20]),
                             ([18], [18]),
                             ([2], [2])
                         ])

def test_positive(platforms, expected_result):
    assert Doodler(0, 100, 100).check_collision(platforms) == expected_result



@pytest.mark.parametrize('value, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                         ])

def test_negative(value, expected_result):
    with pytest.raises(expected_result):
        Doodler(0, 100, 100).set_y_speed(value)


#Тест 4

@pytest.mark.parametrize('platform_count, expected_result',
                         [
                             (13, [13]),
                             (5, [5]),
                             (10, [10])
                         ])

def test_positive(platform_count, expected_result):
    assert Field(0).generate_platforms(platform_count) == expected_result


@pytest.mark.parametrize('platform_count, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             (3.14, TypeError)
                         ])

def test_negative(platform_count, expected_result):
    with pytest.raises(expected_result):
        Field(0).generate_platforms(platform_count)

#Тест 5
@pytest.mark.parametrize('diff, expected_result',
                         [
                             (13, 13),
                             (5, 5),
                             (13, 13)
                         ])

def test_positive(diff, expected_result):
    assert Field(0).scroll_screen() == expected_result


@pytest.mark.parametrize('diff, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             (3.14, TypeError)
                         ])

def test_negative(diff, expected_result):
    with pytest.raises(expected_result):
        Field(0).scroll_screen()


#Тест 7
@pytest.mark.parametrize('score, expected_result',
                         [
                             (13, 13),
                             (5, 5),
                             (22, 22)
                         ])

def test_positive(score, expected_result):
    assert Game().game_over(score) == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             ([0], TypeError)
                         ])

def test_negative(score, expected_result):
    with pytest.raises(expected_result):
        Game().game_over(score)

#Тест 8
@pytest.mark.parametrize('running, expected_result',
                         [
                             (True, True),
                             (False, False),
                             (True, True)
                         ])

def test_positive(running, expected_result):
    assert Game().get_is_running() == expected_result


@pytest.mark.parametrize('running, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError)
                         ])

def test_negative(running, expected_result):
    with pytest.raises(expected_result):
        Game().get_is_running()


#Тест 9

@pytest.mark.parametrize('score, expected_result',
                         [
                             (30, 30),
                             (2, 2),
                             (13, 13)
                         ])

def test_positive(score, expected_result):
    assert Score().get_score() == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             ('', TypeError),
                             ('0', TypeError),
                             ([34, 33], TypeError)
                         ])

def test_negative(score, expected_result):
    with pytest.raises(expected_result):
        Score().get_score()

#Тест 10
@pytest.mark.parametrize('records, expected_result',
                         [
                             ('30', '30'),
                             ('2', '2'),
                             ('13', '13')
                         ])

def test_positive(records, expected_result):
    assert StorageManager().read() == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             (2, TypeError),
                             (3, TypeError)
                         ])

def test_negative(score, expected_result):
    with pytest.raises(expected_result):
        StorageManager().read()

# Тест 11
@pytest.mark.parametrize('records, expected_result',
                         [
                             ('18', '18'),
                             ('5', '5'),
                             ('17', '17')
                         ])

def test_positive(records, expected_result):
    assert StorageManager().__init__() == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             (24, TypeError),
                             (38, TypeError)
                         ])

def test_negative(score, expected_result):
    with pytest.raises(expected_result):
        StorageManager().__init__()

# Тест 12
@pytest.mark.parametrize('value, expected_result',
                         [
                             ('18', '18'),
                             (5, 5),
                             ('17', '17')
                         ])

def test_positive(value, expected_result):
    assert StorageManager().write(value) == expected_result


@pytest.mark.parametrize('value, expected_result',
                         [
                             (24.5, TypeError),
                             ([23], TypeError)
                         ])

def test_negative(value, expected_result):
    with pytest.raises(expected_result):
        StorageManager().write(value)

# Тест 13

@pytest.mark.parametrize('records, expected_result',
                         [
                             ('3', '3'),
                             ('8', '8'),
                             ('34', '34')
                         ])

def test_positive(records, expected_result):
    assert StorageManager().get_records() == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             (24, TypeError),
                             (38, TypeError)
                         ])

def test_negative(score, expected_result):
    with pytest.raises(expected_result):
        StorageManager().get_records()

# Тест 14

@pytest.mark.parametrize('records, expected_result',
                         [
                             (True, True),
                             (False, False)
                         ])

def test_positive(records, expected_result):
    assert Game().__init__() == expected_result


@pytest.mark.parametrize('score, expected_result',
                         [
                             (52, TypeError),
                             (68, TypeError)
                         ])

def test_negative(score, expected_result):
    with pytest.raises(expected_result):
        Game().__init__()

# Тест 15
@pytest.mark.parametrize('type, expected_result',
                         [
                             ('normal', 'normal'),
                             ('broken', 'broken')
                         ])

def test_positive(type, expected_result):
    assert AbstractPlatform(85, 15, None).get_type() == expected_result


@pytest.mark.parametrize('type, expected_result',
                         [
                             (3, TypeError),
                             (15, TypeError)
                         ])

def test_negative(type, expected_result):
    with pytest.raises(expected_result):
        AbstractPlatform(85, 15, None).get_type()

#Тест 16
@pytest.mark.parametrize('speed, expected_result',
                         [
                             (1, 1),
                             (102, 102)
                         ])

def test_positive(speed, expected_result):
    assert Background().__init__() == expected_result


@pytest.mark.parametrize('speed, expected_result',
                         [
                             (54.5, TypeError),
                             (32,86, TypeError)
                         ])

def test_negative(speed, expected_result):
    with pytest.raises(expected_result):
        Background().__init__()
