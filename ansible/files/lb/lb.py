from jinja2 import Template

lists = [
    # service                  'port',  # nodeport
    [ 'argocd',                '8081',  '30041' ],
    [ 'grafana',               '8082',  '30042' ],
    [ 'minio',                 '8083',  '30044' ],
    [ 'postgres-operator-ui',  '8084',  '30049' ],
    [ 'misskey-https',         '8085',  '30085' ],
    [ 'misskey-http',          '8086',  '30086' ],
]


def generate_script(template_path, output_path, **kwargs):
    with open(template_path, 'r') as file:
        template_content = file.read()

    template = Template(template_content)

    rendered_script = template.render(**kwargs)

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_script)

generate_script('./template.j2', './default.conf.j2', lists=lists)
