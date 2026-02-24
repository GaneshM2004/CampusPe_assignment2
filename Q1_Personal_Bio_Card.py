# Variables to store student information and also Update in it when needed easily
name = "Ganesh Mulgund"
age = "20 years"
course = "Computer Science Engineering"
college = "Tontadarya College of Engineering, Gadag"
email = "ganeshmulgund05@gmail.com"

# Width is used to make sure card has fixed border length
width = 56

# Displaying the Bio Card using print statements with f-strings
# Calculated the spaces to align the text properly within the card borders
print("╔" + "═" * (width - 2) + "╗")
print("║"+" "*18+"STUDENT BIO CARD"+" "*20+"║")
print("╠" + "═" * (width - 2) + "╣")
print("║ Name    : "+name+" "*29+"║")
print("║ Age     : "+age+" "*35+"║")
print("║ Course  : "+course+" "*15+"║")
print("║ College : "+college+" "*3+"║")
print("║ Email   : "+email+" "*18+"║")
print("╚" + "═" * (width - 2) + "╝")

# Output:
# ╔══════════════════════════════════════════════════════╗
# ║                   STUDENT BIO CARD                   ║
# ╠══════════════════════════════════════════════════════╣
# ║ Name      : Ganesh Mulgund                           ║
# ║ Age       : 20 years                                 ║
# ║ Course    : Computer Science Engineering             ║
# ║ College   : Tontadarya College of Engineering, Gadag ║
# ║ Email     : ganeshmulgund05@gmail.com                ║
# ╚══════════════════════════════════════════════════════╝