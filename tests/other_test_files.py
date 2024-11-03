# You can add more tests related to specific functionality or edge cases here
# For example, testing invalid input, checking for the presence of specific elements in the response, etc.

def test_invalid_post_request(client):
    """Test the predict data page for POST method with invalid data."""
    response = client.post('/predictdata', data={})
    assert response.status_code == 200  # Expect to be redirected or shown the form again
    assert b'Select your Gender' in response.data  # Ensure the form is shown again due to validation failure
