#!/usr/bin/env python
import click
import os
from nlppln.utils import create_dirs


@click.command()
@click.argument('in_file', type=click.File(encoding='utf-8'))
@click.option('--out_dir', '-o', default=os.getcwd(), type=click.Path())
def remove_newlines(in_file, out_dir):
    create_dirs(out_dir)

    text = in_file.read()
    text = text.replace(u'\n', u'')
    text = text.strip()

    stdout_text = click.get_text_stream('stdout')
    stdout_text.write(text)


if __name__ == '__main__':
    remove_newlines()
