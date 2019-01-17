# coding=utf-8
import click
import math
from functools import (reduce)


def count_allp(size, nb_items):
    return int(math.pow(nb_items, size))


@click.command()
@click.option('--size', default=2, type=int)
@click.option('--count', default=False, is_flag=True)
@click.pass_context
def allp(ctx, size, count):
    """Generate all permutations (with or without repetitions) of the input list"""
    input_list = ctx.obj["list"]
    separator = ctx.obj["separator"]

    if count:
        click.echo(count_allp(size, len(input_list)))
        return

    result = replicate_m(size)(input_list)
    result = [separator.join(x) for x in result]
    result = "\n".join(result)
    click.echo(result)


# GENERIC FUNCTIONS FROM https://rosettacode.org/wiki/Permutations_with_repetitions ------------------------------------


# replicateM :: Int -> [a] -> [[a]]
def replicate_m(n):
    def loop(f):
        def go(x):
            return [[]] if 0 >= x else (
                lift_a_to_list(lambda a, b: [a] + b)(f)(go(x - 1))
            )

        return go(n)

    return lambda f: loop(f)


# liftA2List :: (a -> b -> c) -> [a] -> [b] -> [c]
def lift_a_to_list(f):
    return lambda xs: lambda ys: concat_map(
        lambda x: concat_map(lambda y: [f(x, y)])(ys)
    )(xs)


# concatMap :: (a -> [b]) -> [a] -> [b]
def concat_map(f):
    return lambda xs: (
        reduce(lambda a, b: a + b, map(f, xs), [])
    )
