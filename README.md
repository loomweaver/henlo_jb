# henlo_jb_local
webkit-based jailbreak for Playstation Vita/TV on firmware 3.65+

Based on [SKGleba's work](https://github.com/SKGleba/henlo_jb), this allows you to run HENlo server fully locally for offline usage.

## Requirements
- PC with Python2 or Python3 installed on it
- WiFi router or WiFi dongle capable of acting as access point for Vita (2.4Ghz, AP Mode)

## Usage
1. Download [henlo_jb_local.zip](https://github.com/loomweaver/henlo_jb/releases/tag/henlo_jb_local) to your PC. 
2. Change your IPv4 connection settings to Manual, set your PC's LAN IP  to 192.168.0.123, and set the gateway IP as the LAN IP of your router/WiFi dongle (usually 192.168.0.1 or something similar).
3. Unzip henlo_jb_local.zip somewhere on your PC. 
4. Open console terminal, navigate to the unzipped folder and run one of the server scripts, depending on your installed version of Python (server_python2.py for Python2 or server_python3.py for Python3). If successful, you should see the following message appear: `Starting server on 192.168.0.123:8888`
5. Open http://192.168.0.123:8888 on your Vita and follow the [HENlo Vita guide](https://vita.hacks.guide/using-henlo.html) instructions as normal.

### Why 192.168.0.123? I want to use a different IP!
Repo IP that serves henkaku/VitaDeploy downloads is hardcoded within compiled payload.bin. If you want to use a different IP, you will need to:
1. Download or checkout this repo with git,
2. Change `HEN_REPO_URL` string value in `bootstrap_lite/main.c`,
3. Run `prepare_jb.sh` to recompile the `payload.bin` (you will need [Vita SDK](https://vitasdk.org/) installed for compilation),
4. Change the IP address in `server_python2.py`/`server_python3.py`.
