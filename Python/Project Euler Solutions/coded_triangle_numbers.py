# -*- coding: utf-8 -*-



def triangle_number(n):
    return int( round( 0.5 * n * (n + 1) )   )


class TriangleIterator:
    def __iter__(self):
        self.index = 1
        return self
    
    def __next__(self):
        t = triangle_number(self.index)
        self.index += 1
        return t
    


def initialize_array(filename):
    arr = []
    with open(filename) as f:
        data = f.read()
        data = data.replace('\"','')
        arr = data.split(",")
    return arr



def word_value(word):
    value = 0
    for c in word:
        lowerC = c.lower()
        i = ord(lowerC) - 96
        value = value + i
    return value




def test_if_triangular_value(value):
    for triangle_value in TriangleIterator():
        if triangle_value > value:
            return False
        if triangle_value == value:
            return True



def evaluate_if_word_value_is_triangular(word):
    return test_if_triangular_value(    word_value(word)    )
        


def count_triangular_words_in_word_file(filename):
    words = initialize_array(filename)
    count_of_triangle_words = 0
    for word in words:
        if test_if_triangular_value(word):
            count_of_triangle_words += 1
    return count_of_triangle_words



print(    count_triangular_words_in_word_file("words.txt")      )