# The program is to check website connectivity status....basically for 'http'

# 200(OK) - The request was successful.
# 301(Moved Permanently) - The server tells the browser to go to a different URL.
# 404(Not Found) - The most common error; the URL is valid, but the specific page doesn't exist.
# 500(Internal Server Error) - The server failed to fulfill a request due to an error on its end.

import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects, RequestException

def check_website_connectivity(url):
    if not url.startswith('http'):
        url = 'https://' + url

    print(f"\nAttempting to connect to the {url}")
    print("-"*40)

    try:
        # Use a timeout to prevent the program from hanging indefinitely
        response = requests.get(url, timeout=5)

        # Successful Response
        if 200 <= response.status_code < 300:
            print(f"✅ Success! Status Code: {response.status_code}")
            print("The website is 'UP' and responded successfully.")
        
        # Redirections
        elif 300 <= response.status_code < 400:
            print(f"⚠️ Redirected. Status Code: {response.status_code}")
            print(f"The request was redirected to: {response.url}")

        # Client Errors
        elif 400 <= response.status_code < 500:
            print(f"🛑 Client Error. Status Code: {response.status_code}")
            print("The server is reachable, but the page/resource was not found (e.g., 404) or access was denied (e.g., 403).")

        # Server errors
        elif 500 <= response.status_code < 600:
            print(f"🔥 Server Error. Status Code: {response.status_code}")
            print("The server is reachable, but an internal error occurred (e.g., 500 Internal Server Error).")

        # Other status codes
        else:
            print(f"❓ Unexpected Status Code: {response.status_code}")
            print("The request returned an unknown status code.")

    # Handling Network Exceptions (Connectivity Failure) ---
    except ConnectionError:#Catches issues like an incorrect URL, DNS failure, or no internet connection.
        print("❌ FAILED: Connection Error.")
        print("Could not connect to the website. Check the URL or your network connection.")
    except Timeout:#Catches situations where the server took longer than the specified 5 seconds to respond.
        print("❌ FAILED: Request Timeout.")
        print("The server took too long to respond. The website might be down or heavily loaded.")
    except TooManyRedirects:
        print("❌ FAILED: Too Many Redirects.")
        print("The request exceeded the maximum number of allowed redirects.")
    except RequestException as e:#A generic catch-all for any other errors the requests library might raise.
        print(f"❌ FAILED: An unexpected error occurred: {e}")


# --- Main Program Execution ---
if __name__ == "__main__":
    print("--- Website Connectivity Checker ---")
    user_url = input("Enter a website URL (e.g., google.com or https://bing.com): ")
    check_website_connectivity(user_url.strip())