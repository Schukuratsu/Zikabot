# Zikabot
Instagram bot to get new followers

## Quick Start

### Creating and using a virtual environment
To install venv:\
`pip3 instal virtualenv`\
To create one in your project:\
`mkdir venv`\
`python3 -m venv venv`\
To activate it on Linux:\
`source venv/bin/activate`\
To activate it on Windows PowerShell:\
*Open* **Windows PowerShell** *as* **administrator** \
`Set-ExecutionPolicy RemoteSigned`\
*Agree with the prompt that will show* \
`venv/Scripts/activate`\
*Note: Next time you want to activate you will only need this last command* \
The first time you activate it you want to install the libraries for this specific project:\
`pip install -r requirements.txt`\
If you need to deactivate the virtual environment:\
`deactivate`

### Adjusting the settings
Create a copy of the "settings_example.json" and name it "settings.json".\
In "db" adjust the address, credentials and database name.\
In "instagram" set your instagram credentials.\
In config 
 
## To remember

Command for creating the "requirements.txt" file:\
`pip freeze > requirements.txt`
		