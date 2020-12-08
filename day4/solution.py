# # https://adventofcode.com/2020/day/4
# # part 1
required = ['byr', 'pid', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl']
valid = 0

with open("input.txt") as file:
    lines = [lines.replace("\n", " ") for lines in file.read().split("\n\n")]


    passports = [{key: value for word in line.split() for key, value in [word.split(':')]} for line in lines]

    for p in passports:
        keys = list(p.keys())
        if 'cid' in keys:
            keys.remove('cid')

        if set(keys) == set(required):
            valid +=1


print(valid)

# part 2

import re

required = ['byr', 'pid', 'eyr', 'iyr', 'hgt', 'hcl', 'ecl']
valid = 0
with open("input.txt") as file:
    lines = [lines.replace("\n", " ") for lines in file.read().split("\n\n")]
    passports = [{key: value for word in line.split() for key, value in [word.split(':')]} for line in lines]

    for p in passports:
        if all (key in p for key in required):
            if (
                int(p['byr']) >= 1920 and int(p['byr']) <= 2002 and
                int(p['iyr']) >= 2010 and int(p['iyr']) <= 2020 and
                int(p['eyr']) >= 2020 and int(p['eyr']) <= 2030 and
                re.match("^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$",p['hgt']) and
                re.match("#[0-9a-f]{6}",p['hcl']) and
                re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", p['ecl']) and
                re.match("^\d{9}$", p['pid'])
            ):
                valid += 1

print(valid)
