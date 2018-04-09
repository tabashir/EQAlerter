import yaml

with open("alerts.yml", 'r') as stream:
    try:
        alerts = yaml.load(stream)
        for key,value in alerts.items():
            print( "%s=%s" % (key, value))
            print(value['expect'])

    except yaml.YAMLError as exc:
        print(exc)


