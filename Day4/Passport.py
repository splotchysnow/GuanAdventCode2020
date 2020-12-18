# A class for Passport that contains different attributes.

def cidChecker():
    # This is just useless...
    return True


class Passport:

    def __init__(self, ecl, byr, iyr, pid, cid, hgt, eyr, hcl):
        self.ecl = ecl
        self.byr = byr
        self.iyr = iyr
        self.pid = pid
        self.cid = cid
        self.hgt = hgt
        self.eyr = eyr
        self.hcl = hcl
        self.check = self.checkInvalidPassport()

    def getEcl(self):
        return self.ecl

    def getByr(self):
        return self.byr

    def getIyr(self):
        return self.iyr

    def getPid(self):
        return self.pid

    def getCid(self):
        return self.cid

    def getHgt(self):
        return self.hgt

    def getEyr(self):
        return self.eyr

    def getHcl(self):
        return self.hcl

    def getCheck(self):
        return self.check

    def checkInvalidPassport(self):
        if (
                self.existenceChecker() and self.byrChecker() and cidChecker() and self.eclChecker() and
                self.eyrChecker() and self.hclChecker()
                and self.hgtChecker() and self.iyrChecker() and self.pidChecker()):
            return True
        else:
            return False

    # when called, check if the checker is working properly with correct examples.
    def checkChecker(self):
        error = []
        if not self.existenceChecker():
            error.append("Existence False")
        if not self.byrChecker():
            error.append("Byr False")
        if not cidChecker():
            error.append("cid false")
        if not self.eclChecker():
            error.append("Ecl false")
        if not self.eyrChecker():
            error.append("EYR FALSE")
        if not self.hclChecker():
            error.append("HCL False")
        if not self.hgtChecker():
            error.append("Hgt false")
        if not self.iyrChecker():
            error.append("IYR false")
        if not self.pidChecker():
            error.append("Pid false")
        return error

    def existenceChecker(self):
        F = ""
        if ((self.ecl != F) and (self.byr != F) and (self.iyr != F) and (self.pid != F) and (self.hgt != F) and (
                self.eyr != F) and (self.hcl != F)):
            return True
        else:
            return False

    # Not so sure that maybe length is 3 or 4... I think 4 is fine for now...
    def byrChecker(self):
        byr = int(self.byr)
        if len(self.byr) == 4 and (1920 <= byr <= 2002):
            return True
        else:
            return False

    def iyrChecker(self):
        iyr = int(self.iyr)
        if len(self.iyr) == 4 and (2010 <= iyr <= 2020):
            return True
        else:
            return False

    def eyrChecker(self):
        eyr = int(self.eyr)
        if len(self.eyr) == 4 and (2020 <= eyr <= 2030):
            return True
        else:
            return False

    # Get the letter for if the thing is cm or inch.
    # I Think this function is now working properly.
    def hgtChecker(self):
        try:
            hgt = int(self.hgt[:-2])
            measurement = self.hgt[-2:len(self.hgt)]  # Either in or cm
            # print(hgt)
            if measurement == "cm" and (150 <= hgt <= 193):
                return True
            elif measurement == "in" and (59 <= hgt <= 76):
                return True
            else:
                return False
        except ValueError:
            return False

    # Either get the character value and just compare the value, or make an array with 0-9 and a-f and check it that way.
    # 0-9 is 48 -> 57 and  a-f is 97 -> 102
    # Something is wrong with this...
    def hclChecker(self):

        hcl = self.hcl
        if len(hcl) == 0:
            return False

        if hcl[0] == "#":
            sign = True
        else:
            sign = False

        check = True
        hcl = self.hcl[1:]
        for i in hcl:
            char_int = ord(i)
            if 48 <= char_int <= 57:
                pass
            elif 97 <= char_int <= 102:
                pass
            else:
                check = False

        if check and sign:
            return True
        else:
            return False

    # either amb, blu, brn, gry, grn, hzl, oth
    def eclChecker(self):
        ecl = self.ecl
        arrayOfSolution = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        for i in arrayOfSolution:
            if i == ecl:
                return True
        return False

    # a nine digit number including leading zeros.
    # Maybe do a catch int error? LOL THAT IS A NICE IDEA ACTUALLY.
    # Not really sure if it reports the integer value errors... but yeah we can try this
    def pidChecker(self):
        pid = self.pid
        try:
            int_pid = int(pid)
            if len(pid) == 9:
                return True
            else:
                return False
        except ValueError:
            return False

