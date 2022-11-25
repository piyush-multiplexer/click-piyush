import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--name', prompt='Identify youself by name')
def greet(name):
    click.echo(
        f"Hello {name}! This is Command Line Interface which gives information of maker named Piyush.")


@click.command()
@click.option('--desc', default=0, help='Detailed Info.')
def bio(desc):
    click.echo("This is me, and describing self.")


# @click.command()
# @click.Choice()
cli.add_command(greet)
cli.add_command(bio)

if __name__ == '__main__':
    cli()
