import httpx

url = "https://fantastic-succotash-wvvv456vgxw29v54-5000.app.github.dev/"

# Test the root endpoint
response = httpx.get(url)
print("Root endpoint:")
print(response.status_code)
print(response.text)
print()

# Test the echo endpoint
mydata = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value"
}

response = httpx.post(url + "echo", data=mydata)
print("Echo endpoint:")
print(response.status_code)
print(response.text)
print()

# Test the factor endpoint with various numbers
print("="*50)
print("Testing Factor Endpoint")
print("="*50)

test_cases = [12, 17, 360, 100, 2, 1, 97]

for num in test_cases:
    factor_data = {"inINT": num}
    response = httpx.post(url + "factor", data=factor_data)
    print(f"\nFactors of {num}:")
    print(f"Status: {response.status_code}")
    print(f"Result: {response.json()}")