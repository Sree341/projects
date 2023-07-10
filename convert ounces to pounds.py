def convert_weight(ounces):
    pounds=ounces/16
    result = "{} ounces equal to {:<2.2f} pounds".format(ounces, pounds)
    return result
print(convert_weight(10))
print(convert_weight(12)) # Should be: 12 ounces equals 0.75 pounds
print(convert_weight(50.5)) # Should be: 50.5 ounces equals 3.16 pounds
print(convert_weight(16)) # Should be: 16 ounces equals 1.00 pounds