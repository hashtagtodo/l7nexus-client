<img src="https://i.imgur.com/NSa5t14.png">

A client programmed in Python to interact with the L7Nexus API will allow you to run the stresser tool from a terminal very easily.

# Installation:

First, make sure you have Python and pip installed on your system.

 ```git clone https://github.com/hashtagtodo/l7nexus-client.git```
 
```cd l7nexus-client```

```pip install -r requirements.txt```

Configure the config.json file with your API KEY and USER ID.

# Usage:

Run the client script and follow the on-screen instructions to start the stresser tool.

```python3 main.py```

The script will prompt you for the necessary information, such as the target of the attack and the number of repetitions.

# Notes
The tool only works if you have an active subscription with API access. Additionally, the boot time and concurrent values are limited based on your plan.

This tool is not an official tool; it was designed solely to facilitate the use of the service in a loop on the same target.

**Disclaimer:**

The use of this service should only be for ethical purposes to test your own networks. It should never be executed against third-party networks or sites.

###
