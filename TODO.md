# TODO

- change return to provide more information (currently on provides int as centre of return should include start and end of band as well)
- add error handling if target system name does not exist
- add handling if path intesects band twice
  - python src/main.py arcl1 61333041 47755719 5 (MICl2 -> arcl1 should cross twice, current response gives the second crossing)
- fill in data for "0" value distances
- currently catching errors if path is outside halo with a try/except, would like a better way to do this...
