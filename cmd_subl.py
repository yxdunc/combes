# coding=utf-8
import click


def count_subl(size):
    return (size * (size - 1)) / 2


@click.command()
@click.option('--count', default=False, is_flag=True)
@click.pass_context
def subl(ctx, count):
    """Generate the sub-lists of the input list"""
    input_list = ctx.obj["list"]
    separator = ctx.obj["separator"]

    if count:
        click.echo(count_subl(len(input_list)))
        return

    for i in range(len(input_list) + 1):
        for j in range(i + 1, len(input_list) + 1):
            sub_list = input_list[i:j]
            sub_list = separator.join(sub_list)
            click.echo(sub_list)
