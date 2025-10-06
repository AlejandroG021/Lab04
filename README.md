# Lab 4: Basic HTTP with Python Flask

## Requirements
- Python 3.7+
- Flask
- httpx (for testing)
- pytest (for unit tests)

## Project Structure
```
.
├── my_server.py       # Flask server with all endpoints
├── my_calls.py        # Client script for testing
├── test_server.py     # Unit tests
└── README.md          # This file
```

## Installation

1. Clone the repository from GitHub
2. Open in GitHub Codespaces
3. Install dependencies:
```bash
pip install flask httpx pytest
```

## Running the Server

Start the Flask server:
```bash
python my_server.py
```

The server will start on `http://0.0.0.0:5000`

## API Endpoints

### 1. Root Endpoint
- **URL**: `/`
- **Method**: GET
- **Response**: Plain text message

**Example**:
```bash
curl http://localhost:5000/
```

### 2. Echo Endpoint
- **URL**: `/echo`
- **Method**: POST
- **Parameters**: `text` (form data)
- **Response**: Echoes back the text

**Example**:
```bash
curl -d "text=Hello!" -X POST http://localhost:5000/echo
```

### 3. Factor Endpoint
- **URL**: `/factor`
- **Method**: POST
- **Parameters**: `inINT` (integer as form data)
- **Response**: JSON array of prime factors

**Examples**:
```bash
# Factor 12 -> [2, 2, 3]
curl -d "inINT=12" -X POST http://localhost:5000/factor

# Factor 17 (prime) -> [17]
curl -d "inINT=17" -X POST http://localhost:5000/factor

# Factor 360 -> [2, 2, 2, 3, 3, 5]
curl -d "inINT=360" -X POST http://localhost:5000/factor
```

## Testing

### Manual Testing with Client Script
Run the client script to test all endpoints:
```bash
python my_calls.py
```

### Unit Tests
Run the unit tests with pytest:
```bash
pytest test_server.py -v
```

Or run with coverage:
```bash
pytest test_server.py -v --cov=my-server
```

### Example Results
- `trial_division(12)` → `[2, 2, 3]`
- `trial_division(17)` → `[17]` (prime number)
- `trial_division(360)` → `[2, 2, 2, 3, 3, 5]`
- `trial_division(1)` → `[]` (edge case)

## References
- Flask Documentation: https://flask.palletsprojects.com/
- HTTP Protocol: See course slides
- GitHub Repository: https://github.com/wonder-phil/Lab-04
