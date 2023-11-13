# HTTP.sys-Windows-Exec

to run "python https-exec.py 127.0.0.1"

change 127.0.0.1 to the http of the website that has CVE-2015-1635 exploit

1. The "execution_endpoint" should point to the path where you have set up the code execution, not necessarily to the Python script file itself. In the code example, it's set to "/test.py," which suggests that you are directly executing the "test.py" file, not an endpoint that triggers its execution. If you intend to execute the "test.py" file directly, make sure the web server is configured to do so.

2. The content of the "execution_request" should contain a valid HTTP request, which includes the HTTP method, endpoint, and headers. In your code, it's set to "GET /test.py HTTP/1.1," but you may need to adjust it depending on how your server is set up to handle script execution.

3. Ensure that your web server is configured to execute the Python script when the specified endpoint is accessed.

4. Verify that the "Host" variable is set correctly to the server's hostname or IP address.
