import re


from bs4 import BeautifulSoup as bes
import click
import requests


def get_response_text(link):
    rcount = 0
    while (r := requests.get(link)).status_code != 200:
        if rcount == 20:
            click.echo(f"Tried making request to {link} 20 times, all failed.")
            return None
    return r.text


def search_text_regex(rtext, regex):
    pattern = re.compile(regex)
    text = bes(rtext, "lxml").stripped_strings
    results = [result.groups() for string in text if (result := pattern.search(string)) != None]
    for n, result in enumerate(results, start=1):
        click.echo(f"\n  Result {n}:\n    {result}")


@click.group()
@click.pass_context
def cli(ctx):
    pass


@cli.command()
@click.option("-p", "--pad", is_flag=True, help="Provides the text around the result.")
@click.argument("link", default="https://theprogrammershangout.com/rules/")
@click.argument("regex", default=r"\d\. [ -/:-~]+")
def regsearch(pad, link, regex):
    """Search LINK using REGEX"""
    regex = r"(" + regex + r")" if not pad else r"(.{,50}" + regex + r".{,50})"
    search_text_regex(get_response_text(link), regex)