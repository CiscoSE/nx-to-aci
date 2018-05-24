**ACI First Setup**

 ACI First Setup is a solution that allows you to migrate your current nexus basic configuration (NTP, DNS, etc) to the 
 Application Policy Infrastructure Controller. To use this tool, complete the form with the credentials and upload a nexus configuration file.
  The tool will search for the configurations of interest and will send that information to the APIC.

The application runs on top of a Flask Application and uses Javascript (Sijax) and other constructs to create a simple HTML
application that can be deployed in a production environment using Apache/NGINX with WSGI.


Contacts:

* Santiago Flores ( sfloresk@cisco.com )
* Cesar Obediente ( cobedien@cisco.com )

**Installation**

As this is a Flask application you will need to either integrate the application in your production environment or you can
get it operational in a virtual environment on your computer. In the distribution is a requirements.txt file that you can
use to get the package requirements that are needed. The requirements file is located in the root directory of the distribution.

You also need to install docker within your environment. It can be local or remote. In case that you use a remote docker server be aware
that by default the solution looks for a local docker server. To change that behaviour go to app -> sijax_handlers -> docker_handler
and change the constant DOCKER_URL

It might make sense for you to create a Python Virtual Environment before installing the requirements file. For information on utilizing
a virtual environment please read http://docs.python-guide.org/en/latest/dev/virtualenvs/. Once you have a virtual environment active then
install the packages in the requirements file.

`(virtualenv) % pip install -r requirements.txt
`

For security you should change the default flask secret key for this project:

Inside this project
Go to app -> __init__

Assign this variable:

app.secret_key = ''

This is a flask parameter, just choose a random string of no less than 40 characters.
E.g:
'A0Zr4FhJASD1LFmw0918jHH!jm84$#ssaWQsif!1'

Also, you should generate your own SSL certificates. This command will create them:

openssl req -x509 -newkey rsa:2048 -keyout NCAkey.pem -out NCAcert.pem -days 365 -nodes

After creation, replace the cert and key file within the project.

To run the the application just execute the run.py file.
E.g. for a linux machine will be sudo python run.py

If you need to make the application visible outside your computer, change the run.py file with your own
 IP. You can also change the port that the application will be listening.
