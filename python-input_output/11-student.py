#!/usr/bin/python3
"""
Write a class Student that defines a student by:
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        info_student = {}
        for i in attrs:
            if i in self.__dict__:
                info_student[i] = self.__dict__[i]
        return info_student

    def reload_from_json(self, json):
        for key, value in json.items():
            self.__dict__[key] = value
