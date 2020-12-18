from Passport import Passport

passport = Passport("grn", "1980", "2012", "087499704", "123456", "74in", "2030", "#623a2f")

print(passport.checkChecker())
print(passport.getHcl())
