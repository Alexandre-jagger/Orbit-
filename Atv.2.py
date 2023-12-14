#pip install requests

import requests
import csv




def get_comments_and_export_to_csv():
    url = "https://jsonplaceholder.typicode.com/comments"
    response = requests.get(url)

    if response.status_code == 200:
        comments = response.json()
        headers = comments[0].keys()
        with open('comments.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(comments)
        
        print("Exportação para CSV concluída.")
    else:
        print(f"Falha na requisição. Código de status: {response.status_code}")

get_comments_and_export_to_csv()