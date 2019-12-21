from connect import ConnectWeb
import click


@click.command()
@click.option('--user_id', prompt=True, help='Student number.')
@click.option('--password', prompt=True, hide_input=True, help='password.')
def check_canceled_class(user_id: str, password: str):

    pass


if __name__ == "__main__":
    check_canceled_class()
