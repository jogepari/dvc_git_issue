from pathlib import Path
import argparse

def argparser_setup(extracting_data='features'):
    description = f"""
    Extract {extracting_data} from raw data.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--location_dir', type=Path, default='data/raw',
        help="""path to the raw data dir (excluding subdir)""")

    parser.add_argument(
        '--subdir', type=Path,
        help=f"""subdir of location_dir with files to extract {extracting_data} from""")

    parser.add_argument(
        '--output_dir', type=Path, default='data/interim',
        help="""preprocessed data dir (excluding subdirs)""")
    
    parser.add_argument(
        '--param',)

    return parser

parser = argparser_setup('features')
args = parser.parse_args()

data_dir = args.location_dir / args.subdir
output_path = args.output_dir

for fpath in Path(data_dir).rglob('*.txt'):
    input_text = fpath.read_text()
    out_file_path = Path(output_path).joinpath(fpath.name)
    out_file_path.parent.mkdir(exist_ok=True, parents=True)
    out_file_path.write_text(input_text + f'\n{args.param}')
    
