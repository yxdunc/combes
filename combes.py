import click

from cmd_perm import perm
from cmd_comb import comb
from cmd_subl import subl
from cmd_allp import allp
from helper_stdin import get_piped_stdin


@click.group()
@click.option('--list-string', default=None, type=str)
@click.option('--list-file', default=None, type=click.File('rb'))
@click.option('--list-separator', default=",", type=str)
@click.pass_context
def cli(ctx, list_string, list_file, list_separator):
    std_in = get_piped_stdin()

    number_of_inputs = (list_file is not None) + (list_string is not None) + (std_in is not None)
    if number_of_inputs == 0:
        click.echo("[Error] You didn't provide a list.", err=True)
        return 1
    elif number_of_inputs > 1:
        click.echo("[Warning] You provided multiple lists (stdin / list-file / list-string)", err=True)
        click.echo("[Warning] | list were appended using: {}".format(list_separator), err=True)

        lists = [list_file, list_string, std_in]
        ctx.obj["list"] = list_separator.join(filter(None, lists))
    else:
        ctx.obj["list"] = list_string or list_file or std_in

    ctx.obj["list"] = ctx.obj["list"].strip().split(list_separator)
    ctx.obj["separator"] = list_separator
    return 0


if __name__ == '__main__':
    cli.add_command(perm)
    cli.add_command(comb)
    cli.add_command(subl)
    cli.add_command(allp)
    cli(obj={})
