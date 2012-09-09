from cinderclient import exceptions as cinderclient
from glanceclient.common import exceptions as glanceclient
from keystoneclient import exceptions as keystoneclient
from novaclient import exceptions as novaclient
from quantumclient.common import exceptions as quantumclient
from swiftclient import client as swiftclient


UNAUTHORIZED = (keystoneclient.Unauthorized,
                keystoneclient.Forbidden,
                cinderclient.Unauthorized,
                cinderclient.Forbidden,
                novaclient.Unauthorized,
                novaclient.Forbidden,
                glanceclient.Unauthorized,
                quantumclient.Unauthorized,
                quantumclient.Forbidden)

NOT_FOUND = (keystoneclient.NotFound,
             cinderclient.NotFound,
             novaclient.NotFound,
             glanceclient.NotFound,
             quantumclient.NetworkNotFoundClient,
             quantumclient.PortNotFoundClient)

# NOTE(gabriel): This is very broad, and may need to be dialed in.
RECOVERABLE = (keystoneclient.ClientException,
               # AuthorizationFailure is raised when Keystone is "unavailable".
               keystoneclient.AuthorizationFailure,
               cinderclient.ClientException,
               novaclient.ClientException,
               glanceclient.ClientException,
               # NOTE(amotoki): Quantum exceptions other than the first one
               # are recoverable in many cases (e.g., NetworkInUse is not
               # raised once VMs which use the network are terminated).
               quantumclient.QuantumClientException,
               quantumclient.NetworkInUseClient,
               quantumclient.PortInUseClient,
               quantumclient.AlreadyAttachedClient,
               quantumclient.StateInvalidClient,
               swiftclient.ClientException)
