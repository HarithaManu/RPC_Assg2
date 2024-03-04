import xmlrpc.client

# Create an XML-RPC client
client = xmlrpc.client.ServerProxy('http://localhost:8000')

# Function to send user input to the server
def send_user_input():
    topic = input("Enter the topic: ")
    text = input("Enter the note text: ")
    timestamp = input("Enter the timestamp: ")

    # Call the server's process_input function
    client.process_input(topic, text, timestamp)

# Function to get contents from the XML database based on a given topic
def get_contents_from_database():
    topic = input("Enter the topic to retrieve: ")

    # Call the server's get_contents function
    contents = client.get_contents(topic)

    if contents:
        print(f"Contents for topic '{topic}':")
        for note in contents:
            print(f"Timestamp: {note['timestamp']}, Note: {note['text']}")
    else:
        print(f"No contents found for topic '{topic}'.")

# Function to query Wikipedia API for information
def query_wikipedia():
    topic = input("Enter the topic to search on Wikipedia: ")

    # Call the server's query_wikipedia function
    result = client.query_wikipedia(topic)

    print(result)

def query_wikipedia_and_append():
    topic = input("Enter the topic to search on Wikipedia: ")

    # Call the server's query_wikipedia_and_update function
    result = client.query_wikipedia_and_update(topic)

    print(result)

# Menu for the client
while True:
    print("\n1. Send user input to server")
    print("2. Get contents from the XML database based on a given topic")
    print("3. Query Wikipedia for information on a topic")
    print("4. Exit")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        send_user_input()
    elif choice == 2:
        get_contents_from_database()
    elif choice == 3:
        query_wikipedia_and_append()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")
