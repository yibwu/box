import binascii


class ConsistentHash:
    
    def __init__(self, nodes=[], replicas=3):
        self.replicas = replicas 
        self.ring = []
        self.num_node = dict()    
        for node in nodes:
            self.add_node(node)

    def add_node(self, node):
        for i in range(self.replicas):
            crc32 = binascii.crc32(node + str(i))            
            self.ring.append(crc32)
            self.num_node[crc32] = node
        self.ring.sort()
    
    def remove_node(self, node):
        for i in range(self.replicas):
            crc32 = binascii.crc32(node + str(i))            
            if crc32 in self.ring:
                self.ring.remove(crc32)
            if crc32 in self.num_node:
                del self.num_node[crc32]

    def get_node(self, node):
        if not self.num_node:
            return None, None, None
        crc32 = binascii.crc32(node)            
        for n in self.ring:
            if crc32 <= n:
                return crc32, n, self.num_node[n]
        return crc32, self.ring[0], self.num_node[self.ring[0]] 

    def print_consistent_hash(self):
        for n in self.ring:
            print(n)
        for n, node in self.num_node.items():
            print(n, node)
        

if __name__ == '__main__':
    nodes = [
        '127.0.0.1:8000',
        '127.0.0.1:8001',
        '127.0.0.1:8002',
    ]
    ch = ConsistentHash(nodes, 3)
    ch.print_consistent_hash()
    print('\n')

    cases = ('456', 'aaa', 'abc', '132', '1ac', '90ae')
    for node in cases:
        crc32, n, target = ch.get_node(node)
        print(crc32, n, target)
    print('\n')
    
    ch.remove_node(nodes[0])
    ch.print_consistent_hash()
