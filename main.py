from argparse import ArgumentParser

from kominfo import Kominfo
from kominfo.helpers.Enums import Group, Organisasi

if(__name__ == '__main__'):
    argp = ArgumentParser()
    argp.add_argument("--keyword", '-k', type=str)
    argp.add_argument("--group", '-g', type=str)
    argp.add_argument("--org", '-or', type=str)
    argp.add_argument("--output", '-o', type=str, default='data')
    args = argp.parse_args()

    kominfo: Kominfo = Kominfo()
    kominfo.search(
        q=args.keyword, 
        groups=Group[args.group].value if args.group else None, 
        org=Organisasi[args.org].value if args.org else None
    )