import yaml

with open("test_actions.yml", 'r') as stream:
    try:
        alerts = yaml.load(stream)
        for key,value in alerts.items():
            print( "%s=%s" % (key, value))
            # print(value['expect'])

    except yaml.YAMLError as exc:
        print(exc)


