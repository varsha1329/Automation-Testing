def chars_string_together(x, y):
    new_x=y[:2] + x[2:]
    new_y=x[:2] + y[2:]
    return new_x + ' ' + new_y
print(chars_string_together('abc', 'xyz'))    