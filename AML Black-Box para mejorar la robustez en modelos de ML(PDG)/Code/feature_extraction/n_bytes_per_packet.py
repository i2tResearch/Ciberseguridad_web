from nfstream import NFStreamer, NFPlugin
import numpy as np

class NBytesPerPacket(NFPlugin):
    '''
        Extracts the first n_bytes from each packet in the flow, the bytes are taken
        from the transport layer payload (L4). if the flow have less than n_bytes bytes,
        then the rest of the bytes are zero-valued.
    '''
    def __init__(self, n=1024):
        self.n = n
    
    def on_init(self, packet, flow):
        flow.udps.n_bytes_value = self.n
        flow.udps.n_bytes_per_packet = list()
        
        self.on_update(packet, flow)

    def on_update(self, packet, flow):
        amount_to_copy = min(self.n, packet.payload_size)
        if amount_to_copy == 0:
            flow.udps.n_bytes_per_packet.append([int(i) for i in list(np.zeros(self.n))])
            return
        
        max_index_to_copy = -packet.payload_size+amount_to_copy if -packet.payload_size+amount_to_copy != 0 else None
        n_bytes = np.zeros(self.n)
        n_bytes[:amount_to_copy] = np.frombuffer(packet.ip_packet[-packet.payload_size:max_index_to_copy], dtype=np.uint8)
        flow.udps.n_bytes_per_packet.append([int(i) for i in list(n_bytes)])

    def on_expire(self, flow):
        pass

