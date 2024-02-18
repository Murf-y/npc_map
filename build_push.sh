# This script would build the project and add-commit-push the changes to the remote repository

pip install -r requirements.txt

python3 main.py

git add .

git commit -m "Build the project"

git push

echo "Build and push completed 🚀"