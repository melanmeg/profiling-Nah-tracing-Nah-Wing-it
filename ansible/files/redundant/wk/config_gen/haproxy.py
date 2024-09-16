
# Environment
WK_IP_1 = '192.168.11.124'
WK_IP_2 = '192.168.11.125'
WK_IP_3 = '192.168.11.126'

lists = {
    # id         # service                  # IP               # port   # nodeport
    'service41': [ 'argocd',                '192.168.11.241',  '443',   '30041' ],
    'service42': [ 'grafana',               '192.168.11.242',  '80',    '30042' ],
    'service44': [ 'minio',                 '192.168.11.244',  '80',    '30044' ],
    'service47': [ 'pyroscope',             '192.168.11.247',  '4040',  '30047' ],
    'service49': [ 'postgres-operator-ui',  '192.168.11.249',  '80',    '30049' ],
    'service85': [ 'misskey-https',         '192.168.11.185',  '443',   '30085' ],
    'service86': [ 'misskey-http',          '192.168.11.186',  '80',    '30086' ],
    'service87': [ 'misskey-3000',          '192.168.11.187',  '3000',  '30087' ],
}

# config gen haproxy
from jinja2 import Template


def generate_script(template_path, output_path, **kwargs):
    with open(template_path, 'r') as file:
        template_content = file.read()

    template = Template(template_content)

    rendered_script = template.render(**kwargs)

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_script)

generate_script('../haproxy/template.cfg', '../haproxy/haproxy.cfg', lists=lists, WK_IP_1=WK_IP_1, WK_IP_2=WK_IP_2, WK_IP_3=WK_IP_3)
