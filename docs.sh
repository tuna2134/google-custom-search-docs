pip install pdoc3
pdoc google_custom_search --html -o docs --force
mv docs/google_custom_search/index.html docs/index.html
mv docs/google_custom_search/search.html docs/search.html
mv docs/google_custom_search/object.html docs/object.html
rm -r docs/google_custom_search