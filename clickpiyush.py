import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--name', prompt='Identify youself by name')
def greet(name):
    """What is this tool"""
    click.echo(
        f"Hello {name}! This is Command Line Interface which gives information of maker named Piyush.")


@click.command()
@click.option('--desc', default=0, help='Detailed Info.')
def bio(desc):
    """Basic Bio"""
    click.echo(f'decc {desc}')
    click.echo("This is me, and describing self.")


@click.command()
def age():
    """Get Age"""
    click.echo("I'm 2X years older, shouldn't be matter.")


@click.command()
def blog():
    """Get My blog URL"""
    blog_url = "https://blog.thesourcepedia.org/"
    click.echo(f"{blog_url}   Wanna visit [y/n]: ", nl=False)
    c = click.getchar()
    click.echo(c)
    if c == 'y':
        click.echo("Launching Piyush's Blog")
        click.launch(blog_url)


# @click.command()
# @click.Choice()
cli.add_command(greet)
cli.add_command(bio)
cli.add_command(age)
cli.add_command(blog)

if __name__ == '__main__':
    cli()
