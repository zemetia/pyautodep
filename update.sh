echo "Make sure the version is different [Y/N]"
read ans

if [[ "$ans" == "N" || "$ans" == "n" ]]; then
    echo "Change the version first!"
    exit 0
fi

sudo cp README.md pyautodep
sudo cp LICENSE pyautodep/license.txt
python3 setup.py sdist
twine upload dist/*

echo "UPDATED!"
exit 0