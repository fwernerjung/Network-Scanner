from flask import Flask, render_template, request
import socket
import getpass

hostname = socket.gethostname()

app = Flask(__name__)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

@app.route("/")
def home():
    hostname= "Unbekannt"
    local_ip = "127.0.0.1"
    username = "Unbekannt"
    visitor_ip = "Unbekannt"
    try:
        hostname = socket.gethostname()
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        username = getpass.getuser()
        visitor_ip = request.remote_addr

        hostname=hostname
    except Exception as e:
        print(f"Fehler beim abrufen der Netzwerkinfos: {e}")
    
    return render_template(
        "index.html",  
        hostname=hostname,
        ip= local_ip,
        username= username,
        visitor_ip = visitor_ip
    )

if __name__ == "__main__":
    # host="0.0.0.0" macht den Server für das gesamte Netzwerk erreichbar
    # port=5000 legt den Port fest (kannst du auch ändern, z.B. 80)
    app.run(host="0.0.0.0", port=5000, debug=True)