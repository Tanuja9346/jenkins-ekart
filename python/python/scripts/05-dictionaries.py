# sample_dict = {
#     'colors': ['orange', 'red', 'blue'],
#     'numbers': [1234, 456, 789, 10],
#     'tools': ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes'],
#     (1234, 456, 789): 'a',
# }
# print(sorted(sample_dict['tools'])) #get value with alpha order.
# print(sorted(sample_dict['colors']))
# sample_dict['numbers'][-1] = 100 # replcae or alter a value in dictionary.
# print(sample_dict['numbers'])

# sample_dict = {   # nested dictionary.
#     "employee": {
#         "name": "John",
#         "age": 30,
#         "city": "New York"
#     }
# }

# print(sample_dict["employee"]["age"])

# sample_dict = {
#     'colors': ['orange', 'red', 'blue'],
#     'numbers': [1234, 456, 789, 10],
#     'tools': ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes'],
#     (1234, 456, 789): 'a',
# }
# sample_dict['fruits'] = ['apple', 'banana', 'orange']---adding values.
# print(sample_dict)

# print(sample_dict.keys())
# print(sample_dict.values())
# print(sample_dict.items())

# [
#     ('colors', ['orange', 'red', 'blue']),
#     ('numbers', [1234, 456, 789, 10]), 
#     ('tools', ['Ansible', 'Terraform', 'Prometheus', 'Docker', 'Kubernetes']), 
#     ((1234, 456, 789), 'a')
# ]