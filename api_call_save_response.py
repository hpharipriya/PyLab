import requests
import json

def post_ids_to_api(api_url, headers=None):
    payload = [4854, 4853, 4852, 4851, 4850, 4849, 4848, 4847, 4846, 4856, 4855,4890]

    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    api_url = "API_URL"
        "Content-Type": "application/json"
    }

    response_data = post_ids_to_api(api_url, headers)
    with open("out.json", 'w') as file:
        json.dump(response_data, file, indent=4)
    if response_data:
        print("Response from API:", response_data)


