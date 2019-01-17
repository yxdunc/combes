import os
import click


def is_stdin_term():
    if not os.isatty(0):
        return False
    return True


def get_piped_stdin():
    if not is_stdin_term():
        return click.get_text_stream('stdin').read()

    return None


if __name__ == '__main__':
    print "STD_IN is coming from term: {}".format(is_stdin_term())
