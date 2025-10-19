"""
Word Occurrences
Estimate: 15 minutes
Actual:   1 hr
"""
FILENAME = "wimbledon.csv"
COUNTRY_COLUMN = 1
CHAMPION_COLUMN = 2


def main():
    """Read .csv file and print records about Wimbledon champions and countries."""
    records = load_wimbledon_champion_history(FILENAME)
    countries, champion_to_count = handle_records(records)
    print_record_information(countries, champion_to_count)


def load_wimbledon_champion_history(filename):
    """Load wimbledon champion and champion country information from .csv file"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        wimbledon_records = [line.strip().split(",") for line in in_file]
    return wimbledon_records


def handle_records(records):
    """Process the records information by counting each champion win and tracking champion countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_COLUMN])
        champion_to_count[record[CHAMPION_COLUMN]] = champion_to_count.get(record[CHAMPION_COLUMN], 0) + 1
    return countries, champion_to_count


def print_record_information(countries, champion_to_count):
    """Print the champions and their number of wins, as well as countries that have champions."""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
