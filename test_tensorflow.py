#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import tensorflow as tf

def main():
    hello = tf.constant('hello, tensorflow')
    sess = tf.Session()
    print sess.run(hello)

    a = tf.constant(10)
    b = tf.constant(32)
    print sess.run(a+b)

if __name__ == '__main__':
    main()

