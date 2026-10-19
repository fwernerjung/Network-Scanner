from flask import Flask, render_template
import socket

hostname = socket.gethostname()

app = Flask(__name__)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route("/")
def home():
    titel = "Hello World aus dem Netzwerk!"
    text = "Diese Seite wurde von einem anderen Gerät im WLAN aufgerufen!"
    beispiel_zahl = 100
    hostname= hostname
    local_ip = s.getsockname()[0]
    
    return render_template(
        "index.html", 
        ueberschrift=titel, 
        nachricht=text, 
        zahl=beispiel_zahl,
        hostname=hostname,
        ip= local_ip,
    )

if __name__ == "__main__":
    # host="0.0.0.0" macht den Server für das gesamte Netzwerk erreichbar
    # port=5000 legt den Port fest (kannst du auch ändern, z.B. 80)
    app.run(host="0.0.0.0", port=5000, debug=True)