import pytest
from my_server import app, trial_division

@pytest.fixture
def client():
    """Create a test client for the Flask app"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestTrialDivision:
    """Unit tests for the trial_division function"""
    
    def test_prime_number(self):
        """Test that prime numbers return themselves"""
        assert trial_division(17) == [17]
        assert trial_division(2) == [2]
        assert trial_division(97) == [97]
    
    def test_composite_number(self):
        """Test composite number factorization"""
        assert trial_division(12) == [2, 2, 3]
        assert trial_division(360) == [2, 2, 2, 3, 3, 5]
        assert trial_division(100) == [2, 2, 5, 5]
    
    def test_edge_cases(self):
        """Test edge cases"""
        assert trial_division(1) == []
        assert trial_division(4) == [2, 2]

class TestFlaskEndpoints:
    """Integration tests for Flask endpoints"""
    
    def test_root_endpoint(self, client):
        """Test the root endpoint"""
        response = client.get('/')
        assert response.status_code == 200
        assert b"you called" in response.data
    
    def test_echo_endpoint(self, client):
        """Test the echo endpoint"""
        response = client.post('/echo', data={'text': 'Hello World'})
        assert response.status_code == 200
        assert b"You said: Hello World" in response.data
    
    def test_factor_endpoint_prime(self, client):
        """Test factor endpoint with prime number"""
        response = client.post('/factor', data={'inINT': '17'})
        assert response.status_code == 200
        assert response.json == [17]
    
    def test_factor_endpoint_composite(self, client):
        """Test factor endpoint with composite number"""
        response = client.post('/factor', data={'inINT': '12'})
        assert response.status_code == 200
        assert response.json == [2, 2, 3]
    
    def test_factor_endpoint_360(self, client):
        """Test factor endpoint with 360"""
        response = client.post('/factor', data={'inINT': '360'})
        assert response.status_code == 200
        assert response.json == [2, 2, 2, 3, 3, 5]
    
    def test_factor_endpoint_invalid_input(self, client):
        """Test factor endpoint with invalid input"""
        response = client.post('/factor', data={'inINT': 'not_a_number'})
        assert response.status_code == 400
        assert 'error' in response.json
    
    def test_factor_endpoint_missing_param(self, client):
        """Test factor endpoint with missing parameter"""
        response = client.post('/factor', data={})
        assert response.status_code == 400

if __name__ == '__main__':
    pytest.main([__file__, '-v'])