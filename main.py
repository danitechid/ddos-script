import sys
import requests
import threading
from colorama import Fore, Style

def make_request(url, request_number):
  try:
    response = requests.get(url)
    status_code = response.status_code
    if status_code == 200:
      print(f"{Fore.GREEN}[Success] {Fore.WHITE}Request to {url} completed with status code {status_code}{Style.RESET_ALL}")
    else:
      print(f"{Fore.YELLOW}[Failed] {Fore.WHITE}Request to {url} completed with status code {status_code}{Style.RESET_ALL}")
  except Exception as e:
    print(f"{Fore.RED}[Failed] {Fore.WHITE}Failed to request {url}: {str(e)}{Style.RESET_ALL}")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print(f"{Fore.YELLOW}Usage: python main.py <target-url> <request-count>{Style.RESET_ALL}")
    sys.exit(1)

  domain = sys.argv[1]
  num_requests = int(sys.argv[2])

  urls = [domain for _ in range(num_requests)]  
  threads = []

  for i, url in enumerate(urls, start=1):
    thread = threading.Thread(target=make_request, args=(url, i))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  print(f"{Fore.CYAN}All requests completed.{Style.RESET_ALL}")
