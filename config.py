
import json


class ConfigObject(object):

    def __init__(self, version, type, redis, http):
        self.version = version
        self.type = type
        self.redis = redis
        self.http = http

    @property.getter
    def get_http_properties(self):
        return self.http["authmethod"], self.http["port"], self.http["addr"]

    @property.getter
    def get_redis_properties(self):
        return self.redis["port"], self.redis["addr"]

    def __str__(self):
        return json.dumps({
            "version": self.version,
            "type": self.type,
            "redis": {
                "port": self.redis["port"],
                "addr": self.redis["addr"]
            },
            "http": {
                "authmethod": self.http["authmethod"],
                "port": self.http["port"],
                "addr": self.http["addr"],
            }
        })


class Config(object):

    def __init__(self, config_location):
        try:
            with open(config_location) as fd:
                o = fd.readlines()

            parsed = json.loads(o.join(""))

            # Init
            self.default_config = ConfigObject("0.1priv", "private", {"port": 6379, "addr": "127.0.0.1"}, http={})

            # checks

            try:
                if parsed["version"] is None:
                    raise AttributeError("version")
                if parsed["type"] is None:
                    raise AttributeError("type")
                if parsed["redis"]["port"] is None:
                    raise AttributeError("redis_port")
                if parsed["redis"]["addr"] is None:
                    raise AttributeError("redis_addr")
                if parsed["http"]["authmethod"] is None:
                    raise AttributeError("http_authmethod")
                if parsed["http"]["port"] is None:
                    raise AttributeError("http_port")
                if parsed["http"]["addr"] is None:
                    raise AttributeError("http_addr")
            except AttributeError as ae:
                for error in ae.args:
                    if error is "version":
                        print("Version not found or not valid. Using default values...")
                        parsed["version"] = self.default_config.version
                    if error is "type":
                        print("Type is not found or not valid. Using default values...")
                        parsed["type"] = self.default_config.type
                    if error is "redis_port":
                        print("Redis server port is not found or not valid. Using default values...")
                        parsed["redis"]["port"] = self.default_config.redis["port"]
                    if error is "redis_addr":
                        print("Redis server address is not found or not valid. Using default values...")
                        parsed["redis"]["addr"] = self.default_config.redis["addr"]
                    if error is "http_authmethod":
                        print("Http authentication method is not found or not valid. Using default values...")
                        parsed["http"]["authmethod"] = self.default_config.http["authmethod"]
                    if error is "http_port":
                        print("Http server port is not found or not valid. Using the default values...")
                        parsed["http"]["port"] = self.default_config.http["port"]
                    if error is "http_addr":
                        print("Http server address is not found or not valid. Using the default values... ")
                        parsed["http"]["addr"] = self.default_config.http["addr"]
            else:
                print("Failure while reading configuration. Exiting...")
                exit(-1)

            self.config = parsed

        except IOError:
            print("IOError: Input file broken")
            print("Using default parameters...")
            self.config = ConfigObject("0.1priv", "private", {"port": 6379, "addr": "127.0.0.1"}, http={})
        else:
            print("Failure processing config. Exiting...")
            exit(-1)