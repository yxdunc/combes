import click
import itertools
import math


def count_perm(size, nb_items):
    if size == nb_items:
        return math.factorial(nb_items)
    return math.factorial(nb_items) / math.factorial(nb_items - size)


@click.command()
@click.option('--count', default=False, is_flag=True)
@click.option('--size', default=2, type=int)
@click.pass_context
def perm(ctx, size, count):
    """Generate the permutations of the input list"""
    input_list = ctx.obj["list"]
    list_separator = ctx.obj["separator"]

    if size > len(input_list):
        click.echo("[Warming] Can't generate permutations without repetitions if size is", err=True)
        click.echo("[Warming] | greater than number of elements.", err=True)
        click.echo("[Warming] | To generate permutations with repetitions use `allp`", err=True)

    if count:
        click.echo(count_perm(size, len(input_list)))
        return

    for each in itertools.permutations(input_list, size):
        click.echo(list_separator.join(each))
