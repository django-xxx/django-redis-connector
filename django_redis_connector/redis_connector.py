# -*- coding: utf-8 -*-

import redis_extensions as redis


def redis_conf(conf):
    conf.update({
        'host': conf.get('HOST', 'localhost'),
        'port': conf.get('PORT', 6379),
        'password': '{}:{}'.format(conf.get('USER', ''), conf.get('PASSWORD', '')) if conf.get('USER') else '',
        'db': conf.get('db', 0),
    })
    return conf


def connector(conf):
    return redis.StrictRedisExtensions(connection_pool=redis.ConnectionPool(**redis_conf(conf)))


redis_connect = connector
