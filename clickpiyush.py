import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--desc', default=0, help='Detailed Info.')
def bio(desc):
    click.echo("This is me, and describing self.")


@click.command()
@click.argument('name')
def greet(name):
    click.echo(f"Hello {name}! I'm Piyush.")


cli.add_command(greet)
cli.add_command(bio)

if __name__ == '__main__':
    cli()
