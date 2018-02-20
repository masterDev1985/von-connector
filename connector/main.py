#! /usr/bin/python3

from von_agent.nodepool import NodePool
from von_agent.agents import AgentRegistrar

import asyncio
import logging

async def main():
    logging.basicConfig(level=logging.DEBUG);

    pool = NodePool('test', '/root/.indy-cli/networks/sandbox/pool_transactions_genesis')


    logging.info('\n\n\nOpening pool...\n\n\n')
    await pool.open()
    logging.debug('\n\n\nFinished opening pool\n\n\n')

    logging.info('Creating AgentRegistrar')
    tag = AgentRegistrar(
        pool,
        Wallet(pool.name, 'trustee-seed', 'trustee-wallet'),
        '127.0.0.1',
        8000, 'api/v0')
    logging.debug('AgentRegistrar\'s DID: {}'.format(tag.process_get_did()))

    logging.info('\n\n\nClosing pool...\n\n\n')
    await pool.close()
    logging.info('\n\n\nFinished closing pool\n\n\n')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
