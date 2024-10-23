#!/usr/bin/python3
import asyncio
from blank_pkg.cli import print_logo
from blank_pkg.repository.mirror_update import update_mirrors
from blank_pkg.config import Mirrors


async def main():
	print_logo()
	await update_mirrors(Mirrors.SYSTEM_WIDE)


if __name__ == '__main__':
	asyncio.run(main())
