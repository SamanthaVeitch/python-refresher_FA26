import argparse
import array
import my_utils

parser = argparse.ArgumentParser()

parser.add_argument("--country", type=str, required=True,
                    help="Country name to query")
parser.add_argument("--file_name", type=str, required=True,
                    help="Name of the CSV file to read")
parser.add_argument("--county_column", type=int, required=True,
                    help="Index of the column to search for the country name")
parser.add_argument("--fires_column", type=int, required=True,
                    help="Index of the column to return values from")
parser.add_argument("--operation",
                    help="What operation to preform on the returned data.")

args = parser.parse_args()

country = args.country
file_name = args.file_name
county_column = args.county_column
fires_column = args.fires_column
fires = my_utils.get_column(
    file_name, county_column, country, fires_column)

if args.operation is None:
    print(fires)
elif (args.operation == "mean"
      or args.operation == "Mean"):
    print(my_utils.array_mean(array.array("i", fires)))
elif (args.operation == "median"
      or args.operation == "Median"):
    print(my_utils.array_median(array.array("i", fires)))
elif (args.operation == "std_dev"
      or args.operation == "std"
      or args.operation == "stdev"):
    print(my_utils.array_std_dev(array.array("i", fires)))
