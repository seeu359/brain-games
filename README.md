### Hexlet tests and linter status:
[![Actions Status](https://github.com/seeu359/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/seeu359/python-project-lvl1/actions)
<a 
href="https://codeclimate.com/github/codeclimate/codeclimate/maintainability"><img 
src="https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability" 
/></a>


Проект Brain-games - мой первый проект. Его главная цель - построение правильной архитектуры программы, выделение общей логики и вынесение ее в отдельные модули. Проект объединет в себе 5 мини-игр, в которых нужно решить простейшие математические задачи. Краткие инструкции к каждой игре даны ниже.

Для установки:
1) Клонуруем репозиторий https://github.com/seeu359/python-project-lvl1.git 
2) Выполняем команду Make install

1. Brain-even. Игра, в которой нужно определить четное число или нет, ответив соответственно "yes" или "no". Пример:

<a href="https://asciinema.org/a/501663" target="_blank"><img src="https://asciinema.org/a/501663.svg" /></a>

2. Brain-calc. Вторая мини-игра, в которой необходимо вычислить значение простейшего арифметического примера и ввести ответ в поле ввода. Пример:

<a href="https://asciinema.org/a/502438" target="_blank"><img src="https://asciinema.org/a/502438.svg" /></a>

3. Brain-gcd. В третьей игре нужно определить наибольший общий делитель двух чисел:

<a href="https://asciinema.org/a/502440" target="_blank"><img src="https://asciinema.org/a/502440.svg" /></a>

4. Brain-progression. Перед вами арифметическая прогрессия. Ваша задача найти число, которое выпало(замененно на две точки), и вписать его в поле ввода. Смотрим:

<a href="https://asciinema.org/a/502593" target="_blank"><img src="https://asciinema.org/a/502593.svg" /></a>

5. Brain-prime. Заключительная игра, в которой нужно определить просто число или нет (https://ru.wikipedia.org/wiki/Простое_число). Вариантов ответов: "yes - если число простое, "no" - если нет.

<a href="https://asciinema.org/a/502595" target="_blank"><img src="https://asciinema.org/a/502595.svg" /></a>

Команды в Makefile: 
1) install  - установка/отладка пакета в систему. Выполнит:
        poetry install
        poetry build
        python3 -m pip install --user --force-reinstall dist/*.whl
        
2) publish - выполнит: poetry publish --dry-run
3) lint - Команда для проверки линтером всех файлов в пакете. Выполнит: poetry run flake8 brain_games
