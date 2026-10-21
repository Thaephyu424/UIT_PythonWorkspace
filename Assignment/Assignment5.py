class Student:

  def __init__(self, name, marks):
    self.name = name
    self.marks = marks  # Dictionary of {subject: marks}

  def calculate_percentage(self):
    """Calculates the percentage assuming each subject is out of 100 marks."""
    if not self.marks:
      return 0.0

    total_obtained = sum(self.marks.values())
    total_maximum = len(self.marks) * 100

    percentage = (total_obtained / total_maximum) * 100
    return percentage

  def print_info(self):
    """Prints student details including name, subject marks, and percentage."""
    print(f"Student Name: {self.name}")
    print("Marks per Subject:")
    for subject, mark in self.marks.items():
      print(f"  - {subject}: {mark}")
    print(f"Percentage: {self.calculate_percentage():.2f}%")
    print("-" * 40)


# --- Example Usage ---

# 1. Store multiple students in a list
students_list = [
    Student("Alice", {"Math": 85, "Science": 90, "English": 78, "History": 88}),
    Student("Bob", {"Math": 60, "Science": 65, "English": 70, "History": 55}),
    Student(
        "Charlie", {"Math": 95, "Science": 92, "English": 96, "History": 90}
    ),
    Student("Diana", {"Math": 72, "Science": 78, "English": 80, "History": 75}),
]

# 2. Print info for each student
print("=== Individual Student Records ===")
for student in students_list:
  student.print_info()

# 3. Find student with max and min percentage
top_student = max(students_list, key=lambda s: s.calculate_percentage())
lowest_student = min(students_list, key=lambda s: s.calculate_percentage())

print("=== Performance Summary ===")
print(
    f"🏆 Highest Performer: {top_student.name} with"
    f" {top_student.calculate_percentage():.2f}%"
)
print(
    f"📉 Lowest Performer: {lowest_student.name} with"
    f" {lowest_student.calculate_percentage():.2f}%"
)




# No2
class Employee:

  def __init__(self, empid, ename, basicSalary, medicalAllowance):
    self.empid = empid
    self.ename = ename
    self.basicSalary = basicSalary
    self.medicalAllowance = medicalAllowance

    # Standard allowances and deductions
    self.hra = 0.50 * self.basicSalary
    self.pf = 0.12 * self.basicSalary
    self.pt = 200

  def calculate_gross(self):
    return self.basicSalary + self.hra + self.medicalAllowance

  def calculate_net(self):
    return self.calculate_gross() - self.pf - self.pt

  def show_details(self):
    print(f"--- Employee Details ---")
    print(f"Employee ID   : {self.empid}")
    print(f"Employee Name : {self.ename}")
    print(f"Basic Salary  : ${self.basicSalary:.2f}")
    print(f"Gross Salary  : ${self.calculate_gross():.2f}")
    print(f"Net Salary    : ${self.calculate_net():.2f}")
    print("=" * 40)


class Manager(Employee):

  def __init__(self, empid, ename, basicSalary, medicalAllowance):
    super().__init__(empid, ename, basicSalary, medicalAllowance)

    # Manager-specific extra attributes
    self.managerAllowance = 0.08 * self.basicSalary
    self.foodAllowance = 0.10 * self.basicSalary
    self.otherAllowance = 0.03 * self.basicSalary

  def calculate_gross(self):
    base_gross = super().calculate_gross()
    return (
        base_gross
        + self.managerAllowance
        + self.foodAllowance
        + self.otherAllowance
    )

  def calculate_net(self):
    return self.calculate_gross() - self.pf - self.pt

  def show_details(self):
    print(f"--- Manager Details ---")
    print(f"Employee ID   : {self.empid}")
    print(f"Manager Name  : {self.ename}")
    print(f"Basic Salary  : ${self.basicSalary:.2f}")
    print(f"HRA (50%)     : ${self.hra:.2f}")
    print(f"Medical Allow : ${self.medicalAllowance:.2f}")
    print(f"Manager Allow : ${self.managerAllowance:.2f}")
    print(f"Food Allow    : ${self.foodAllowance:.2f}")
    print(f"Other Allow   : ${self.otherAllowance:.2f}")
    print(f"PF (12%)      : ${self.pf:.2f}")
    print(f"PT            : ${self.pt:.2f}")
    print(f"------------------------")
    print(f"Gross Salary  : ${self.calculate_gross():.2f}")
    print(f"Net Salary    : ${self.calculate_net():.2f}")
    print("=" * 40)


class MarketingExecutive(Employee):

  def __init__(
      self, empid, ename, basicSalary, medicalAllowance, kmsTravelled
  ):
    super().__init__(empid, ename, basicSalary, medicalAllowance)

    # Marketing Executive specific attributes
    self.kmsTravelled = kmsTravelled
    self.phoneAllowance = 1000
    self.travelAllowance = 5 * self.kmsTravelled

  def calculate_gross(self):
    """Calculates gross salary including base components plus marketing allowances."""
    base_gross = super().calculate_gross()
    return base_gross + self.phoneAllowance + self.travelAllowance

  def calculate_net(self):
    """Calculates net salary for the marketing executive (Gross - PF - PT)."""
    return self.calculate_gross() - self.pf - self.pt

  def show_details(self):
    """Displays comprehensive details and salary breakdown of the marketing executive."""
    print(f"--- Marketing Executive Details ---")
    print(f"Employee ID   : {self.empid}")
    print(f"Executive Name: {self.ename}")
    print(f"Basic Salary  : ${self.basicSalary:.2f}")
    print(f"HRA (50%)     : ${self.hra:.2f}")
    print(f"Medical Allow : ${self.medicalAllowance:.2f}")
    print(f"Phone Allow   : ${self.phoneAllowance:.2f}")
    print(
        f"Travel Allow  : ${self.travelAllowance:.2f} ({self.kmsTravelled} kms"
        " @ $5/km)"
    )
    print(f"PF (12%)      : ${self.pf:.2f}")
    print(f"PT            : ${self.pt:.2f}")
    print(f"-----------------------------------")
    print(f"Gross Salary  : ${self.calculate_gross():.2f}")
    print(f"Net Salary    : ${self.calculate_net():.2f}")
    print("=" * 40)


# --- Example Usage ---

# Creating a MarketingExecutive object (e.g., traveled 150 kms)
mkt_exec = MarketingExecutive(
    empid=301,
    ename="Alex Mercer",
    basicSalary=45000,
    medicalAllowance=2500,
    kmsTravelled=150,
)

# Displaying marketing executive details and calculated salaries
mkt_exec.show_details()