# CIS-117 Lab3
# Read and write country information into separate CSV files by region.
# Thet Tun
# Kezlyn Margareth
# Group #8

# Collaboration:
# Thet Tun was responsible for reading the CSV file
# and grouping countries by region.
# Kezlyn Margareth was responsible for writing the
# country information into separate CSV files.

import csv


def read_countries(filename):
    """Read a CSV and return its country rows grouped by region."""
    countries_by_region = {}

    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["name"]
                region = row["region"]

                group = region
                if region == "":
                    group = "Unassigned"

                if group not in countries_by_region:
                    countries_by_region[group] = []

                countries_by_region[group].append([name, region])

    except FileNotFoundError:
        print(f"Could not find {filename}.")
        return None

    except OSError as error:
        print(f"Could not read {filename}. {error}")
        return None

    return countries_by_region

def write_countries(countries_by_region):
    """Write each region's countries into a separate CSV file."""

    for region, countries in countries_by_region.items():

        filename = region + ".CSV"

        try:
            with open(filename, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["name", "region"])

                writer.writerows(countries)

        except PermissionError:
            print(f"Permission denied: Cannot write to {filename}.")

        except OSError as error:
            print(f"Could not write {filename}. {error}")

countries = read_countries("country_full.csv")
if countries is not None:
    print (countries["Europe"][:3])
    write_countries(countries)
