import urllib.error
import urllib.request
from datetime import date, datetime
from itertools import product
from pathlib import Path


def get_input(year: int, day: int) -> str:
    """Request input from aoc website."""
    with open("env/session.txt") as f:
        contents = f.read()

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    req = urllib.request.Request(url, headers={"Cookie": contents.strip()})
    return urllib.request.urlopen(req).read().decode()  # noqa: S310


def main() -> None:
    """Main app routine, returns nothing."""
    today = date.today()
    now = datetime.now().time()
    first_year = 2015
    for year, day in product(range(first_year, today.year + 1), range(1, 26)):
        this_date = date(year, 12, day)
        if this_date > today:
            print("Reached last challenge.")
            break
        elif this_date == today and now.hour < 5:
            print("Reached last challenge, todays challenge will be available at 5:00.")
            break
        print(f"Advent of {year}: Day {day:>2d}")

        path = Path(f"src/year{year}/day{day:02d}")
        if path.exists():
            continue

        path.mkdir(parents=True, exist_ok=True)

        try:
            s = get_input(year, day)
            with open(path.joinpath("input.txt"), "w") as f:
                f.write(s)
        except urllib.error.URLError as e:
            print(f"Failed to download: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
