import yaml

class ActionsMap:

    def __init__(self, config_file):
        with open(config_file, 'r') as stream:
            try:
                self.actions = yaml.load(stream).items()
                for key,value in self.actions:
                    print("DEBUG: %s=%s" % (key, value))

            except yaml.YAMLError as exc:
                print(exc)


