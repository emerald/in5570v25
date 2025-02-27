# Import the stuff
from mininet.topo    import Topo
from mininet.nodelib import NAT

# Setup the network topology.
class NetworkTopology( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        h3 = self.addHost( 'h3' )

        # Add switches
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )

        # Add Network Address Translation
        nat = self.addNode('nat0', cls=NAT, ip='10.0.0.254/24', inNamespace=False)

        # Add links
        self.addLink( h1 , s1 , delay='100ms')
        self.addLink( s1 , s2 , delay='200ms')
        self.addLink( s2 , h2 , delay='300ms')
        self.addLink( s2 , h3 , delay='175ms')

        self.addLink( s1 , nat ) # internet access

# Name for everyone outside to refer to
topos = { 'in5570': ( lambda: NetworkTopology() ) }

