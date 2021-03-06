from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Echo(DatagramProtocol):
    def datagramReceived(self, data, addr):
        print("received {!r} from {}".format(data, addr))
        self.transport.write(data, addr)


reactor.listenUDP(9999, Echo(), interface="::")
reactor.run()
