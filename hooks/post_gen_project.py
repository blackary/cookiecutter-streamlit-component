import os
import shutil
import subprocess

REMOVE_PATHS = [
    '{% if cookiecutter.deployment_via_github_actions != "y" %} .github/ {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)


subprocess.call(["git", "init"])
