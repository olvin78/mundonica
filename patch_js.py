import re

with open('/home/minipc/Documentos/proyectos/mundonica/mundonica/mundonica/templates/empresa_crear.html', 'r') as f:
    content = f.text if hasattr(f, 'text') else f.read()

replacement = """
      group.fields.forEach(fName => {
         const node = getFieldNode(fName);
         if (node) {
            // Add a visibility toggle to text inputs and textareas
            const inputEl = node.querySelector('input:not([type="checkbox"]):not([type="file"]):not([type="hidden"]), textarea');
            if(inputEl) {
                const labelEl = node.querySelector('label');
                if(labelEl && !node.querySelector('.hide-field-btn')) {
                    labelEl.style.display = 'flex';
                    labelEl.style.justifyContent = 'space-between';
                    labelEl.style.alignItems = 'center';
                    
                    const btn = document.createElement('button');
                    btn.type = 'button';
                    btn.className = 'btn btn-sm btn-outline-secondary hide-field-btn';
                    btn.style.padding = '0 6px';
                    btn.style.fontSize = '12px';
                    btn.style.lineHeight = '1.2';
                    
                    // State initialization
                    if (inputEl.value === ' ') {
                        btn.innerHTML = '<i class="bi bi-eye-slash"></i> Oculto';
                        btn.classList.add('btn-outline-danger');
                        btn.classList.remove('btn-outline-secondary');
                        inputEl.readOnly = true;
                        inputEl.style.opacity = '0.5';
                    } else {
                        btn.innerHTML = '<i class="bi bi-eye"></i> Visible';
                        inputEl._savedValue = inputEl.value;
                    }
                    
                    btn.onclick = function() {
                        if (inputEl.readOnly) {
                            // Turn ON
                            inputEl.readOnly = false;
                            inputEl.style.opacity = '1';
                            inputEl.value = inputEl._savedValue || '';
                            btn.innerHTML = '<i class="bi bi-eye"></i> Visible';
                            btn.classList.remove('btn-outline-danger');
                            btn.classList.add('btn-outline-secondary');
                        } else {
                            // Turn OFF
                            inputEl._savedValue = inputEl.value;
                            inputEl.value = ' ';
                            inputEl.readOnly = true;
                            inputEl.style.opacity = '0.5';
                            btn.innerHTML = '<i class="bi bi-eye-slash"></i> Oculto';
                            btn.classList.add('btn-outline-danger');
                            btn.classList.remove('btn-outline-secondary');
                        }
                    };
                    labelEl.appendChild(btn);
                }
            }
            targetContainer.appendChild(node);
            activeFieldsInGroup++;
            hasFieldsInPane = true;
         }
"""

target = """
      group.fields.forEach(fName => {
         const node = getFieldNode(fName);
         if (node) {
            targetContainer.appendChild(node);
            activeFieldsInGroup++;
            hasFieldsInPane = true;
         }
"""

content = content.replace(target.strip(), replacement.strip())

with open('/home/minipc/Documentos/proyectos/mundonica/mundonica/mundonica/templates/empresa_crear.html', 'w') as f:
    f.write(content)
print("Patched empresa_crear.html successfully.")
