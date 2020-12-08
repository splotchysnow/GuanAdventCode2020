#A class for Passport that contains different attributes.

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
        F = ""
        if ((self.ecl != F) and (self.byr != F) and (self.iyr != F) and (self.pid != F) and (self.hgt != F) and (self.eyr != F) and (self.hcl != F)):
            return True
        else:
            return False


        