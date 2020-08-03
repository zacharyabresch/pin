"""CLI Module"""
import click

from .modules.logger import logger
from .modules.client import Client


@click.group()
@click.pass_context
def cli(ctx):
    """CLI command group"""
    ctx.obj = Client()


@cli.command()
@click.pass_context
def init(ctx):
    """Initializes client"""


@cli.command()
@click.pass_context
def add(ctx):
    """Adds a bookmark"""


@cli.command()
@click.pass_context
def list(ctx):
    """Lists bookmarks"""


@cli.command()
@click.pass_context
def delete(ctx):
    """Deletes a bookmark"""


@cli.command()
@click.pass_context
def edit(ctx):
    """Edits a bookmark"""
