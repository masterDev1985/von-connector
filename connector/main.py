#! /usr/bin/python3

from von_agent.nodepool import NodePool
from von_agent.agents import AgentRegistrar

import asyncio


async def main():
    pool = NodePool('test', '/root/.indy/pool_transactions_sandbox_genesis')

    print('\n\n\nOpening pool...\n\n\n')
    await pool.open()
    print('\n\n\nFinished opening pool\n\n\n')

    print('Creating AgentRegistrar')
    tag = AgentRegistrar(
        pool,
        Wallet(pool.name, 'trustee-seed', 'trustee-wallet'),
        '127.0.0.1',
        8000, 'api/v0')
    print('AgentRegistrar\'s DID: {}'.format(tag.process_get_did()))

    print('\n\n\nClosing pool...\n\n\n')
    await pool.close()
    print('\n\n\nFinished closing pool\n\n\n')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
