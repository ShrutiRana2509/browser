import requests
from django.shortcuts import render

def search_view(request):
    query = request.GET.get('q', '')  # Get the search query from the user
    results = []

    if query:
        # Use the provided API key and Search Engine ID
        api_key = "AIzaSyBzHEqs8hMxMV8VYZoxf5q243zt1DMhaWk"
        search_engine_id = "82b45760fe29e490c"
        url = "https://www.googleapis.com/customsearch/v1"

        # Parameters for the API request
        params = {
            "key": api_key,
            "cx": search_engine_id,
            "q": query,
        }

        try:
            response = requests.get(url, params=params)
            
            # Log the status and response for debugging
            #print(f"Status Code: {response.status_code}")
            #print(f"Response Content: {response.text}")

            if response.status_code == 200:
                try:
                    # Decode the JSON response
                    data = response.json()
                    results = data.get("items", [])  # Extract the search results
                except ValueError:
                    results = [{"title": "Error", "link": "", "snippet": "Invalid JSON response."}]
            else:
                # Handle non-200 HTTP responses
                results = [{"title": "Error", "link": "", "snippet": f"API Error: {response.status_code}"}]
        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            results = [{"title": "Error", "link": "", "snippet": f"Request Exception: {str(e)}"}]


    return render(request, "browser.html", {"query": query, "results": results})
