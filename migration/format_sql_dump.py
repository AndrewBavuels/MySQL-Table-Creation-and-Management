import re

# Read the SQL file
with open('holi_books.sql', 'r') as file:
    sql_content = file.read()

# Replace commas within values with new lines
formatted_content = re.sub(r'\),\(', '),\n(', sql_content)
formatted_content = formatted_content.replace('),(', '),\n(')

# Write the formatted content to a new file
with open('formatted_holi_books.sql', 'w') as file:
    file.write(formatted_content)

print("Formatted file saved as 'formatted_backup.sql'")
