Run instructions

If flask not installed:
pip3 install --upgrade pip
pip3 install flask
pip3 install shapely // library for checking long/lat. why reinvent the wheel? also makes my code cleaner. happy to discuss the algorithm behind the library.

Start server:
python3 state-server.py

Execute request:
curl -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/

Cheers.