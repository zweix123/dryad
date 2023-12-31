from dryad import Dryad, DryadFlag

cmd_tree = {
    "vis-cmd": [
        "echo 1",
        "echo 2",
        "echo 3",
    ],
    "invis-cmd": [
        DryadFlag.InVisible,
        "echo 1",
        "echo 2",
        "echo 3",
    ],
}


Dryad(cmd_tree)

"""
> python test/flag_invisiable.py vis-cmd
echo 1
1
echo 2
2
echo 3
3

> python test/flag_invisiable.py invis-cmd
1
2
3
"""
