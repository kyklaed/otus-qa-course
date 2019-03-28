import pytest


class Test1:
    def test_to_int(self, start_module, test_to_int):
        print("check int")
        assert type(test_to_int) == int

    def test_to_float(self, test_to_float):
        print("check int")
        assert type(test_to_float) == float

    def test_to_list(self, test_to_list):
        print("check list")
        assert type(test_to_list) == list

    def test_to_string(self, test_to_string):
        print("check string")
        assert type(test_to_string) == str

    def test_to_tuple(self, test_to_tuple):
        print("check tuple")
        assert type(test_to_tuple) == tuple


class Test2:
    def test_to_count_in_list(self, test_to_list):
        print("check count")
        assert 5 == len(test_to_list)

    def test_check_content(self, test_check_content):
        print("check content")
        assert 1 in test_check_content.keys()

    def test_append_in_list(self, test_append_in_list):
        print("check append")
        assert 9 == len(test_append_in_list)

    def test_subtraction(self, test_subtraction):
        assert test_subtraction[0] - test_subtraction[1] == 0

    def test_addition_row(self, test_addition_row):
        assert len(test_addition_row[0] + test_addition_row[1]) == 8

