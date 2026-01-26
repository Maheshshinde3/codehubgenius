from app.models import Question, Option  # replace your_app_name

questions = [
    {"question": "What does LAN stand for?", "option1": "Local Area Network", "option2": "Large Area Network", "option3": "Long Access Network", "option4": "Low Area Network", "answer": "Local Area Network"},
    {"question": "Which device connects multiple networks together?", "option1": "Switch", "option2": "Router", "option3": "Hub", "option4": "Repeater", "answer": "Router"},
    {"question": "What layer of the OSI model is responsible for data encryption?", "option1": "Application", "option2": "Presentation", "option3": "Session", "option4": "Transport", "answer": "Presentation"},
    {"question": "Which protocol is used to send emails?", "option1": "HTTP", "option2": "SMTP", "option3": "FTP", "option4": "IMAP", "answer": "SMTP"},
    {"question": "What does IP stand for in networking?", "option1": "Internet Protocol", "option2": "Internal Processing", "option3": "Integrated Protocol", "option4": "Internet Port", "answer": "Internet Protocol"},
    {"question": "Which topology has all devices connected to a central hub?", "option1": "Bus", "option2": "Ring", "option3": "Star", "option4": "Mesh", "answer": "Star"},
    {"question": "What is the main purpose of a switch?", "option1": "Connect networks", "option2": "Filter and forward data within a network", "option3": "Provide IP addresses", "option4": "Store network data", "answer": "Filter and forward data within a network"},
    {"question": "Which protocol is used to transfer files over the Internet?", "option1": "HTTP", "option2": "FTP", "option3": "SMTP", "option4": "DNS", "answer": "FTP"},
    {"question": "What type of IP address is 192.168.1.1?", "option1": "Public", "option2": "Private", "option3": "Dynamic", "option4": "Reserved", "answer": "Private"},
    {"question": "Which layer of OSI is responsible for reliable data delivery?", "option1": "Network", "option2": "Transport", "option3": "Data Link", "option4": "Physical", "answer": "Transport"},
    {"question": "What does DNS stand for?", "option1": "Domain Name System", "option2": "Digital Network Service", "option3": "Data Name Server", "option4": "Domain Node Service", "answer": "Domain Name System"},
    {"question": "Which device regenerates signals to extend the network range?", "option1": "Hub", "option2": "Router", "option3": "Repeater", "option4": "Switch", "answer": "Repeater"},
    {"question": "Which topology provides the highest redundancy?", "option1": "Bus", "option2": "Ring", "option3": "Star", "option4": "Mesh", "answer": "Mesh"},
    {"question": "Which protocol is used to retrieve emails?", "option1": "SMTP", "option2": "POP3", "option3": "FTP", "option4": "HTTP", "answer": "POP3"},
    {"question": "What is the purpose of a firewall?", "option1": "Connect networks", "option2": "Filter network traffic for security", "option3": "Assign IP addresses", "option4": "Store network logs", "answer": "Filter network traffic for security"},
    {"question": "Which protocol provides secure communication over the Internet?", "option1": "HTTP", "option2": "HTTPS", "option3": "FTP", "option4": "SMTP", "answer": "HTTPS"},
    {"question": "Which layer of OSI converts data into signals?", "option1": "Network", "option2": "Data Link", "option3": "Physical", "option4": "Transport", "answer": "Physical"},
    {"question": "What does MAC address stand for?", "option1": "Media Access Control", "option2": "Main Access Code", "option3": "Media Assigned Code", "option4": "Machine Access Control", "answer": "Media Access Control"},
    {"question": "Which protocol resolves domain names to IP addresses?", "option1": "HTTP", "option2": "DNS", "option3": "FTP", "option4": "SMTP", "answer": "DNS"},
    {"question": "Which network type covers a large geographic area?", "option1": "LAN", "option2": "MAN", "option3": "WAN", "option4": "PAN", "answer": "WAN"},
    {"question": "Which device works at both Data Link and Physical layers?", "option1": "Hub", "option2": "Switch", "option3": "Router", "option4": "Repeater", "answer": "Switch"},
    {"question": "What is the purpose of DHCP?", "option1": "Assign IP addresses automatically", "option2": "Filter network traffic", "option3": "Resolve domain names", "option4": "Encrypt data", "answer": "Assign IP addresses automatically"},
    {"question": "Which layer of OSI provides logical addressing?", "option1": "Network", "option2": "Transport", "option3": "Data Link", "option4": "Application", "answer": "Network"},
    {"question": "Which topology uses a single backbone cable?", "option1": "Star", "option2": "Bus", "option3": "Ring", "option4": "Mesh", "answer": "Bus"},
    {"question": "Which protocol ensures data integrity during transmission?", "option1": "TCP", "option2": "UDP", "option3": "IP", "option4": "ICMP", "answer": "TCP"},
    {"question": "Which network layer handles routing?", "option1": "Transport", "option2": "Network", "option3": "Data Link", "option4": "Session", "answer": "Network"},
    {"question": "What type of network uses Bluetooth to connect devices?", "option1": "LAN", "option2": "MAN", "option3": "PAN", "option4": "WAN", "answer": "PAN"},
    {"question": "Which protocol is connectionless?", "option1": "TCP", "option2": "UDP", "option3": "HTTP", "option4": "SMTP", "answer": "UDP"},
    {"question": "Which layer of OSI compresses data?", "option1": "Application", "option2": "Presentation", "option3": "Session", "option4": "Transport", "answer": "Presentation"},
    {"question": "Which device forwards data based on MAC addresses?", "option1": "Router", "option2": "Switch", "option3": "Hub", "option4": "Firewall", "answer": "Switch"},
    {"question": "Which layer of OSI establishes, manages, and terminates connections?", "option1": "Session", "option2": "Transport", "option3": "Network", "option4": "Application", "answer": "Session"},
    {"question": "Which protocol provides IP address and subnet mask to devices?", "option1": "DNS", "option2": "DHCP", "option3": "FTP", "option4": "HTTP", "answer": "DHCP"},
    {"question": "Which layer of OSI detects and corrects errors?", "option1": "Data Link", "option2": "Network", "option3": "Transport", "option4": "Application", "answer": "Data Link"},
    {"question": "Which protocol is used to browse the web?", "option1": "HTTP", "option2": "FTP", "option3": "SMTP", "option4": "IMAP", "answer": "HTTP"},
    {"question": "Which type of cable is used in Ethernet networks?", "option1": "Coaxial", "option2": "Twisted Pair", "option3": "Fiber Optic", "option4": "All of the above", "answer": "All of the above"},
    {"question": "What does ARP stand for?", "option1": "Address Resolution Protocol", "option2": "Application Routing Protocol", "option3": "Automatic Routing Process", "option4": "Address Routing Procedure", "answer": "Address Resolution Protocol"},
    {"question": "Which layer adds logical addresses to data?", "option1": "Network", "option2": "Transport", "option3": "Data Link", "option4": "Physical", "answer": "Network"},
    {"question": "Which protocol is used for secure file transfer?", "option1": "FTP", "option2": "SFTP", "option3": "SMTP", "option4": "HTTP", "answer": "SFTP"},
    {"question": "What is the purpose of a gateway?", "option1": "Connect different networks", "option2": "Filter traffic", "option3": "Provide IP addresses", "option4": "Encrypt data", "answer": "Connect different networks"},
    {"question": "Which device operates only at the Physical layer?", "option1": "Hub", "option2": "Switch", "option3": "Router", "option4": "Firewall", "answer": "Hub"},
    {"question": "Which protocol is used to check network connectivity?", "option1": "ICMP", "option2": "TCP", "option3": "UDP", "option4": "FTP", "answer": "ICMP"},
    {"question": "Which type of transmission is used in full-duplex communication?", "option1": "One-way", "option2": "Two-way simultaneously", "option3": "Two-way alternately", "option4": "Broadcast only", "answer": "Two-way simultaneously"},
    {"question": "Which topology connects devices in a closed loop?", "option1": "Bus", "option2": "Ring", "option3": "Star", "option4": "Mesh", "answer": "Ring"},
    {"question": "Which protocol resolves MAC addresses to IP addresses?", "option1": "ARP", "option2": "RARP", "option3": "DHCP", "option4": "DNS", "answer": "RARP"},
    {"question": "Which layer of OSI provides end-to-end communication?", "option1": "Transport", "option2": "Network", "option3": "Data Link", "option4": "Session", "answer": "Transport"},
    {"question": "Which type of network cable is immune to electromagnetic interference?", "option1": "Coaxial", "option2": "Twisted Pair", "option3": "Fiber Optic", "option4": "None", "answer": "Fiber Optic"},
    {"question": "Which layer of OSI handles flow control?", "option1": "Network", "option2": "Transport", "option3": "Data Link", "option4": "Application", "answer": "Transport"},
    {"question": "Which protocol is used for sending messages over the Internet?", "option1": "HTTP", "option2": "SMTP", "option3": "FTP", "option4": "DNS", "answer": "SMTP"},
    {"question": "Which topology requires the least amount of cable?", "option1": "Star", "option2": "Bus", "option3": "Ring", "option4": "Mesh", "answer": "Bus"},
    {"question": "Which device prevents unauthorized access to a network?", "option1": "Switch", "option2": "Router", "option3": "Firewall", "option4": "Hub", "answer": "Firewall"},
    {"question": "Which layer of OSI is closest to the end user?", "option1": "Application", "option2": "Presentation", "option3": "Session", "option4": "Transport", "answer": "Application"},
    {"question": "Which protocol is faster but unreliable?", "option1": "TCP", "option2": "UDP", "option3": "HTTP", "option4": "SMTP", "answer": "UDP"},
    {"question": "Which layer of OSI establishes logical connections between devices?", "option1": "Session", "option2": "Transport", "option3": "Network", "option4": "Data Link", "answer": "Session"},
    {"question": "Which device can filter traffic based on IP address?", "option1": "Switch", "option2": "Hub", "option3": "Router", "option4": "Repeater", "answer": "Router"},
    {"question": "Which protocol is used to securely access remote systems?", "option1": "FTP", "option2": "SSH", "option3": "HTTP", "option4": "SMTP", "answer": "SSH"},
    {"question": "Which layer of OSI defines data format and syntax?", "option1": "Application", "option2": "Presentation", "option3": "Session", "option4": "Transport", "answer": "Presentation"},
    {"question": "Which topology provides point-to-point connection between all devices?", "option1": "Star", "option2": "Bus", "option3": "Ring", "option4": "Mesh", "answer": "Mesh"},
]

for q in questions:
    # Create the question
    question_obj = Question.objects.create(text=q["question"])
    print(f"Added question: {q['question']}")

    # Create options
    for i in range(1, 5):
        option_text = q[f"option{i}"]
        is_correct = (option_text == q["answer"])
        opt = Option.objects.create(question=question_obj, text=option_text, is_correct=is_correct)
        print(f"  Added option: {option_text} | Correct: {is_correct}")

print("All questions and options added!")




# Steps for adding new questions of other subject 
# 1. create new model and assign it in admin panel 
# 2. here in these script change the model name
# 3. change question and answers 
# 4. open shell using command - python manage.py shell
# 5. type command exec(open("newone.py").read())