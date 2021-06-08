# Cybervision Security and Automated Components Grouping



## Summary
 This python application provides the following features/ Solution:
 1. It retrieves domains/public IPs from cyber vision and checks them against Cisco Umbrella (or integrated 3rd party platform) to get their reputation. For any malicious domain or IP detected, an event is pushed to Cyber Vision dashboard to notify the user.

 2. Components grouping. A group here is a logical collection of components that share certain characteristic. When Cisco Cyber Vision is deployed in an environment, it detects the components connected. To ease with the grouping, this application can enable you to create a group, and place components in the group created or pre-created group automatically. This grouping can be based on several characteristics. A few examples are: 
  - Components by same manufacturer
  - Components that have similar tags.eg, Http, DNS (Not implemented fully at the time of this writing)
  - Components in the same subnet (Not Implemented in this Application at the time of this writing)

 **The script can be run on a remote PC or directly on Cyber Vision Center.**


## Application workflow

 **Retrieve domains and public IPs, Check Reputation and Push Event on Cyber Vision**
   - Retrieve domains and public IPs seen in Cisco Cyber Vision
   - Check the reputation of the above against Cisco Umbrella.
   - if malicious domain/ip is detected, an event is pushed to Cyber Vision dashboard.

 **Create groups and/or automatically group Components**
   - Retrieve all components from Cyber Vision and check for ungrouped components.
   - Group the components based on user's input, either by tags or by vendor.
   - Create and update the group on Cyber Vision dashboard.


## Components
      - Cisco Cyber Vision
      - Catalyst Switch(eg, IE3400, 9300) with Cyber Vision sensor deployed for connecting components
      - Cisco Umbrella for domain and Ip reputation check
      - 3rd party domain reputation check platform. In this case we have integrated IPQualityScore and WhoisXML
## Prerequisites
  - Cisco Cyber Vision Center deployment
  - If running it on a Remote PC and not on Cyber Vision Center, the remote PC needs to have Python 3.x
  - Active Umbrella subscription with Access to a valid Umrella investigate API key
  - IPQualityScore and WhoisXML API Access


## Installation

 - On the env file, fill the following details:
      - Cyber Vision  - local_cybervision_ip:port
                      - API Key: *x-token-id*
      - Umbrella - Investigate API url
                 - Valid investigate API keys
      - For the 3rd party platforms we have used:
                 - IPQualityScore API base url and valid API key
                 - WhoisXML API url and a valid API key
    
 - Log in to Cyber Vision Center via SSH console.  
 - Clone / Copy the code to your desired folder.
 - Install the required libraries: 
      - Pip install -r requirements.txt

## Operation
   **To Retrieve domains, check their Reputation and Push events to CyberVision:**
   - if running the script for the very first time, it is recommended to check all domains/ public IPs. To do that, ensure the PERIOD variable in the env file is empty; PERIOD = { 'period' : ''} and then the scrip as below:
    
- **$ Python3 TASK_1_1.py**

    For subsequent checks, you can define the period for which you want to check by setting a period X (in days); PERIOD = {'period':X} in the env file then run:

- **$ Python3 TASK_1_1.py**

   **To Retrieve public IPs , check their reputation and Push events to CyberVision:**
   - Follow the above procedure but now run:

     - **$ python TASK_1_2.py**    in place of Task1_1.py

   **To Automatically Group Ungrouped Components**

    RUN
- **$ TASK_2.py**

         - This will automatically group ungrouped components by their vendor.

## Examples

- **A screenshot of the events after a Malicious domain is found**
![sample events](/IMAGES/img1.png)


- **A screenshot of Grooups automatically created and components assigned to them**
![sample groups](/IMAGES/img2.png)
