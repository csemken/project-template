# Project template

## Usage

This is a reusable project template.
To use it:

1. Create a fork of the repository
2. Adjust this README and the wiki

## File structure

```
analysis       # code for data analysis
└── *          # module
bin            # maintenance scripts
config         # configuration files
data           # data
├── raw        # raw input data
│   └── *      # source
├── input      # input data
│   └── *      # module
├── output     # output data
│   └── *      # module
└── release    # publication output
paper_slides   # tex code
├── release    # -> /data/release/
└── *          # manually created assets
```

## Getting started

The [manual](wiki/Introduction) in the wiki explains the general setup.
The analysis setup is explained in `analysis/README.md`.
