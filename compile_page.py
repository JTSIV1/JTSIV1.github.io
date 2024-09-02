import os
import glob
from bs4 import BeautifulSoup

# Read the navbar content
with open('./components/navbar.html', 'r') as file:
    navbar_content = file.read()

# Read the header content
with open('./components/header.html', 'r') as file:
    header_content = file.read()

# Read the header content
with open('./components/footer.html', 'r') as file:
    footer_content = file.read()

# Read the scripts and libraries content
with open('./components/scripts_and_libraries.html', 'r') as file:
    scripts_and_libraries_content = file.read()

# Get all HTML files in ./src
html_files = glob.glob('./src/*.html')

# Iterate over each HTML file
for html_file in html_files:
    # Read the content of the HTML file
    with open(html_file, 'r') as file:
        file_content = file.read()

    # Find the current page file name
    current_page = os.path.basename(html_file)

    # Add "active" class to the current page in the navbar
    navbar_content_modified = navbar_content.replace(f'href="{current_page}" class="nav-item nav-link">', f'href="{current_page}" class="nav-item nav-link active">')

    # Replace "INSERT_X" with the correct content
    file_content = file_content.replace('<!-- INSERT_NAVBAR -->', navbar_content_modified)
    file_content = file_content.replace('<!-- INSERT_HEADER -->', header_content)
    file_content = file_content.replace('<!-- INSERT_SCRIPTS_AND_LIBRARIES -->', scripts_and_libraries_content)
    file_content = file_content.replace('<!-- INSERT_FOOTER -->', footer_content)

    # Write the updated content back to the file in the current directory
    with open(os.path.basename(html_file), 'w') as file:
        file.write(file_content)