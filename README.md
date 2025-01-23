# Real-Time Traffic Monitor on Localhost

This project demonstrates how to monitor real-time traffic on a localhost server while simulating DDoS attacks for educational purposes. It uses a Flask backend to handle incoming requests and an HTML frontend to visualize the traffic load.

## Features
- Real-time request count visualization.
- Simple HTML interface for monitoring.
- Demonstrates the impact of multiple simultaneous requests on a server.

## File Structure
```
project-folder/
│
├── server.py             # Flask backend script
├── templates/            # Folder for HTML templates
│   └── monitor.html       # HTML file for monitoring traffic
└── static/               # (Optional) Folder for static files like CSS, JS, or images
```

## Prerequisites

Make sure you have the following installed:
- Python 3.x
- pip (Python package installer)

### Python Libraries
Install Flask if it's not already installed:
```bash
pip install flask
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd project-folder
   ```

2. **Run the Flask Server**
   Execute the following command in the project directory:
   ```bash
   python server.py
   ```
   This will start the server on `http://localhost:5000`.

3. **Access the Monitoring Page**
   Open your browser and navigate to:
   ```
   http://localhost:5000/monitor
   ```

4. **Simulate Traffic**
   Use a script or tool to send repeated requests to the server's root endpoint (`http://localhost:5000`). For example, you can use the DDoS simulation script provided for educational purposes.

5. **Watch Real-Time Updates**
   The monitoring page will dynamically display the total number of requests received by the server.

## How It Works
- **Flask Backend**:
  - The server counts incoming requests to the `/` endpoint.
  - A `/get_count` API endpoint provides the current count as JSON data.
- **Frontend**:
  - The `monitor.html` page fetches the request count every second and updates the display in real time.

## Example Output
- **Monitoring Page**:
  - Displays a title and the current request count.
  - Automatically updates the count every second.

- **Simulated Requests**:
  - Using the DDoS script, requests to `http://localhost:5000` will increment the counter visible on the monitoring page.

## Educational Use Only
This project is intended for educational purposes to demonstrate the principles of real-time traffic monitoring and the effects of high request loads on a server. **Do not use this project for malicious purposes.**

## License
This project is licensed under the MIT License. Feel free to use and modify it for educational purposes.

