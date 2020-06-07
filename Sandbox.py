import re
result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.group(0))

result1 = re.findall(r'\w+', 'AV is largest Analytics community of India')
print(result1)