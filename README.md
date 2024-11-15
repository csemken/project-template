# Project template

## Usage

This is a reusable project template.
To use it:

1. Create a fork of the repository
2. Adjust this README and the wiki
3. Update the dvc remote in `.dvc/config` and push existing files
4. Remove test data and module
5. (Optional) Import the project on overleaf (New project → Import from GitHub → `repo_name` → Import to Overleaf) and set the main document (Menu → Main document → paper_slides/paper.tex)

## File structure

```
analysis       # code for data analysis
└── *          # module
bin            # maintenance scripts
data           # data
├── raw        # raw input data
│   └── *      # source
├── input      # input data
│   └── *      # module
├── output     # output data
│   └── *      # module
└── release    # publication output
paper_slides   # tex code
└── *          # manually created assets
```

## Getting started

The [manual](wiki/Introduction) in the wiki explains the general setup.
The analysis setup is explained in `analysis/README.md`.
