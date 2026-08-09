import re

with open('/home/minipc/Documentos/proyectos/mundonica/mundonica/mundonica/applications/home/forms.py', 'r') as f:
    content = f.text if hasattr(f, 'text') else f.read()

# We want to replace all occurrences of:
# 'xyz_activo': forms.Select( ... choices=[ ... ] ),
# But they can span multiple lines!
# A better way is to use a regex that matches:
# '(\w+_activo)'\s*:\s*forms\.Select\([^)]*?\s*choices\s*=\s*\[.*?\]\s*\)
# Actually, the closing parenthesis for Select might be on a different line, and there could be nested parens.
# Let's just find each field that ends in _activo': forms.Select(...)
# and replace it with 'xyz_activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),

# A safer regex:
pattern = re.compile(r"'(\w+_activo)'\s*:\s*forms\.Select\s*\(\s*(?:attrs\s*=\s*\{[^}]*\}\s*,\s*)?choices\s*=\s*\[.*?\]\s*\)", re.DOTALL)

# Let's check how many it matches
matches = pattern.findall(content)
print(f"Found {len(matches)} exact matches for the simple pattern")

# Some might not have attrs first. So let's do a more robust approach:
pattern2 = re.compile(r"'(\w+_activo)'\s*:\s*forms\.Select\([^)]*\)", re.DOTALL)
# Wait, if choices=[...] contains parens, [^)]* will fail.

# Let's write a simple state machine or simpler regex that just matches the block up to the closing `]),` or `])`
pattern3 = re.compile(r"('\w+_activo'\s*:\s*forms\.Select\b.*?\]\s*\))", re.DOTALL)
matches3 = pattern3.findall(content)
print(f"Found {len(matches3)} matches for pattern3")

for match in matches3:
    field_name = re.search(r"'(\w+_activo)'", match).group(1)
    replacement = f"'{field_name}': forms.CheckboxInput(attrs={{'class': 'form-check-input'}})"
    content = content.replace(match, replacement)

with open('/home/minipc/Documentos/proyectos/mundonica/mundonica/mundonica/applications/home/forms.py', 'w') as f:
    f.write(content)
print("Updated forms.py")
