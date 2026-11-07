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
countries = read_countries("country_full.csv")
if countries is not None:
    print (countries["Europe"][:3])