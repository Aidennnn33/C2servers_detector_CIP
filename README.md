# About

This automated tool detects C2 server IPs that have been identified on Criminal IP (https://www.criminalip.io) and retrieves their corresponding information

I employed the /v1/banner/search endpoint from the Criminal IP API for this purpose, enabling us to query and identify C2 (Command and Control) servers through Asset Search.

The collected information about the identified C2 servers includes their type, the query used for detection, C2 server IP address, port, current status, host name, and tags.

This data is stored in a ".csv" file format."

* The query file currently uploaded offers a list of detectable C2 servers:
    * Covenant C2
    * Sliver C2
    * Posh C2
    * Mythic C2
    * Havoc C2
    * Gophish C2
    * Metasploit C2
    * Deimos C2
      
<br/>

# Prerequisites

1. Sign up for a free account on [criminalip.io](www.criminalip.io) to obtain a Criminal IP API key.

2. Make sure you have the Python requests module installed.
```
    pip install requests
```  
<br/>

# Instsallation and Setup

1. Download the code from the GitHub repository using the following command:
```
    git clone (https://github.com/Aidennnn33/C2servers_detector_CIP)
```
2. Open the 'cip_c2detect.py' file in a code editor (text editor) and insert your unique API key into the 'CriminalIP_API_KEY' field located at the top.

<br/>

# How to get started & screenshot

* The partial example query file is shown below.
```
    {
    "count": 8,
    "data": {
        "covenant": [
            "blazor ssl_subject_common_name : covenant"
        ],
        "posh": [
            "ssl_subject_common_name : P18055077"
        ],
        "mythic": [
            "ssl_subject_organization : Mythic port : 7443"
        ],
        "havoc": [
            "jarm : 3fd21b20d00000021c43d21b21b43de0a012c76cf078b8d06f4620c2286f5e ssl_subject_organization:tech co"
        ],
        "sliver": [
            "\"HTTP/1.1\" \"404 Not Found\" \"must-revalidate\" jarm : 3fd21b20d00000021c43d21b21b43d41226dd5dfc615dd4a96265559485910"
        ],
        "gophish": [
            "favicon:2FE4DD37 jarm:28d28d28d00028d00041d28d28d41dd279b0cf765af27fa62e66d7c8281124"
        ],
        "metasploit": [
            "metasploit ssl_subject_organization:rapid7",
            "favicon:-79F667F ssl_subject_organizationLrapid7"
        ],
        "deimos": [
            "jarm:1bd1bd1bd0001bd00041d1bd1bd41db0fe6e6bbf8c4edda78e3ec2bfb55687 ssl_subject_organization:acme co",
            "\"Deimos C2\" ssl_subject_organization:acme co port:8443"
        ]
    }
}
```
</br>

* To execute the program, use the following command:
```
    python cip_c2detect.py
```

* Upon running the program, the following process occurs:

Initially, the terminal displays the current C2 being detected and the query being utilized.

Once the detection for all queries is finished, the program displays the filename in which the results are saved in ".csv" format, and then the program terminates.

</br>

![Graph](https://github.com/Aidennnn33/C2servers_detector_CIP/blob/main/C2servers_detector%20Images/Command%20Image.png)

</br>

# How to save the result

The results are stored in a .csv file, each containing the following information:

|Target C2|Query|IP address|Detected Port|Now Status|Hostname|Tags|
|---------|-----|----------|-------------|----------|--------|----|


</br>

The saved files are organized in ascending order according to the Target C2 name. Below, you can find screenshots of specific sections from the stored result file.

![Graph](https://github.com/Aidennnn33/C2servers_detector_CIP/blob/main/C2servers_detector%20Images/Result%20Image.png)
