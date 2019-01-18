import click
import itertools
import math


def count_comb(size, nb_items):
    return math.factorial(nb_items) / (math.factorial(size) * math.factorial(nb_items - size))

@click.command()
@click.option('--size', default=2, type=int)
@click.option('--count', default=False, is_flag=True)
@click.pass_context
def comb(ctx, size, count):
    """Generate the combinations of the input list"""
    input_list = ctx.obj["list"]
    list_separator = ctx.obj["separator"]

    if count:
        click.echo(count_comb(size, len(input_list)))
        return

    for each in itertools.combinations(input_list, r=size):
        click.echo(list_separator.join(each))
