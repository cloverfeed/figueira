from mako.template import Template
import email
import fileinput
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    with open('in.mail') as f:
        s = f.read()

    msg = email.message_from_string(s)

    part = msg.get_payload()[1]
    charset = part.get_content_charset()
    body = part.get_payload(decode=True).decode(charset)

    temp = Template(filename='templates/message.mako', default_filters=['h'])
    out = temp.render(_from=msg['From'],
                      date=msg['Date'],
                      subject=msg['Subject'],
                      body=body,
                      )
    return out.encode('utf8')

if __name__ == '__main__':
    app.run(debug=True)
