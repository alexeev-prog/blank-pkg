import aiohttp
import time
from rich.progress import Progress
from rich import print
from blank_pkg.config import Mirrors


async def update_mirrors(mirrors: Mirrors):
	with Progress(transient=True) as progress:
		task1 = progress.add_task("[cyan]Update mirrors...", total=len(mirrors))

		while not progress.finished:
			for mirror in mirrors:
				async with aiohttp.ClientSession() as session:
					async with session.get(mirror) as response:
						if response.status != 200:
							print(f'[red][ ✗ ] Mirror {mirror} not available {response.status}[/red]')
						else:
							print(f'[green][ ✓ ] Mirror {mirror} available {response.status}[/green]')

						progress.update(task1, advance=1)
