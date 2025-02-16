# LibraryProject

import os

readme_path = "README.md"

if os.path.exists(readme_path) and os.path.getsize(readme_path) > 0:
    print("✅ README.md exists and is not empty.")
else:
    print("⚠️ README.md is missing or empty.")
