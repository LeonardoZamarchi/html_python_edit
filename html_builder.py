import pandas as pd
from bs4 import BeautifulSoup

def add_rows_to_html_table(df, html_file):
    # Load the HTML file
    with open(html_file, 'r') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table you want to append rows to (you might need to adjust this)
    table = soup.find('table', {'id': 'sample_table'})

    # Loop through the DataFrame and add rows to the table
    for _, row in df.iterrows():
        tr = soup.new_tag('tr')
        for col in df.columns:
            td = soup.new_tag('td')
            td.string = str(row[col])
            tr.append(td)
        table.append(tr)

    # Save the modified HTML content
    with open('modified.html', 'w') as file:
        file.write(str(soup))

# Example usage
data = {'Name': ['John', 'Jane', 'Jim'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Call the function with your DataFrame and HTML file
add_rows_to_html_table(df, '/Users/leozamarchi/Projetos/html_generator/my_html_file.html')