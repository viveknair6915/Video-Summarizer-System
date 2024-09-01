import os
import importlib.util

class ModuleEditor:
    def __init__(self, module_name):
        self.module_name = module_name
        self.base_dir = self._find_module_base_dir()
        self.frontend_dir = os.path.join(self.base_dir, 'frontend')
        self.index_html_path = os.path.join(self.frontend_dir, 'index.html')
        self.styles_css_path = os.path.join(self.frontend_dir, 'styles.css')

    def _find_module_base_dir(self):
        spec = importlib.util.find_spec(self.module_name)
        if spec is None:
            raise ImportError(f"Module {self.module_name} not found")
        return os.path.dirname(spec.origin)

    def read_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write_file(self, file_path, content):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def modify_index_html(self):
        new_index_html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Clipboard Utility</title>
  <link rel="stylesheet" href="styles.css">
  <script src="./streamlit-component-lib.js"></script>
  <script src="./main.js" defer></script>
</head>
<body class="dark-mode">
  <div class="container">
    <h1>Clipboard Utility</h1>
    <button id="copy-button" class="copy-btn">📋 Copy to Clipboard</button>
  </div>
</body>
</html>
        """
        self.write_file(self.index_html_path, new_index_html_content.strip())

    def modify_styles_css(self):
        new_styles_css_content = """
/* styles.css */

body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  color: #333;
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  transition: background-color 0.3s, color 0.3s;
}

.dark-mode {
  background-color: rgba(14, 17, 23, 0.7);
  color: #fff;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

h1 {
  font-size: 2rem;
  margin-bottom: 20px;
}

.copy-btn {
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.copy-btn:hover {
  background-color: #0056b3;
}

.copy-btn:active {
  transform: scale(0.98);
}
        """
        self.write_file(self.styles_css_path, new_styles_css_content.strip())

    def modify_frontend_files(self):
        self.modify_index_html()
        self.modify_styles_css()
