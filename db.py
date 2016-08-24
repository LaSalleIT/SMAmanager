
import redis


class Redis(object):

    # noinspection PyBroadException
    def __init__(self, redis_port, redis_addr, redis_auth):
        self.port = redis_port
        self.addr = redis_addr
        self.passwd = redis_auth

        try:
            self._connection = redis.Redis(host=self.addr, port=self.port, password=self.passwd)
        except:
            print("Failed to establish connection to Redis server.")
            exit(-1)

    def get_list_count(self, l):
        return len(self._connection.lrange(l, 0, -1))

    def get_keys_list(self):
        return self._connection.keys()

    def get_every_list_count(self):
        ls = self.get_keys_list()
        ls_count = {}
        for l in ls:
            if self._connection.type(l) is "list":
                ls_count[l] = self.get_list_count(l)

        return ls_count

    def del_in_list(self, name, list_name):
        self._connection.lrem(list_name, name, 0)




