from jinja2 import Template

lists = [
    # service                  # nodeport
    [ 'argocd',                '30041' ],
    [ 'grafana',               '30042' ],
    [ 'minio',                 '30044' ],
    [ 'postgres-operator-ui',  '30049' ],
    [ 'misskey-https',         '30085' ],
    [ 'misskey-http',          '30086' ],
]


def generate_script(template_path, output_path, **kwargs):
    with open(template_path, 'r') as file:
        template_content = file.read()

    template = Template(template_content)

    rendered_script = template.render(**kwargs)

    with open(output_path, 'w') as output_file:
        output_file.write(rendered_script)

generate_script('./template.j2', './default.conf.j2', lists=lists)
