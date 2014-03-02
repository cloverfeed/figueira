from mako.template import Template
import email
import fileinput


def main():
    lines = []
    for line in fileinput.input():
        lines.append(line)
    s = ''.join(lines)

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
    print out.encode('utf8')

if __name__ == '__main__':
    main()
