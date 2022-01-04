
import logging
import log

logging.basicConfig(
    filename='client.log',
    format='%(asctime)-10s %(levelname)s %(module)s %(message)s',
    level=logging.INFO
)

# log = logging.getLogger('basic')
#
# log.warning('Warning')
