from processor import process_file


def main():

    filepath = input(
        "Enter file path: "
    ).strip('"')

    process_file(filepath)


if __name__ == "__main__":
    main()