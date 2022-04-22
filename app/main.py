import click
from animals import speak


@click.command()
@click.option("--animal_type", help="The type of animal to hear a noise from")
@click.option("--animal_name", help="The animal's name")
def main(animal_type: str, animal_name: str):
    noise = speak(animal_type)
    click.echo(f"{animal_name} says {noise}")


if __name__ == "__main__":
    main()
