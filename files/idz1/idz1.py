#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json


def add():
    punkt = input("Пункт назначения: ")
    nomer = input("Номер поезда: ")
    time = input("Время отправления: ")

    return {
        'punkt': punkt,
        'nomer': nomer,
        'time': time,
    }


def show(info):
    if info:
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
            )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "No",
                "Город прибытия",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)

        for idx, station in enumerate(info, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                    idx,
                    station.get('punkt', ''),
                    station.get('nomer', ''),
                    station.get('time', '')
                )
            )
        print(line)

    else:
        print("Список маршрутов пуст")


def select(info, name_station):
    result = []
    for station in info:
        if station.get('punkt', '') == name_station:
            result.append(station)
    return result


def save_stations(file_name, info):

    with open(file_name, "w", encoding="utf-8") as fout:
        json.dump(info, fout, ensure_ascii=False, indent=4)


def load_stations(file_name):
    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    stations = []

    while True:
        command = input(">>> ").lower()

        if command == "exit":
            break

        elif command == "add":
            station = add()
            stations.append(station)
            if len(stations) > 1:
                stations.sort(key=lambda item: item.get('time', ''))

        elif command == "show":
            show(stations)

        elif command.startswith("select "):
            parts = command.split(maxsplit=1)
            select_punkt = parts[1]
            selected = select(stations, select_punkt)
            show(selected)

        elif command.startswith("save "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            save_stations(file_name, stations)

        elif command.startswith("load "):
            parts = command.split(maxsplit=1)
            file_name = parts[1]
            stations = load_stations(file_name)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить станцию")
            print("show - вывести список станций;")
            print("select <название> - запросить станцию по названию;")
            print("help - отобразить справку;")
            print("load - загрузить данные из файла;")
            print("save - сохранить данные в файл;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
