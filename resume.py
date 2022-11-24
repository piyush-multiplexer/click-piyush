import click


@click.command()
def greet():
    click.echo("Hello! I'm Piyush.")


if __name__ == '__main__':
    greet()
