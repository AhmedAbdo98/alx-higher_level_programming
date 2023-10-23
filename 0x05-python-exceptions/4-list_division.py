#!/usr/bin/python3
def list_division(my _list_1, my_list_2, list_lenght):
    new_list = []
    for i in range(list_lenght):
    try:
        new_list.append(my _list_1[i] / my_list_2[i])
    except ZeroDivisionError:
        new_list.append(0)
        print('division by 0')
        continue
    except IndexError:
        new_list.append(0)
        print('out of range')
        continue
    except TypeError:
        new_list.append(0)
        new_list.append('wrong type')
        continue
    finally:
    pass
    return new_list
