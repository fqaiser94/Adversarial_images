# this script is to generate add adversarial images

import argparse

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir', type=str,
                    default='/tmp/tensorflow/mnist/input_data',
                    help='Directory for storing input data')

FLAGS, unparsed = parser.parse_known_args()

# read in mnist data
mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)

