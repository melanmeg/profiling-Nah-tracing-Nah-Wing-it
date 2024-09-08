
# Environment
WK_IP_1 = '192.168.11.124'
WK_IP_3 = '192.168.11.125'

lists = {
    # id         # LB_ID    # vrId  # IP
    'service41': [ '41',    '41',   '192.168.11.241' ],
    'service42': [ '42',    '42',   '192.168.11.242' ],
    'service44': [ '44',    '44',   '192.168.11.244' ],
    'service47': [ '47',    '47',   '192.168.11.247' ],
    'service49': [ '49',    '49',   '192.168.11.249' ],
    'service81': [ '81',    '81',   '192.168.11.181' ],
    'service82': [ '82',    '82',   '192.168.11.182' ],
}

# config gen keepalived
from jinja2 import Template


def generate_script(template_path, output_path, **kwargs):
    with open(template_path, 'r') as file:
        template_content = file.read()

    template = Template(template_content)

    rendered_script = template.render(**kwargs)

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_script)

generate_script('../keepalived/template.conf', '../keepalived/keepalived_master.conf', lists=lists, WK_IP_1=WK_IP_1, WK_IP_3=WK_IP_3, state='MASTER', priority='101')
generate_script('../keepalived/template.conf', '../keepalived/keepalived_backup.conf', lists=lists, WK_IP_1=WK_IP_1, WK_IP_3=WK_IP_3, state='BACKUP', priority='102')
