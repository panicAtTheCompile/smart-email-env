from env.graders import *

print(grade_classification("normal", "normal"))
print(grade_extraction("5th april high", {"date": "5th April", "priority": "high"}))
print(grade_response("Sorry, your refund is processed"))