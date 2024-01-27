# WiiUExploit
A WiiU exploit self hosting package (works with 5.5.x), this allows you to run HENlo server fully locally for offline usage.

## Requirements
- PC with Python2 or Python3 installed on it
- WiFi router or WiFi dongle capable of acting as access point for WiiU (2.4Ghz, AP Mode)

## Usage
1. Download [WiiUExploit.7z](https://github.com/loomweaver/WiiUExploit/releases/latest) to your PC. 
2. Change your PC WiFi's IPv4 connection settings to Manual, set your PC's LAN IP  to 192.168.0.123, and set the gateway IP as the LAN IP of your router/WiFi dongle (usually 192.168.0.1 or something similar).
3. Unzip WiiUExploit.7z somewhere on your PC. 
4. Open console terminal, navigate to the unzipped folder and run one of the server scripts, depending on your installed version of Python (server_python2.py for Python2 or server_python3.py for Python3). If successful, you should see a similar message appear: `Starting server on 192.168.0.123:8888`. Note the IP and port address.
5. Connect your WiiU via WiFi to your router/WiFi dongle, open http://192.168.0.123:8888 on your WiiU browser and follow the [WiiU CFW guide](https://wiiu.hacks.guide/#/tiramisu/browser-exploit) instructions as normal.

### Why 192.168.0.123? I want to use a different IP!
Just change IP in the server_python2.py/server_python3.py files then. IP is hardcoded specifically for the case when you don't have any kind of Internet.
