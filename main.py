import os

from argparse import ArgumentParser
from json import dumps

from kominfo import Kominfo
from kominfo.helpers import logging
from kominfo.helpers.Enums import Group, Organisasi

if(__name__ == '__main__'):
    argp = ArgumentParser()
    argp.add_argument("--keyword", '-k', type=str)
    argp.add_argument("--group", '-g', type=str)
    argp.add_argument("--org", '-or', type=str)
    argp.add_argument("--page", '-p', type=int, default=1)
    argp.add_argument("--output", '-o', type=str, default='data')
    args = argp.parse_args()

    kominfo: Kominfo = Kominfo()

    output_type: str = f'all'  
    
    if(args.keyword):
        output_type: str = f'keyword/{args.keyword}'
    elif(args.group):
        output_type: str = f'group/{Group[args.group].name}'
    elif(args.org):
        output_type: str = f'org/{Organisasi[args.org].name}'

    output: str = f'{args.output}/{output_type}'

    data: dict = kominfo.search(
        q=args.keyword, 
        groups=Group[args.group].value if args.group else None, 
        org=Organisasi[args.org].value if args.org else None,
        page=args.page
    )

    if(data):
        if(not os.path.exists(output)):
            os.makedirs(output)

        with open(f'{output}/page_{args.page}.json', 'w') as file:
            file.write(dumps(data, indent=2))
        
        logging.info(f'file save on {output}/page_{args.page}.json')
