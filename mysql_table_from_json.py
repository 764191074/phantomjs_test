#! /bin/usr/env python3
# coding=utf-8
import logging
import traceback
logger = logging.getLogger()


def get_sql(table_name, j):
    '''
        CREATE TABLE person (
        number INT(11),
        name VARCHAR(255),
        birthday DATE
        );
    :return:
    '''
    str_tou = 'CREATE TABLE {} ( \n id INT NOT NULL AUTO_INCREMENT,\n'.format(table_name)
    str_wei = 'PRIMARY KEY ( id ) \n );'

    str_int = '{} INT({}),\n'
    str_varchar = '{} VARCHAR({}),\n'
    str_pre = ''

    return_str = str_tou
    for i in j.items():
        if len(i[1]) >= 50:
            return_str += str_varchar.format(i[0], 225)
        else:
            return_str += str_varchar.format(i[0], 50)
    return_str += str_wei
    print(return_str)


if __name__ == '__main__':
    get_sql()
