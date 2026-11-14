# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
#
# Names: Joel Castillo, Kevin Shu, Vaibhav Vaidish, Namith Chelikani
# Section: 469, 569
# Assignment: LAB Topic 11 Team
# Date: 11 Nov 2026
#
def valid_hair_color(hcl):

    # Hair color must be exactly 7 characters
    if len(hcl) != 7:
        return False

    # First character must be #
    if hcl[0] != "#":
        return False

    # Remaining characters must be hexadecimal digits
    for char in hcl[1:]:
        if char not in "0123456789abcdef":
            return False

    return True


def valid_height(hgt):

    # Height ending in cm
    if hgt.endswith("cm"):

        value = int(hgt[:-2])

        return 150 <= value <= 193

    # Height ending in in
    elif hgt.endswith("in"):

        value = int(hgt[:-2])

        return 59 <= value <= 76

    # Anything else is invalid
    return False


def valid_cid(cid):

    # Must contain exactly 3 characters
    if len(cid) != 3:
        return False

    # All characters must be digits
    if not cid.isdigit():
        return False

    # Leading zeros are not allowed
    if cid[0] == "0":
        return False

    return True


def main():

    # Ask user for the input file
    filename = input("Enter the name of the file: ")

    # Read passport data from file
    infile = open(filename, "r")
    data = infile.read()
    infile.close()

    # Split into individual passports
    passports = data.strip().split("\n\n")

    # Store passports that pass all checks
    valid_passports = []

    # Allowed eye colors from the lab instructions
    valid_eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    # Check each passport
    for passport in passports:

        # Store passport fields in a dictionary
        fields = {}

        for item in passport.split():

            pieces = item.split(":")
            fields[pieces[0]] = pieces[1]

        # Required fields
        required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "cid"]

        valid = True

        # Verify all required fields exist
        for field in required:
            if field not in fields:
                valid = False

        # Only perform value checks if all required fields were present
        if valid:

            # Check birth year range
            if not (1922 <= int(fields["byr"]) <= 2010):
                valid = False

            # Check issue year range
            elif not (2016 <= int(fields["iyr"]) <= 2026):
                valid = False

            # Check expiration year range
            elif not (2026 <= int(fields["eyr"]) <= 2036):
                valid = False

            # Check height format and range
            elif not valid_height(fields["hgt"]):
                valid = False

            # Check hair color format
            elif not valid_hair_color(fields["hcl"]):
                valid = False

            # Check eye color is one of the accepted values
            elif fields["ecl"] not in valid_eyes:
                valid = False

            # Check country ID rules
            elif not valid_cid(fields["cid"]):
                valid = False

        # Save passport if every check passed
        if valid:
            valid_passports.append(passport)

    # Create the output file
    outfile = open("valid_passports2.txt", "w")

    for i in range(len(valid_passports)):
        outfile.write(valid_passports[i])

        # Separate passports with one blank line
        if i != len(valid_passports) - 1:
            outfile.write("\n\n")

    outfile.close()

    print(f"There are {len(valid_passports)} valid passports")


main()