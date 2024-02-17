from app import *

def test_get_images_data():
    # Mocking the images_ref
    images_ref = MockImageRef(sample_data)
    
    # Call the function with the mocked data
    result = get_images_data(images_ref)
    
    # Define the expected output
    expected_output = {
        1: {"id": 1, "url": "image1.jpg"},
        2: {"id": 2, "url": "image2.jpg"},
        3: {"id": 3, "url": "image3.jpg"}
    }
    
    assert result == expected_output