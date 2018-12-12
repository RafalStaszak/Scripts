import tensorflow as tf
import argparse


def show_variables(checkpoint_dir):
    with tf.Session() as sess:
        checkpoint = tf.train.get_checkpoint_state(checkpoint_dir)
        print("Checkpoint model path: %s" % checkpoint.model_checkpoint_path)
        for var_name, _ in tf.contrib.framework.list_variables(checkpoint_dir):
            print(var_name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--checkpoint_dir', help='Checkpoint directory')
    args = parser.parse_args()

    tf.logging.set_verbosity(tf.logging.ERROR)

    show_variables(args.checkpoint_dir)


if __name__ == '__main__':
    main()
