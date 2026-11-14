# By submitting this assignment, I agree to the following:
# Aggies do not lie, cheat, or steal, or tolerate those who do.
# I have not given or received any unauthorized aid on this assignment.
#
# Names: Joel Castillo, Kevin Shu, Vaibhav Vaidish, Namith Chelikani
# Section: 469, 569
# Assignment: LAB Topic 11 Team
# Date: 11 Nov 2026
#
def main():

     # Ask the user for the file containing passport data
    filename = input("Enter the name of the file: ")

     # Read the entire file as one string
    infile = open(filename, "r")
    data = infile.read()
    infile.close()

    # Each passport is separated by a blank line
    passports = data.strip().split("\n\n")

    # Store all valid passports here
    valid_passports = []

    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "cid"]

    # Go through each passport one at a time
    for passport in passports:

        # Store the field names found in this passport
        fields = []

        # split() separates all key:value pairs regardless of whether they are separated by spaces or newlines
        entries = passport.split()

        for item in entries:
            # Extract only the key part before the colon
            key = item.split(":")[0]
            fields.append(key)

        # Assume the passport is valid until proven otherwise
        valid = True

        # Check that every required field exists
        for field in required_fields:
            if field not in fields:
                valid = False

        # Save the passport if all required fields were found
        if valid:
            valid_passports.append(passport)

    # Create output file for valid passports
    outfile = open("valid_passports.txt", "w")

    # Write passports in the same format as the input
    for i in range(len(valid_passports)):
        outfile.write(valid_passports[i])

        # Add one blank line between passports
        if i != len(valid_passports) - 1:
            outfile.write("\n\n")

    # Close the output file
    outfile.close()

    print(f"There are {len(valid_passports)} valid passports")

main()
