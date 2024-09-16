
# Environment
WK_IP_1 = '192.168.11.124'
WK_IP_2 = '192.168.11.125'
WK_IP_3 = '192.168.11.126'

lists = {
    # id         # LB_ID    # vrId  # IP
    'service41': [ '41',    '41',   '192.168.11.241' ],
    'service42': [ '42',    '42',   '192.168.11.242' ],
    'service44': [ '44',    '44',   '192.168.11.244' ],
    'service47': [ '47',    '47',   '192.168.11.247' ],
    'service49': [ '49',    '49',   '192.168.11.249' ],
    'service85': [ '85',    '85',   '192.168.11.185' ],
    'service86': [ '86',    '86',   '192.168.11.186' ],
    'service87': [ '87',    '87',   '192.168.11.187' ],
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

generate_script('../keepalived/template.conf', '../keepalived/keepalived_k8s-wk-1.conf', lists=lists, SRC_IP=WK_IP_1, PEER_IP_1=WK_IP_2, PEER_IP_2=WK_IP_3, state='MASTER', priority='101')
generate_script('../keepalived/template.conf', '../keepalived/keepalived_k8s-wk-2.conf', lists=lists, SRC_IP=WK_IP_2, PEER_IP_1=WK_IP_1, PEER_IP_2=WK_IP_3, state='BACKUP', priority='99')
generate_script('../keepalived/template.conf', '../keepalived/keepalived_k8s-wk-3.conf', lists=lists, SRC_IP=WK_IP_3, PEER_IP_1=WK_IP_1, PEER_IP_2=WK_IP_2, state='BACKUP', priority='97')
