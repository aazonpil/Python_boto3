d = {"employees":[{"firstName":"John", "lastName":"Doe"},{"firstName":"Anna", "lastName":"Smith"},
 {"firstName":"Petter", "lastName":"Jones"}],
 "owners":[{"firstName":"Jack","lastName":"Petter"},{"firstName":"Jessy", "lastName":"Petter"}]}
list_employees=d.get("employees")
employee_two=list_employees[1]
print(employee_two)
print(f"The employee2 last name is {employee_two.get('lastName')}")

