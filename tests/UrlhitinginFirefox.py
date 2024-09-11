# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# # driver = webdriver.Firefox
# # driver.get("https://www.google.com")
# # driver.maximize_window()
#
#
# # Path to the Edge WebDriver
# edge_driver_path = "C:/Users/ravi.malik/Downloads/edgedriver_win64/msedgedriver.exe"
#
# # Set up Edge options
# edge_options = Options()
# edge_options.add_argument("--start-maximized")  # Optional: Start maximized
#
# # Initialize the Edge WebDriver
# driver = webdriver.Edge(service=Service(edge_driver_path), options=edge_options)
#
# # Open a URL
# driver.get("https://www.example.com")



def test_find_repeated_letters(input_string):
    # Create a dictionary to store the count of each character
    char_count = {}

    # Convert the string in lowercase to make it case-insensitive.
    input_string = input_string.lower()

    # Iterate through each character in the string
    for char in input_string:
        # If the character is a letter, update its count in the dictionary
        if char.isalpha():
            char_count[char] = char_count.get(char,0)+ 1
    repeated_chars = {char: count for char,  count in char_count.items() if count > 1}
    return repeated_chars

input_string = input("What is the String please enter here : ")
repeated_letters = test_find_repeated_letters(input_string)
print("Repeated Letters", repeated_letters)
