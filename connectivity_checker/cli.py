# connectivity_checker/cli.py

import argparse

def read_user_cli_args():
    """
    Handle the user CLI arguments and options.
    """
    parser = argparse.ArgumentParser(
        prog="connectivity_checker", description="Check the availability of websites."
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="Enter one or more website urls.",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read urls from a file.",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """
    Displays the result of a connectivity check.
    """
    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online!" 👍')
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')
