from xmlrpc.server import SimpleXMLRPCServer
import xml.etree.ElementTree as ET
import requests

# Load the existing XML database
xml_file_path = 'Z:\\rpc_assg2\\notes_database.xml'
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Function to process client's input
def process_input(topic, text, timestamp):
    # Check if the topic exists
    topic_element = root.find(".//topic[@name='%s']" % topic)
    
    if topic_element is not None:
        # Topic exists, append data
        note_element = ET.SubElement(topic_element, 'note')
        note_element.text = text
        note_element.set('timestamp', timestamp)
    else:
        # Topic doesn't exist, create a new entry
        topic_element = ET.SubElement(root, 'topic', {'name': topic})
        note_element = ET.SubElement(topic_element, 'note')
        note_element.text = text
        note_element.set('timestamp', timestamp)

    # Save data to the local XML database
    tree.write(xml_file_path)

# Function to query Wikipedia API for information
def query_wikipedia(topic):
    # Use Wikipedia OpenSearch API to get relevant information
    wikipedia_api_url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'opensearch',
        'search': topic,
        'limit': 1,  # Limiting to one result for simplicity
        'format': 'json'
    }

    response = requests.get(wikipedia_api_url, params=params)
    data = response.json()

    if data and len(data) >= 3 and len(data[1]) > 0:
        # Get the first result and return the link
        link = data[3][0]
        return link
    else:
        return "No information found on Wikipedia."


# Function to get contents from the XML database based on a given topic
def get_contents(topic):
    topic_element = root.find(".//topic[@name='%s']" % topic)

    if topic_element is not None:
        # Retrieve all notes under the specified topic
        notes = [{'timestamp': note.get('timestamp'), 'text': note.text} for note in topic_element.findall('note')]
        return notes
    else:
        return None    

# Function to query Wikipedia for information and update the XML database
def query_wikipedia_and_update(topic):
    # Use Wikipedia OpenSearch API to get relevant information
    wikipedia_api_url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'opensearch',
        'search': topic,
        'limit': 1,  # Limiting to one result for simplicity
        'format': 'json'
    }

    response = requests.get(wikipedia_api_url, params=params)
    data = response.json()

    if data and len(data) >= 3 and len(data[1]) > 0:
        # Get the first result and extract relevant information
        link = data[3][0]
        title = data[1][0]
        history = data[2][0]

        # Add relevant information to user-submitted topic in the XML database
        topic_element = root.find(".//topic[@name='%s']" % topic)

        if topic_element is not None:
            info_element = ET.SubElement(topic_element, 'info')
            link_element = ET.SubElement(info_element, 'link')
            link_element.text = link
            title_element = ET.SubElement(info_element, 'title')
            title_element.text = title
            summary_element = ET.SubElement(info_element, 'history')
            summary_element.text = history

            # Save data to the local XML database
            tree.write(xml_file_path)

        return f"Information added to '{topic}' from Wikipedia. Link: {link}"
    else:
        return f"No information found on Wikipedia for '{topic}'."    

# Create an XML-RPC server
server = SimpleXMLRPCServer(('localhost', 8000), logRequests=True, allow_none=True)

# Register functions for the client to call
server.register_function(process_input, 'process_input')
server.register_function(query_wikipedia, 'query_wikipedia')


# Register the get_contents function for the client to call
server.register_function(get_contents, 'get_contents')

# Register the query_wikipedia_and_update function for the client to call
server.register_function(query_wikipedia_and_update, 'query_wikipedia_and_update')


# Run the server
print("Server is ready to accept requests.")
server.serve_forever()





