import streamlit as st
import random

# Extended quiz questions database
quiz_data = {
    "cybersecurity": {
        "easy": [
            {"question": "CIA stands for?", "options": ["Confidentiality, Integrity, Availability", "Confidentiality, Identity, Authorization", "Configuration, Integrity, Accessibility", "Confidentiality, Identity, Availability"], "answer": "Confidentiality, Integrity, Availability"},
            {"question": "What is a VPN used for?", "options": ["Speed Boost", "File Sharing", "Network Security", "Data Deletion"], "answer": "Network Security"},
            {"question": "What does HTTP stand for?", "options": ["HyperText Transfer Protocol", "High Transfer Tunnel Protocol", "HyperText Transfer Program", "High Traffic Transfer Protocol"], "answer": "HyperText Transfer Protocol"},
            {"question": "Which one is a type of malware?", "options": ["Firewall", "Router", "Trojan", "Switch"], "answer": "Trojan"},
            {"question": "Which tool is used for penetration testing?", "options": ["Photoshop", "Wireshark", "Excel", "Apache"], "answer": "Wireshark"},
            {"question": "What does phishing aim to do?", "options": ["Increase network speed", "Steal sensitive information", "Encrypt files", "Filter traffic"], "answer": "Steal sensitive information"},
            {"question": "Which protocol is used for secure communication?", "options": ["HTTP", "HTTPS", "FTP", "SMTP"], "answer": "HTTPS"},
            {"question": "What is the purpose of a DMZ?", "options": ["Increase bandwidth", "Isolate external services", "Store backup data", "Monitor network speed"], "answer": "Isolate external services"},
            {"question": "What is the first step in the incident response process?", "options": ["Preparation", "Detection", "Containment", "Eradication"], "answer": "Preparation"},
            {"question": "Which type of attack targets personal information?", "options": ["DDoS", "Phishing", "SQL Injection", "MitM"], "answer": "Phishing"},
            {"question": "What is a common method to secure data in transit?", "options": ["Encryption", "Compression", "Decryption", "Transcoding"], "answer": "Encryption"},
            {"question": "Which technology helps to prevent unauthorized access?", "options": ["Antivirus", "Firewall", "Router", "Switch"], "answer": "Firewall"},
            {"question": "What does MFA stand for?", "options": ["Multi-Factor Authentication", "Multi-File Access", "Multi-Factor Analysis", "Multiple Frequency Authentication"], "answer": "Multi-Factor Authentication"},
            {"question": "Which attack involves overwhelming a server?", "options": ["Phishing", "DDoS", "Man-in-the-Middle", "SQL Injection"], "answer": "DDoS"},
            {"question": "What is the purpose of penetration testing?", "options": ["Improve speed", "Identify vulnerabilities", "Backup data", "Encrypt files"], "answer": "Identify vulnerabilities"},
            {"question": "Which encryption standard is widely used?", "options": ["AES", "RSA", "SHA-256", "MD5"], "answer": "AES"},
            {"question": "What does a brute-force attack involve?", "options": ["Social engineering", "Guessing passwords", "Phishing", "SQL injection"], "answer": "Guessing passwords"},
            {"question": "What is a common cause of data breaches?", "options": ["Outdated software", "Fast internet", "Firewalls", "Backup systems"], "answer": "Outdated software"},
            {"question": "What does an IDS do?", "options": ["Prevents attacks", "Detects attacks", "Encrypts data", "Stores logs"], "answer": "Detects attacks"},
            {"question": "What is the main purpose of an SSL certificate?", "options": ["To encrypt data", "To speed up websites", "To increase bandwidth", "To store data"], "answer": "To encrypt data"},
            {"question": "What does the term 'malware' refer to?", "options": ["Good software", "Malicious software", "Network monitoring software", "Data recovery software"], "answer": "Malicious software"},
        ],
        "medium": [
            {"question": "What does SSL stand for?", "options": ["Secure Socket Layer", "Secure System Layer", "System Socket Layer", "Secure Socket Link"], "answer": "Secure Socket Layer"},
            {"question": "A firewall is used to:", "options": ["Increase Internet Speed", "Filter Network Traffic", "Monitor Disk Usage", "Encrypt Data"], "answer": "Filter Network Traffic"},
            {"question": "What is social engineering?", "options": ["A coding language", "A human-based hacking method", "A security protocol", "A firewall configuration"], "answer": "A human-based hacking method"},
            {"question": "Which is a common hashing algorithm?", "options": ["SHA-256", "DNS", "TCP", "UDP"], "answer": "SHA-256"},
            {"question": "Ransomware typically:", "options": ["Deletes files", "Locks data until payment", "Increases storage", "Speeds up the system"], "answer": "Locks data until payment"},
            {"question": "What is a common threat to cloud security?", "options": ["Data loss", "Reduced latency", "Improved bandwidth", "More accessibility"], "answer": "Data loss"},
            {"question": "What does the term 'zero-day vulnerability' mean?", "options": ["A vulnerability that has not been patched", "A type of malware", "An outdated application", "A secure application"], "answer": "A vulnerability that has not been patched"},
            {"question": "What does the principle of least privilege refer to?", "options": ["Everyone has full access", "Access based on necessity", "Full access for all admins", "No access for anyone"], "answer": "Access based on necessity"},
            {"question": "What type of attack exploits vulnerabilities in web applications?", "options": ["DDoS", "SQL Injection", "Phishing", "Sniffing"], "answer": "SQL Injection"},
            {"question": "What does 'data breach' mean?", "options": ["Data is lost", "Unauthorized access to data", "Data is backed up", "Data is encrypted"], "answer": "Unauthorized access to data"},
            {"question": "Which of the following is a strong password?", "options": ["123456", "password", "MyP@ssw0rd!", "qwerty"], "answer": "MyP@ssw0rd!"},
            {"question": "What is a VPN primarily used for?", "options": ["Remote access", "Streaming", "Gaming", "File sharing"], "answer": "Remote access"},
            {"question": "What is the purpose of a digital certificate?", "options": ["To sign documents", "To encrypt emails", "To verify identity", "To create backups"], "answer": "To verify identity"},
            {"question": "Which of the following is NOT a type of malware?", "options": ["Trojan", "Worm", "Virus", "Router"], "answer": "Router"},
            {"question": "What does DDoS stand for?", "options": ["Distributed Denial of Service", "Direct Denial of Service", "Data Denial of Service", "Dynamic Denial of Service"], "answer": "Distributed Denial of Service"},
            {"question": "What does 'phishing' mean?", "options": ["Fishing for data", "Searching for passwords", "A type of malware", "An encryption method"], "answer": "Fishing for data"},
            {"question": "What is a common method for ensuring data integrity?", "options": ["Checksum", "Encryption", "Backup", "Compression"], "answer": "Checksum"},
            {"question": "What is the role of a Security Information and Event Management (SIEM) system?", "options": ["To manage security policies", "To analyze security alerts", "To prevent attacks", "To manage user access"], "answer": "To analyze security alerts"},
            {"question": "What does the term 'malware' refer to?", "options": ["Malicious software", "Useful software", "Open-source software", "Public domain software"], "answer": "Malicious software"},
            {"question": "What is a keylogger?", "options": ["Software that monitors keystrokes", "Hardware for logging data", "A data recovery tool", "A network security tool"], "answer": "Software that monitors keystrokes"},
            {"question": "What does 'ransomware' do?", "options": ["Steals information", "Encrypts data and demands payment", "Deletes files", "Increases bandwidth"], "answer": "Encrypts data and demands payment"},
        ],
        "hard": [
            {"question": "NIST is known for its:", "options": ["Hardware Standards", "Cybersecurity Framework", "Educational Courses", "Virus Definitions"], "answer": "Cybersecurity Framework"},
            {"question": "XSS stands for:", "options": ["Cross-Site Scripting", "Cross Server Scripting", "External Site Scripting", "None of the above"], "answer": "Cross-Site Scripting"},
            {"question": "What is SQL Injection?", "options": ["Inserting code into a database query", "Using encrypted code", "Adding security patches", "Connecting to a VPN"], "answer": "Inserting code into a database query"},
            {"question": "What does IDS stand for?", "options": ["Intrusion Detection System", "Internet Data System", "Internal Data Security", "Internet Detection Service"], "answer": "Intrusion Detection System"},
            {"question": "What is the purpose of encryption?", "options": ["To scramble data", "To speed up network", "To compress files", "To clear memory"], "answer": "To scramble data"},
        ],
    },
    #ai

    "ai":{
    "easy": [
        {"question": "What does AI stand for?", "options": ["Artificial Intelligence", "Automated Integration", "Artificial Integration", "Automated Intelligence"], "answer": "Artificial Intelligence"},
        {"question": "Which of these is a type of AI?", "options": ["Weak AI", "Strong AI", "Narrow AI", "All of the above"], "answer": "All of the above"},
        {"question": "What is machine learning?", "options": ["A subset of AI", "A programming language", "A type of database", "A hardware component"], "answer": "A subset of AI"},
        {"question": "What is the purpose of neural networks?", "options": ["To analyze data", "To mimic human brain functions", "To store data", "To provide internet security"], "answer": "To mimic human brain functions"},
        {"question": "Which company developed the AI program Watson?", "options": ["Google", "IBM", "Microsoft", "Facebook"], "answer": "IBM"},
        # Additional easy questions
        {"question": "What is natural language processing?", "options": ["AI understanding human language", "Programming in natural languages", "An AI programming language", "None of the above"], "answer": "AI understanding human language"},
        {"question": "What is an example of a virtual assistant?", "options": ["Cortana", "Alexa", "Siri", "All of the above"], "answer": "All of the above"},
        {"question": "What type of learning involves reward-based learning?", "options": ["Supervised learning", "Unsupervised learning", "Reinforcement learning", "None of the above"], "answer": "Reinforcement learning"},
        {"question": "What is the Turing Test used for?", "options": ["To test a computer's intelligence", "To evaluate programming skills", "To measure speed", "To analyze data"], "answer": "To test a computer's intelligence"},
        {"question": "Which language is commonly used for AI development?", "options": ["Java", "Python", "C++", "All of the above"], "answer": "All of the above"},
        {"question": "What does deep learning refer to?", "options": ["Learning at a basic level", "Learning using neural networks", "Learning through reinforcement", "Learning from mistakes"], "answer": "Learning using neural networks"},
        {"question": "Which AI technique is used for recommendation systems?", "options": ["Clustering", "Classification", "Regression", "Collaborative filtering"], "answer": "Collaborative filtering"},
        {"question": "What is computer vision?", "options": ["Teaching computers to see", "Programming visual displays", "Creating graphics", "None of the above"], "answer": "Teaching computers to see"},
        {"question": "What is a chatbot?", "options": ["A robot for chat", "An AI that simulates conversation", "A type of AI hardware", "None of the above"], "answer": "An AI that simulates conversation"},
        {"question": "What does 'training a model' mean in AI?", "options": ["Preparing a model for use", "Teaching a model to learn from data", "Creating a model", "None of the above"], "answer": "Teaching a model to learn from data"},
        {"question": "What is a dataset?", "options": ["A collection of data", "A model", "An AI algorithm", "A programming language"], "answer": "A collection of data"},
        {"question": "Which is a key component of AI systems?", "options": ["Algorithms", "Data", "Hardware", "All of the above"], "answer": "All of the above"},
        {"question": "What is supervised learning?", "options": ["Learning without labeled data", "Learning with labeled data", "Learning from experience", "Learning from feedback"], "answer": "Learning with labeled data"},
        {"question": "What is a common use of AI in healthcare?", "options": ["Medical diagnosis", "Patient monitoring", "Predictive analytics", "All of the above"], "answer": "All of the above"},
        {"question": "What does reinforcement learning focus on?", "options": ["Learning from labeled data", "Learning from rewards", "Learning from visual inputs", "Learning from history"], "answer": "Learning from rewards"},
    ],
    "medium": [
        {"question": "What is a generative adversarial network (GAN)?", "options": ["A type of neural network", "A learning model that generates new data", "A system for fighting AI", "None of the above"], "answer": "A learning model that generates new data"},
        {"question": "Which algorithm is commonly used for classification tasks?", "options": ["K-means", "Decision Tree", "Linear Regression", "None of the above"], "answer": "Decision Tree"},
        {"question": "What is overfitting in machine learning?", "options": ["Model is too simple", "Model performs well on training data but poorly on new data", "Model performs well on new data", "None of the above"], "answer": "Model performs well on training data but poorly on new data"},
        {"question": "What is feature extraction?", "options": ["Selecting relevant features for model training", "Creating new data", "Removing data", "None of the above"], "answer": "Selecting relevant features for model training"},
        {"question": "What is natural language generation (NLG)?", "options": ["Converting text to speech", "Generating text from data", "Understanding human language", "Translating languages"], "answer": "Generating text from data"},
        # Additional medium questions
        {"question": "Which technique is used for dimensionality reduction?", "options": ["Principal Component Analysis", "Support Vector Machines", "Random Forest", "Clustering"], "answer": "Principal Component Analysis"},
        {"question": "What is the purpose of transfer learning?", "options": ["Applying knowledge from one domain to another", "Training from scratch", "Improving data quality", "All of the above"], "answer": "Applying knowledge from one domain to another"},
        {"question": "What does NLP stand for?", "options": ["Natural Language Processing", "Neural Language Programming", "Natural Learning Process", "None of the above"], "answer": "Natural Language Processing"},
        {"question": "Which AI technique is used in self-driving cars?", "options": ["Reinforcement learning", "Supervised learning", "Clustering", "All of the above"], "answer": "All of the above"},
        {"question": "What is a support vector machine?", "options": ["A type of neural network", "A supervised learning model", "An unsupervised learning model", "A reinforcement learning model"], "answer": "A supervised learning model"},
        ],
    },

#civil
    "civil_engineering": {
        "easy": [
            {"question": "What is the primary purpose of surveying?", 
             "options": ["Measure land area", "Determine land boundaries", "Create maps", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "What instrument is commonly used for measuring angles in surveying?", 
             "options": ["Theodolite", "Total Station", "Level", "Tape measure"], 
             "answer": "Theodolite"},
             
            {"question": "Which type of surveying uses satellites for determining precise locations?", 
             "options": ["Triangulation", "GPS Surveying", "Leveling", "Tacheometry"], 
             "answer": "GPS Surveying"},
             
            {"question": "In leveling, what is the term for the difference in elevation between two points?", 
             "options": ["Slope", "Rise", "Fall", "Vertical Distance"], 
             "answer": "Vertical Distance"},
             
            {"question": "What does the term 'benchmark' refer to in surveying?", 
             "options": ["A fixed reference point", "A type of measurement", "A surveying tool", "A type of map"], 
             "answer": "A fixed reference point"},
             
            {"question": "What is the primary function of a total station?", 
             "options": ["Measuring angles", "Measuring distances", "Both a and b", "Creating maps"], 
             "answer": "Both a and b"},
             
            {"question": "Which method of surveying is used for determining the area of irregular plots?", 
             "options": ["Cross-Section Method", "Planimeter Method", "Rectangular Method", "Chain Surveying"], 
             "answer": "Planimeter Method"},
             
            {"question": "What does a leveling rod measure?", 
             "options": ["Distance", "Angle", "Elevation", "Area"], 
             "answer": "Elevation"},
             
            {"question": "What is the main purpose of using a dumpy level?", 
             "options": ["Measuring angles", "Establishing horizontal lines", "Finding distances", "Mapping"], 
             "answer": "Establishing horizontal lines"},
             
            {"question": "In surveying, what is a traverse?", 
             "options": ["A series of connected lines", "An elevation change", "A mapping technique", "None of the above"], 
             "answer": "A series of connected lines"},
             {"question": "What is the primary purpose of a foundation?", 
             "options": ["To provide support", "To create space", "To add aesthetics", "To connect structures"], 
             "answer": "To provide support"},
             
            {"question": "Which material is commonly used for constructing beams?", 
             "options": ["Concrete", "Glass", "Plastic", "Wood"], 
             "answer": "Concrete"},
             
            {"question": "What is a load-bearing wall?", 
             "options": ["A wall that supports weight from above", "A decorative wall", "A partition wall", "An external wall"], 
             "answer": "A wall that supports weight from above"},
             
            {"question": "What is the unit of measurement for concrete strength?", 
             "options": ["Pascals", "Kilograms", "Newtons", "Metres"], 
             "answer": "Pascals"},
             
            {"question": "What is the main purpose of a retaining wall?", 
             "options": ["To hold back soil", "To enhance aesthetics", "To support beams", "To connect structures"], 
             "answer": "To hold back soil"},
             
            {"question": "What does the term 'civil engineering' encompass?", 
             "options": ["Infrastructure design and construction", "Only buildings", "Environmental studies", "Transportation only"], 
             "answer": "Infrastructure design and construction"},
             
            {"question": "Which of the following is a common surveying instrument?", 
             "options": ["Theodolite", "Compass", "Ruler", "Tape measure"], 
             "answer": "Theodolite"},
             
            {"question": "What is the function of a cross-section in civil engineering?", 
             "options": ["To show internal features of a structure", "To display a landscape", "To represent dimensions", "To provide color"], 
             "answer": "To show internal features of a structure"},
             
            {"question": "What is the role of a civil engineer?", 
             "options": ["Design and oversee construction projects", "Only manage finances", "Conduct environmental studies", "Create art"], 
             "answer": "Design and oversee construction projects"},
             
            {"question": "What does 'shear strength' refer to in soil mechanics?", 
             "options": ["Resistance to sliding", "Resistance to compression", "Resistance to tension", "Resistance to bending"], 
             "answer": "Resistance to sliding"},
        ],
        "medium": [
            {"question": "What is the main material used in concrete?", 
             "options": ["Cement", "Sand", "Gravel", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "What is the primary purpose of a retaining wall?", 
             "options": ["Support structures", "Prevent soil erosion", "Hold back soil", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "Which type of foundation is best suited for weak soil?", 
             "options": ["Shallow foundation", "Deep foundation", "Strip foundation", "Pad foundation"], 
             "answer": "Deep foundation"},
             
            {"question": "What is the modulus of elasticity?", 
             "options": ["Measure of material stiffness", "Measure of tensile strength", "Measure of hardness", "None of the above"], 
             "answer": "Measure of material stiffness"},
             
            {"question": "What does the term 'slump' refer to in concrete?", 
             "options": ["Consistency of concrete", "Type of aggregate", "Curing process", "None of the above"], 
             "answer": "Consistency of concrete"},
             
            {"question": "Which is a common type of bridge?", 
             "options": ["Suspension bridge", "Arch bridge", "Beam bridge", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "What is the primary purpose of a water treatment plant?", 
             "options": ["To purify water", "To store water", "To distribute water", "To measure water quality"], 
             "answer": "To purify water"},
             
            {"question": "What is the ideal water-cement ratio for concrete?", 
             "options": ["1:1", "1:2", "1:3", "0.4 to 0.6"], 
             "answer": "0.4 to 0.6"},
             
            {"question": "Which material is used for making bricks?", 
             "options": ["Clay", "Cement", "Sand", "Gravel"], 
             "answer": "Clay"},
             
            {"question": "What does the term 'shear strength' refer to in materials?", 
             "options": ["Resistance to shearing forces", "Resistance to tensile forces", "Resistance to compressive forces", "None of the above"], 
             "answer": "Resistance to shearing forces"},
             {"question": "What is the primary purpose of concrete admixtures?", 
             "options": ["To modify properties of concrete", "To enhance color", "To reduce cost", "To increase volume"], 
             "answer": "To modify properties of concrete"},
             
            {"question": "Which test is commonly used to determine the compressive strength of concrete?", 
             "options": ["Slump test", "Cube test", "Tensile test", "Bending test"], 
             "answer": "Cube test"},
             
            {"question": "What does the term 'hydraulic' refer to in civil engineering?", 
             "options": ["Related to water movement", "Related to air", "Related to soil", "None of the above"], 
             "answer": "Related to water movement"},
             
            {"question": "Which material is primarily used in road construction?", 
             "options": ["Asphalt", "Glass", "Brick", "Wood"], 
             "answer": "Asphalt"},
             
            {"question": "What is a civil engineering drawing?", 
             "options": ["A detailed graphic representation", "An artistic sketch", "A random collection of images", "None of the above"], 
             "answer": "A detailed graphic representation"},
             
            {"question": "What is the purpose of a drainage system in civil engineering?", 
             "options": ["To remove excess water", "To provide drinking water", "To decorate landscapes", "To create recreational areas"], 
             "answer": "To remove excess water"},
             
            {"question": "What is the most common type of bridge?", 
             "options": ["Beam bridge", "Arch bridge", "Suspension bridge", "Truss bridge"], 
             "answer": "Beam bridge"},
             
            {"question": "Which soil type is most stable for construction?", 
             "options": ["Clay", "Sand", "Gravel", "Silt"], 
             "answer": "Gravel"},
             
            {"question": "What is the primary goal of structural analysis?", 
             "options": ["To ensure safety and stability", "To enhance aesthetics", "To reduce costs", "To maximize profits"], 
             "answer": "To ensure safety and stability"},
             
            {"question": "What does the term 'earthquake engineering' refer to?", 
             "options": ["Designing structures to withstand earthquakes", "Creating buildings", "Planning cities", "None of the above"], 
             "answer": "Designing structures to withstand earthquakes"},
        ],
        "hard": [
            {"question": "What is a common method for testing the strength of concrete?", 
             "options": ["Compression test", "Tension test", "Bending test", "Shear test"], 
             "answer": "Compression test"},
             
            {"question": "What is the purpose of a construction schedule?", 
             "options": ["To outline project phases", "To allocate resources", "To manage timelines", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "Which type of survey is used for highway construction?", 
             "options": ["Topographic Survey", "Boundary Survey", "Control Survey", "Route Survey"], 
             "answer": "Route Survey"},
             
            {"question": "What does 'load bearing' refer to in structures?", 
             "options": ["Carrying weight", "Resisting pressure", "Holding moisture", "None of the above"], 
             "answer": "Carrying weight"},
             
            {"question": "What is the primary function of a geotechnical engineer?", 
             "options": ["Design buildings", "Study soil properties", "Plan transportation", "Manage construction projects"], 
             "answer": "Study soil properties"},
             {"question": "What is the primary function of a geotechnical engineer?", 
             "options": ["To study soil and rock behavior", "To design bridges", "To plan cities", "To manage construction projects"], 
             "answer": "To study soil and rock behavior"},
             
            {"question": "What is the significance of a concrete mix design?", 
             "options": ["To achieve desired strength and durability", "To increase cost", "To reduce material use", "None of the above"], 
             "answer": "To achieve desired strength and durability"},
             
            {"question": "What is a common method for soil stabilization?", 
             "options": ["Compaction", "Painting", "Heating", "Cooling"], 
             "answer": "Compaction"},
             
            {"question": "What is the role of a project manager in civil engineering?", 
             "options": ["To oversee construction projects", "To design structures", "To perform surveys", "To conduct experiments"], 
             "answer": "To oversee construction projects"},
             
            {"question": "What is the term for the maximum load a structure can safely carry?", 
             "options": ["Dead load", "Live load", "Ultimate load", "Service load"], 
             "answer": "Ultimate load"},
        ],
    },

    #eg\draw
    "engineering_drawing": {
        "easy": [
            {"question": "What is the purpose of engineering drawing?", 
             "options": ["To communicate ideas", "To record data", "To create designs", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "Which projection method shows the true shape of an object?", 
             "options": ["Orthographic projection", "Isometric projection", "Perspective projection", "Oblique projection"], 
             "answer": "Orthographic projection"},
             
            {"question": "What does a dashed line represent in a drawing?", 
             "options": ["Hidden edges", "Visible edges", "Center lines", "Dimension lines"], 
             "answer": "Hidden edges"},
             
            {"question": "What is the standard unit for measuring angles in engineering drawing?", 
             "options": ["Degrees", "Radians", "Gradians", "Both degrees and radians"], 
             "answer": "Degrees"},
             
            {"question": "What is an isometric drawing?", 
             "options": ["A type of 2D drawing", "A 3D representation where all axes are equally foreshortened", "A projection technique", "A technical sketch"], 
             "answer": "A 3D representation where all axes are equally foreshortened"},
             
            {"question": "What do dimensions indicate in a drawing?", 
             "options": ["Size", "Shape", "Location", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "What is the purpose of a title block in engineering drawings?", 
             "options": ["To provide drawing details", "To add artistic elements", "To show color", "To hide information"], 
             "answer": "To provide drawing details"},
             
            {"question": "Which symbol is used to indicate the center of an arc or circle?", 
             "options": ["A dot", "A cross", "A triangle", "A square"], 
             "answer": "A dot"},
             
            {"question": "What is the primary purpose of a sectional view?", 
             "options": ["To show internal features", "To show external features", "To provide dimensions", "To add aesthetics"], 
             "answer": "To show internal features"},
             
            {"question": "In which view do height and width appear as true size?", 
             "options": ["Top view", "Front view", "Side view", "All views"], 
             "answer": "Front view"},
            {"question": "What is the primary purpose of engineering drawing?", 
             "options": ["To communicate ideas and specifications", "To create art", "To enhance creativity", "To decorate buildings"], 
             "answer": "To communicate ideas and specifications"},
             
            {"question": "What does a scale on a drawing represent?", 
             "options": ["The proportion between the drawing and the real object", "The color of the drawing", "The thickness of lines", "None of the above"], 
             "answer": "The proportion between the drawing and the real object"},
             
            {"question": "Which type of line is used to indicate hidden edges?", 
             "options": ["Dashed line", "Solid line", "Dotted line", "Wavy line"], 
             "answer": "Dashed line"},
             
            {"question": "What is a technical drawing?", 
             "options": ["A precise and detailed drawing", "A random sketch", "An artistic representation", "A blueprint only"], 
             "answer": "A precise and detailed drawing"},
             
            {"question": "What does the term 'dimensioning' refer to in engineering drawing?", 
             "options": ["Adding measurements to a drawing", "Coloring a drawing", "Making a 3D model", "None of the above"], 
             "answer": "Adding measurements to a drawing"},
             
            {"question": "What is the difference between first-angle and third-angle projection?", 
             "options": ["Their orientation in relation to the object", "Their color schemes", "Their line thickness", "Their material used"], 
             "answer": "Their orientation in relation to the object"},
             
            {"question": "Which view is typically shown in a top view?", 
             "options": ["The view from above", "The view from the side", "The view from the front", "The view from below"], 
             "answer": "The view from above"},
             
            {"question": "What is the purpose of a title block in a drawing?", 
             "options": ["To provide information about the drawing", "To make it look good", "To add color", "To show dimensions"], 
             "answer": "To provide information about the drawing"},
             
            {"question": "Which software is commonly used for engineering drawing?", 
             "options": ["AutoCAD", "Photoshop", "Word", "Excel"], 
             "answer": "AutoCAD"},
             
            {"question": "What does 'orthographic projection' help to represent?", 
             "options": ["3D objects in 2D", "2D objects in 3D", "Only line drawings", "None of the above"], 
             "answer": "3D objects in 2D"},
        ],
        "medium": [
            {"question": "What is the purpose of a scale in engineering drawing?", 
             "options": ["To measure length", "To maintain proportion", "To create symmetry", "To indicate materials"], 
             "answer": "To maintain proportion"},
             
            {"question": "What does the term 'dimensioning' refer to?", 
             "options": ["Adding labels", "Measuring angles", "Providing measurements", "Sketching"], 
             "answer": "Providing measurements"},
             
            {"question": "What is a broken view used for?", 
             "options": ["To show hidden details", "To show a portion of an object", "To provide dimensions", "To enhance aesthetics"], 
             "answer": "To show a portion of an object"},
             
            {"question": "Which projection shows three dimensions in one view?", 
             "options": ["Isometric projection", "Axonometric projection", "Orthographic projection", "Oblique projection"], 
             "answer": "Isometric projection"},
             
            {"question": "What is the function of dimension lines?", 
             "options": ["To show size", "To show location", "To show angles", "Both a and b"], 
             "answer": "Both a and b"},
             
            {"question": "What is a fillet?", 
             "options": ["A rounded interior corner", "A rounded exterior corner", "A sharp edge", "A hidden line"], 
             "answer": "A rounded interior corner"},
             
            {"question": "Which type of line indicates an alternate position of an object?", 
             "options": ["Hidden line", "Center line", "Phantom line", "Dimension line"], 
             "answer": "Phantom line"},
             
            {"question": "What does the term 'tolerance' refer to in engineering drawings?", 
             "options": ["Allowable variation in a dimension", "Measurement of angles", "Size of the drawing", "Number of views"], 
             "answer": "Allowable variation in a dimension"},
             
            {"question": "In engineering drawings, what does a 'hatching' pattern indicate?", 
             "options": ["Hidden features", "Sectioned areas", "Dimensions", "None of the above"], 
             "answer": "Sectioned areas"},
             
            {"question": "What is the main purpose of a cross-section view?", 
             "options": ["To provide detailed information", "To show dimensions", "To illustrate the internal features", "To enhance aesthetics"], 
             "answer": "To illustrate the internal features"},
             {"question": "What is a sectional view used for?", 
             "options": ["To show internal features of an object", "To provide colors", "To represent dimensions", "To create perspectives"], 
             "answer": "To show internal features of an object"},
             
            {"question": "What is the function of a reference line in a drawing?", 
             "options": ["To provide a baseline for measurements", "To add colors", "To indicate hidden features", "To make it more complex"], 
             "answer": "To provide a baseline for measurements"},
             
            {"question": "Which type of drawing includes dimensions and tolerances?", 
             "options": ["Detail drawing", "Perspective drawing", "Exploded view", "Isometric drawing"], 
             "answer": "Detail drawing"},
             
            {"question": "What is the primary benefit of using CAD (Computer-Aided Design)?", 
             "options": ["Increased accuracy and efficiency", "More artistic freedom", "Less need for precision", "Simpler than manual drawing"], 
             "answer": "Increased accuracy and efficiency"},
             
            {"question": "What does the symbol 'Φ' represent in engineering drawing?", 
             "options": ["Diameter", "Radius", "Length", "Width"], 
             "answer": "Diameter"},
             
            {"question": "What is the purpose of a bill of materials (BOM) in engineering drawing?", 
             "options": ["To list components and materials required", "To show dimensions", "To provide colors", "None of the above"], 
             "answer": "To list components and materials required"},
             
            {"question": "What is the significance of tolerances in engineering drawings?", 
             "options": ["To specify allowable variations", "To enhance aesthetics", "To reduce costs", "To simplify the drawing"], 
             "answer": "To specify allowable variations"},
             
            {"question": "Which type of projection gives a more realistic view of an object?", 
             "options": ["Perspective projection", "Orthographic projection", "Isometric projection", "Multiview projection"], 
             "answer": "Perspective projection"},
             
            {"question": "What is the purpose of hatching in a drawing?", 
             "options": ["To indicate different materials", "To color the drawing", "To add dimensions", "To enhance aesthetics"], 
             "answer": "To indicate different materials"},
             
            {"question": "What is the standard size of an A4 paper in mm?", 
             "options": ["210 x 297 mm", "210 x 210 mm", "297 x 420 mm", "A5 size"], 
             "answer": "210 x 297 mm"},
        ],
        "hard": [
            {"question": "What does 'CAD' stand for?", 
             "options": ["Computer-Aided Design", "Computer Assisted Drafting", "Creative Architectural Design", "None of the above"], 
             "answer": "Computer-Aided Design"},
             
            {"question": "What is the significance of line weight in engineering drawings?", 
             "options": ["To indicate importance", "To show material type", "To define edges", "To add color"], 
             "answer": "To indicate importance"},
             
            {"question": "Which type of projection uses parallel lines to project images?", 
             "options": ["Perspective projection", "Orthographic projection", "Isometric projection", "Oblique projection"], 
             "answer": "Orthographic projection"},
             
            {"question": "What is a key aspect of engineering drawing that helps prevent misinterpretation?", 
             "options": ["Color coding", "Standardization", "Artistic flair", "Creative layouts"], 
             "answer": "Standardization"},
             
            {"question": "What do auxiliary views show?", 
             "options": ["Different angles of an object", "Internal features", "Exterior features", "None of the above"], 
             "answer": "Different angles of an object"},
            {"question": "What is an exploded view drawing?", 
             "options": ["A drawing showing components separated", "A colored drawing", "A 3D model", "None of the above"], 
             "answer": "A drawing showing components separated"},
             
            {"question": "What does the term 'hidden lines' refer to?", 
             "options": ["Lines representing hidden edges", "Decorative lines", "Thick lines", "Dashed lines only"], 
             "answer": "Lines representing hidden edges"},
             
            {"question": "What is the main function of a layout drawing?", 
             "options": ["To show arrangement of components", "To color the drawing", "To provide dimensions", "To add textures"], 
             "answer": "To show arrangement of components"},
             
            {"question": "In engineering drawing, what does 'datum' refer to?", 
             "options": ["A reference point or line for measurements", "A color scheme", "A line style", "A type of projection"], 
             "answer": "A reference point or line for measurements"},
             
            {"question": "What does the term 'isometric drawing' refer to?", 
             "options": ["A 3D representation on a 2D plane", "Only line drawings", "2D perspective", "None of the above"], 
             "answer": "A 3D representation on a 2D plane"},
        ],
    },
    #solid mech
     "solid_mechanics": {
        "easy": [
            {"question": "What is stress in solid mechanics?", 
             "options": ["Force per unit area", "Material strength", "Deformation", "Weight of an object"], 
             "answer": "Force per unit area"},
             
            {"question": "What is strain?", 
             "options": ["Change in length per unit length", "Force applied", "Weight of an object", "Area of cross-section"], 
             "answer": "Change in length per unit length"},
             
            {"question": "What does Hooke's Law state?", 
             "options": ["Stress is proportional to strain", "Strain is proportional to volume", "Force is proportional to weight", "None of the above"], 
             "answer": "Stress is proportional to strain"},
             
            {"question": "Which type of stress occurs perpendicular to the surface?", 
             "options": ["Normal stress", "Shear stress", "Tensile stress", "Compressive stress"], 
             "answer": "Normal stress"},
             
            {"question": "What is the modulus of elasticity?", 
             "options": ["Ratio of stress to strain", "Ratio of force to area", "Ratio of weight to volume", "None of the above"], 
             "answer": "Ratio of stress to strain"},
             
            {"question": "What type of loading leads to bending in beams?", 
             "options": ["Transverse loading", "Axial loading", "Torsional loading", "Shear loading"], 
             "answer": "Transverse loading"},
             
            {"question": "What is the main purpose of a shear force diagram?", 
             "options": ["To visualize internal forces", "To measure stress", "To calculate volume", "To analyze material properties"], 
             "answer": "To visualize internal forces"},
             
            {"question": "In which materials does elastic deformation occur?", 
             "options": ["Elastic materials", "Plastic materials", "Brittle materials", "All of the above"], 
             "answer": "Elastic materials"},
             
            {"question": "What is the ultimate tensile strength?", 
             "options": ["Maximum stress before failure", "Stress after yielding", "Stress at fracture", "None of the above"], 
             "answer": "Maximum stress before failure"},
             
            {"question": "What is a moment in mechanics?", 
             "options": ["Force multiplied by distance", "Stress multiplied by area", "Weight divided by volume", "None of the above"], 
             "answer": "Force multiplied by distance"},
        ],
        "medium": [
            {"question": "What is the principle of superposition in solid mechanics?", 
             "options": ["The response of a structure can be determined by adding individual responses", "Stress is independent of strain", "All forces cancel out", "None of the above"], 
             "answer": "The response of a structure can be determined by adding individual responses"},
             
            {"question": "What is the difference between elastic and plastic deformation?", 
             "options": ["Elastic is reversible; plastic is permanent", "Plastic is reversible; elastic is permanent", "Both are reversible", "Both are permanent"], 
             "answer": "Elastic is reversible; plastic is permanent"},
             
            {"question": "What is shear stress?", 
             "options": ["Force parallel to the surface", "Force perpendicular to the surface", "Force divided by area", "None of the above"], 
             "answer": "Force parallel to the surface"},
             
            {"question": "What happens to a material beyond its yield point?", 
             "options": ["It deforms plastically", "It returns to original shape", "It fractures instantly", "None of the above"], 
             "answer": "It deforms plastically"},
             
            {"question": "What is the significance of the area under a stress-strain curve?", 
             "options": ["It represents toughness", "It represents elastic limit", "It shows maximum stress", "It indicates density"], 
             "answer": "It represents toughness"},
             
            {"question": "What is the unit of stress?", 
             "options": ["N/m²", "m²", "N", "kg"], 
             "answer": "N/m²"},
             
            {"question": "What is Poisson's ratio?", 
             "options": ["Ratio of lateral strain to axial strain", "Ratio of volume to area", "Ratio of stress to strain", "None of the above"], 
             "answer": "Ratio of lateral strain to axial strain"},
             
            {"question": "Which theory predicts failure in brittle materials?", 
             "options": ["Maximum stress theory", "Distortion energy theory", "Mohr's circle theory", "None of the above"], 
             "answer": "Maximum stress theory"},
             
            {"question": "What is the relationship between bending moment and shear force?", 
             "options": ["Shear force is the derivative of bending moment", "Bending moment is the derivative of shear force", "Both are independent", "None of the above"], 
             "answer": "Shear force is the derivative of bending moment"},
             
            {"question": "What is the impact of temperature on material strength?", 
             "options": ["Can increase or decrease depending on the material", "Always decreases strength", "Always increases strength", "None of the above"], 
             "answer": "Can increase or decrease depending on the material"},
        ],
        "hard": [
            {"question": "What is the significance of the neutral axis in bending?", 
             "options": ["No tension or compression occurs", "Maximum tension occurs", "Maximum compression occurs", "None of the above"], 
             "answer": "No tension or compression occurs"},
             
            {"question": "What does the term 'fatigue' refer to in solid mechanics?", 
             "options": ["Failure after repeated loading", "Immediate failure", "No failure", "None of the above"], 
             "answer": "Failure after repeated loading"},
             
            {"question": "What is the difference between elastic and plastic buckling?", 
             "options": ["Elastic buckling is reversible; plastic is not", "Plastic buckling is always reversible", "Both types are the same", "None of the above"], 
             "answer": "Elastic buckling is reversible; plastic is not"},
             
            {"question": "What is the relationship between stress concentration and material failure?", 
             "options": ["High stress concentration leads to failure", "Low stress concentration leads to failure", "Stress concentration does not affect failure", "None of the above"], 
             "answer": "High stress concentration leads to failure"},
             
            {"question": "What is the role of reinforcement in concrete?", 
             "options": ["To improve tensile strength", "To reduce weight", "To enhance aesthetics", "None of the above"], 
             "answer": "To improve tensile strength"},
        ],
    },

    #safety eng
    
    "safety engineering": {
        "easy": [
            {"question": "What is the main purpose of safety materials in construction?", 
             "options": ["To prevent accidents", "To enhance aesthetics", "To reduce costs", "To improve durability"], 
             "answer": "To prevent accidents"},
             
            {"question": "Which type of protective equipment is essential on a construction site?", 
             "options": ["Hard hats", "Decoration helmets", "Normal caps", "None of the above"], 
             "answer": "Hard hats"},
             
            {"question": "What does PPE stand for?", 
             "options": ["Personal Protective Equipment", "Professional Performance Equipment", "Public Protection Equipment", "None of the above"], 
             "answer": "Personal Protective Equipment"},
             
            {"question": "What is the primary function of safety goggles?", 
             "options": ["To protect eyes from debris", "To enhance vision", "To look fashionable", "None of the above"], 
             "answer": "To protect eyes from debris"},
             
            {"question": "What is the importance of safety training?", 
             "options": ["To ensure worker awareness", "To improve work efficiency", "To reduce costs", "None of the above"], 
             "answer": "To ensure worker awareness"},
             
            {"question": "Which material is commonly used for safety gloves?", 
             "options": ["Rubber", "Cotton", "Silk", "Leather"], 
             "answer": "Rubber"},
             
            {"question": "What is a safety data sheet (SDS)?", 
             "options": ["Document providing information on hazards", "Document for filing taxes", "Marketing brochure", "None of the above"], 
             "answer": "Document providing information on hazards"},
             
            {"question": "What does fall protection equipment do?", 
             "options": ["Prevents workers from falling", "Enhances performance", "Increases costs", "None of the above"], 
             "answer": "Prevents workers from falling"},
             
            {"question": "What is the role of signage in safety?", 
             "options": ["To communicate hazards", "To decorate the site", "To provide directions", "None of the above"], 
             "answer": "To communicate hazards"},
             
            {"question": "Which of the following is a fire safety material?", 
             "options": ["Fire-resistant fabric", "Cotton fabric", "Plastic", "Paper"], 
             "answer": "Fire-resistant fabric"},
        ],
        "medium": [
            {"question": "What should be done if there is a chemical spill?", 
             "options": ["Evacuate and notify authorities", "Ignore it", "Clean it immediately", "None of the above"], 
             "answer": "Evacuate and notify authorities"},
             
            {"question": "What is the main purpose of a first aid kit?", 
             "options": ["To treat minor injuries", "To provide food", "To enhance performance", "None of the above"], 
             "answer": "To treat minor injuries"},
             
            {"question": "What is the importance of wearing a harness?", 
             "options": ["Prevents falls from heights", "Increases speed", "Looks professional", "None of the above"], 
             "answer": "Prevents falls from heights"},
             
            {"question": "What are the risks of working without PPE?", 
             "options": ["Increased likelihood of injury", "No risks", "Better work performance", "None of the above"], 
             "answer": "Increased likelihood of injury"},
             
            {"question": "What is the primary function of ear protection?", 
             "options": ["To protect against noise-induced hearing loss", "To enhance hearing", "To improve fashion", "None of the above"], 
             "answer": "To protect against noise-induced hearing loss"},
             
            {"question": "What is the main objective of a safety audit?", 
             "options": ["To evaluate safety practices", "To increase productivity", "To reduce costs", "None of the above"], 
             "answer": "To evaluate safety practices"},
             
            {"question": "Which of the following is NOT a part of personal protective equipment?", 
             "options": ["Safety boots", "Work gloves", "Fashion shoes", "Face shields"], 
             "answer": "Fashion shoes"},
             
            {"question": "What should be included in an emergency action plan?", 
             "options": ["Evacuation procedures", "Contact information", "Roles of employees", "All of the above"], 
             "answer": "All of the above"},
             
            {"question": "What is the purpose of using scaffolding?", 
             "options": ["To provide a safe working platform", "To increase construction speed", "To enhance aesthetics", "None of the above"], 
             "answer": "To provide a safe working platform"},
             
            {"question": "What is the significance of fire drills?", 
             "options": ["To practice evacuation procedures", "To waste time", "To show off", "None of the above"], 
             "answer": "To practice evacuation procedures"},
        ],
        "hard": [
            {"question": "What is the role of a safety manager on a construction site?", 
             "options": ["To oversee safety compliance", "To improve productivity", "To manage finances", "None of the above"], 
             "answer": "To oversee safety compliance"},
             
            {"question": "What is the importance of risk assessment in construction?", 
             "options": ["To identify potential hazards", "To reduce costs", "To improve aesthetics", "None of the above"], 
             "answer": "To identify potential hazards"},
             
            {"question": "What is the difference between hard and soft barriers in safety?", 
             "options": ["Hard barriers are physical; soft barriers are procedural", "Both are the same", "Hard barriers are temporary", "None of the above"], 
             "answer": "Hard barriers are physical; soft barriers are procedural"},
             
            {"question": "What are the consequences of ignoring safety regulations?", 
             "options": ["Increased accidents", "Higher productivity", "Better morale", "None of the above"], 
             "answer": "Increased accidents"},
             
            {"question": "What is the purpose of a safety performance indicator?", 
             "options": ["To measure safety performance", "To improve profits", "To evaluate employee performance", "None of the above"], 
             "answer": "To measure safety performance"},
        ],
    },


}


# Current Affairs Data (Expanded Details)
current_affairs = {
    "India-Specific": [{
        "title": "Singapore Leads FDI in India",
        "details":
        "In the July-September quarter of FY25, Singapore contributed 50% of the total Foreign Direct Investment inflows into India, amounting to USD 13.6 billion. This marks a significant recovery in FDI inflows and highlights Singapore's growing role in India's economic development.",
        "source": "ADDA247"
    }, {
        "title": "Ratapani Wildlife Sanctuary Declared a Tiger Reserve",
        "details":
        "Ratapani Wildlife Sanctuary, located in Madhya Pradesh, has been declared the state’s 8th tiger reserve. This decision is part of broader efforts to enhance tiger conservation and promote ecotourism in the region, supporting wildlife and local economic growth.",
        "source": "GKToday"
    }, {
        "title": "Banking Laws (Amendment) Bill, 2024",
        "details":
        "The Union Finance Minister introduced the Banking Laws (Amendment) Bill, 2024, in the Lok Sabha. The bill aims to revise key banking regulations to ensure improved governance, financial stability, and sectoral growth.",
        "source": "ADDA247"
    }, {
        "title": "India and Kuwait Sign MoU",
        "details":
        "India and Kuwait have signed a Memorandum of Understanding to establish a Joint Commission for Cooperation (JCC). This agreement is a milestone in strengthening bilateral relations between the two nations.",
        "source": "GKToday"
    }, {
        "title": "AOMSUC-14 Conference in New Delhi",
        "details":
        "New Delhi hosted the 14th Asia-Oceania Meteorological Satellite Users’ Conference (AOMSUC-14). The event focused on advancements in meteorology, satellite technology, and climate resilience, drawing experts and officials from across the region.",
        "source": "ADDA247"
    }],
    "Global": [{
        "title": "World AIDS Day 2024 Observed",
        "details":
        "December 1, 2024, marked World AIDS Day, emphasizing global efforts in awareness, prevention, and treatment of HIV/AIDS. The day encouraged communities to combat stigma and provide support to affected individuals.",
        "source": "ADDA247"
    }, {
        "title": "International Day for the Abolition of Slavery",
        "details":
        "Observed on December 2, this day highlighted global efforts to eradicate modern slavery, including human trafficking and forced labor. Awareness campaigns stressed the importance of collective action to end exploitation.",
        "source": "ADDA247"
    }, {
        "title": "BBC's 100 Most Inspiring Women",
        "details":
        "Indian activist Pooja Sharma was named among BBC's 100 Most Inspiring Women of 2024 for her extraordinary humanitarian work, including performing funeral rites for unclaimed bodies and supporting underprivileged communities.",
        "source": "GKToday"
    }]
}

# App Tabs
tabs = st.tabs(["Quiz", "Current Affairs"])


# Streamlit App Structure
with tabs[0]:
    st.title("Quiz App")
    st.sidebar.header("Quiz Settings")
    
    # Select Topic
    topic = st.sidebar.selectbox("Select Topic", options=list(quiz_data.keys()))
    
    # Select Difficulty
    difficulty = st.sidebar.selectbox("Select Difficulty", options=["easy", "medium", "hard"])
    
    # Determine number of available questions in selected topic and difficulty
    available_questions = len(quiz_data[topic][difficulty])
    
    # Select Number of Questions (limited to available questions)
    num_questions = st.sidebar.slider("Number of Questions", min_value=1, max_value=available_questions, value=min(5, available_questions))
    
    # Filter Questions
    questions = random.sample(quiz_data[topic][difficulty], num_questions)
    
    # Quiz Logic
    for i, q in enumerate(questions):
        st.subheader(f"Question {i + 1}")
        st.write(q["question"])
        
        # Show options (non-interactive)
        st.write("**Options:**")
        for option in q["options"]:
            st.write(f"- {option}")
    
        # Expandable section to show the answer
        with st.expander("Show Answer"):
            st.write(f"**Correct Answer:** {q['answer']}")
    
    # Topic Suggestion Box
    #st.write("### Suggest a Topic for Future Quizzes")
    #suggestion = st.text_input("Enter your topic suggestion:")
    #if suggestion:
     #   # Append suggestion to a file
      #  with open("C:/Users/Jatin/OneDrive/Desktop/New folder/covid data/suggestions.txt", "a") as file:
       #     file.write(f"Topic requested/: {suggestion} \n")
       # st.write("Thank you for your suggestion!")
        
# Current Affairs Tab
with tabs[1]:
    st.title("Current Affairs")

    # Display India-Specific Affairs
    st.subheader("India-Specific Current Affairs")
    for affair in current_affairs["India-Specific"]:
        st.markdown(f"### {affair['title']}")
        st.write(affair["details"])
        st.write(f"**Source:** {affair['source']}")

    # Display Global Affairs
    st.subheader("Global Current Affairs")
    for affair in current_affairs["Global"]:
        st.markdown(f"### {affair['title']}")
        st.write(affair["details"])
        st.write(f"**Source:** {affair['source']}")

 

